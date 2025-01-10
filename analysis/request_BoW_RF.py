#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("classif unknown data with pretrained BoW classifier")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2025 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import joblib
import pandas as pd
import numpy as np
from collections import Counter
import json



def load_abstract_input():
    with open('/home/ruth/ProgrammingProjects/AQUS/AQUAS/AQUAS4LIVIVO/2023-03_KE_dbrecordid_doi_abstracts/dbrecordid2abstract.json', 'r') as file:
        text_dict= json.load(file)
        text_df = pd.DataFrame(list(text_dict.items()), columns=["dbrecordid", "text"])
    return text_df

def load_doi_input():
    with open('/home/ruth/ProgrammingProjects/AQUS/AQUAS/AQUAS4LIVIVO/2023-03_KE_dbrecordid_doi_abstracts/dbrecordid2doi.json', 'r') as file:
        doi_dict = json.load(file)
        doi_df= pd.DataFrame(list(doi_dict.items()), columns= ['dbrecordid', 'doi'])
    return doi_df

def proces_text(df,  classifier, vectorizer):

    for index, row in df.iterrows():
        text = row['text']
        text_list = [text]
        #print(text_list)

        text_vectorized = vectorizer.transform(text_list)
        predictions = classifier.predict(text_vectorized)
        predictions_int = predictions.astype(int).tolist()
        print(predictions_int)
        df.at[index, 'pred_0'] = predictions_int[0][0]
        df.at[index, 'pred_1'] = predictions_int[0][1]
        df.at[index, 'pred_2'] = predictions_int[0][2]
        df.at[index, 'pred_3'] = predictions_int[0][3]
    return df





def main():
    # Load the trained classifier and vectorizer from the file
    classifier = joblib.load(
        '/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-06_FSoLF-25-v5_random_forest_classifier.pkl')
    vectorizer = joblib.load(
        '/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-06_FSoLF-25-v5_vectorizer.pkl')

    text_df = load_abstract_input()
    doi_df = load_doi_input()
    df = pd.merge(text_df, doi_df, on='dbrecordid')

    df = proces_text(df, classifier, vectorizer)
    print(df)

    df.to_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/AQUAS4LIVIVO/2025-01-06_AQUAS4LIVIV_RF_pred.csv')
    print('done')

if __name__ == "__main__":
    main()
