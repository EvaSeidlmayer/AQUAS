#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "request pretrained BERT model"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023-2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import argparse
import torch
from transformers import BertTokenizer, AutoModelForSequenceClassification
import pandas as pd
import json



BERT_MODEL_IDENTIFIER = "models/FSoLS-24-v5_Bertbase_e3_lr3e-5_mlclass"

max_length = 512

try:
    import wandb
except ImportError:
    print("Wandb not installed. Not using wandb. To use: pip install wandb")





def load_abstract_input():
    with open('dbrecordid2abstract.json', 'r') as file:
        text_dict= json.load(file)
        text_df = pd.DataFrame(list(text_dict.items()), columns=["dbrecordid", "text"])
    return text_df

def load_doi_input():
    with open('dbrecordid2doi.json', 'r') as file:
        doi_dict = json.load(file)
        doi_df= pd.DataFrame(list(doi_dict.items()), columns= ['dbrecordid', 'doi'])
    return doi_df


def preproces_text(df,  model):
    # preprocess text

    for index, row in df.iterrows():
        text = row['text']
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        tokens = tokenizer(text, max_length=max_length, padding="max_length", truncation=True, return_tensors='pt')
        input_ids = tokens['input_ids']
        attn_mask = tokens['attention_mask']
        #print("text is preprocessed")

        # apply model on text and add results to dataframe
        pred_0, pred_1, pred_2, pred_3 = apply_model(input_ids, attn_mask, model)

        df.at[index, 'pred_sci'] =  pred_0
        df.at[index, 'pred_pop']  =  pred_1
        df.at[index,'pred_dis']   = pred_2
        df.at[index,'pred_alt']   = pred_3
    return df




def apply_model(input_ids, attn_mask,  model):
    output = model(input_ids=input_ids, attention_mask= attn_mask)

    logits = output['logits']
    sigmoid_output =torch.sigmoid(logits)
    soft_output = torch.softmax(logits, -1)


    #print(f'text {dbrecordid} processed without softmax {sigmoid_output}')
    #print('with softmax', soft_output)

    sigmoid = sigmoid_output.tolist()
    #print(sigmoid)
    pred_0, pred_1, pred_2, pred_3= sigmoid[0][0], sigmoid[0][1], sigmoid[0][2], sigmoid[0][3]
    wandb.log(
        {"pred_sci": pred_0, "pred_pop": pred_1, "pred_dis": pred_2, "pred_alt": pred_3})
    return pred_0, pred_1, pred_2, pred_3


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("model", help="Path to the pre-trained model")
    args = argparser.parse_args()

    wandb.init(
        # Set the project where this run will be logged
        project="AQUAS",
        # Track hyperparameters and run metadata
    )

    # Load the trained model and inputs
    model = AutoModelForSequenceClassification.from_pretrained(args.model)
    wandb.watch(model)
    print("weight and biases is tracking")
    text_df = load_abstract_input()
    doi_df = load_doi_input()
    df = pd.merge(text_df, doi_df, on='dbrecordid')

    # preprocess text and apply model
    df = preproces_text(df,  model)
    print('done')
    df.to_csv('2025-01-06_AQUAS4LIVIV_pred.csv')



if __name__ == '__main__':
    main()
