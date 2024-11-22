#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "request pretrained BERT model"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import argparse
import torch
from transformers import BertTokenizer, AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

# Define the model identifier and maximum length
BERT_MODEL_IDENTIFIER = "models/FSoLS-24-v4_Fewshot_specter_t512_e5_lr3e-5_mlclass"
max_length = 512


class EvalDataset(Dataset):
    def __init__(self, input_ids, attention_masks, labels):
        self.input_ids = torch.tensor(input_ids, dtype=torch.long)
        self.attention_masks = torch.tensor(attention_masks, dtype=torch.long)
        self.labels = torch.tensor(labels, dtype=torch.float)  # One-hot encoded



    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "input_ids": self.input_ids[idx],
            "attention_mask": self.attention_masks[idx],
            "label": self.labels[idx],
        }


def load_model(model):
    model = AutoModelForSequenceClassification.from_pretrained(model)
    model.eval()  # Set the model to evaluation mode
    return model

def load_evaldata(evaldata):
    df = pd.read_csv(evaldata)
    texts = df["text"].to_list()
    labels = df["category_id"].to_list()
    return texts, labels

# Preprocess the dataset
def tokenize(texts):
    # Load the tokenizer
    tokenizer = BertTokenizer.from_pretrained('allenai/specter')
    tokens =  tokenizer(texts, max_length=max_length, padding="max_length", truncation=True)
    return tokens

def convert_labels(labels):
    # Convert labels to numerical values
    label_map = {'scientific': 0, 'popular': 1, 'disinfo': 2, 'alternative_science':3}
    labels_conv = [label_map[label] for label in labels]
    labels_conv = torch.tensor(labels_conv, dtype=torch.long)
    labels_onehot = torch.nn.functional.one_hot(labels_conv, num_classes=4).float()
    print("labels converted")
    return labels_onehot

def prepare_dataloader(tokens, labels, batch_size=1):
    dataset = EvalDataset(tokens["input_ids"], tokens["attention_mask"], labels)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    return dataloader





def evaluate_model(model, dataloader, device):
    all_logits = []
    all_labels = []

    with torch.no_grad():
        model.to(device)
        model.eval()

        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["label"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            assert logits.size(1) == 4, "Something went terribly wrong"
            all_logits.append(logits)
            all_labels.append(labels)

    all_logits = torch.cat(all_logits, dim=0)
    all_labels = torch.cat(all_labels, dim=0)

    # Calculate accuracy
    # This only makes sense for single label..
    # ..we keep it to compare with softmax BERT..
    # ..and because our eval set is actually single label
    multiclass_accuracy = (
        (all_logits.argmax(dim=-1) == all_labels.argmax(dim=-1)).float().mean()
    ).item()

    # Turn logits into binary Yes/No decision per class with threshold 0.5
    # for multi-label classification (instead of taken just the maximum)
    predictions = torch.sigmoid(all_logits) > 0.5

    # calculate f1 score
    #all_labels= all_labels.long().numpy()
    all_labels = all_labels.cpu().numpy()
    #predictions =predictions.long().numpy()
    predictions = predictions.cpu().numpy()
    f1 = f1_score(all_labels, predictions, average="weighted")

    # calculate accuracy per class
    target_class = ["class scientific", "class popular scientific", "class disinformation", "class alternative science"]

    # classification report
    class_rep = classification_report(
        all_labels, predictions, target_names=target_class
    )
    return multiclass_accuracy, f1, class_rep




def main():
    # Parse command-line arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument("model", help="Path to the pre-trained model")
    argparser.add_argument("evaldata", help="Path to the evaluation data set")
    args = argparser.parse_args()

    model = load_model(args.model)

    texts, labels = load_evaldata(args.evaldata)
    tokens = tokenize(texts)
    labels_onehot = convert_labels(labels)
    dataloader = prepare_dataloader(tokens, labels_onehot)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    multiclass_accuracy, f1, class_rep = evaluate_model(model, dataloader, device)
    class_rep = str(class_rep)
    print("accuracy:", multiclass_accuracy, "f1:", f1, "classification_report:", class_rep)

    print('done')

if __name__ == "__main__":
    main()
