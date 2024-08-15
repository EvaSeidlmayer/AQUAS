#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "classify FSoLS-24-v2 datatset with BoW"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import argparse
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import f1_score, classification_report
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

def load_dataset(input_file_csv):
    # Load dataset
    df = pd.read_csv(input_file_csv, sep=",")
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna()
    df = df.sample(frac=1)
    df = df.astype(str)
    texts = df["text"].to_list()
    labels = df["category_id"].to_list()
    print("data input lists created")
    return texts, labels

def vectorize_text(texts):
    vectorizer = CountVectorizer() # converts texts into a matrix of token counts
    X = vectorizer.fit_transform(texts)
    return X

def binarize_ml_targets(labels):
    mlb = MultiLabelBinarizer() #transforms list of labels in a binary matrix
    y = mlb.fit_transform(labels)
    return y

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_csv")
    args = parser.parse_args()

# load dataset
    texts, labels = load_dataset(args.input_file_csv)

# Convert text to Bag-of-Words representation
    X = vectorize_text(texts)
    print('texts vectorized')

# Binarize the multi-label targets
    y = binarize_ml_targets(labels)
    print('labels binarized')

# Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print('dataset split')

# Initialize  and train  classifier
    #classifier = OneVsRestClassifier(LogisticRegression(max_iter=500)) #fits one classifier per label and allows for multi-label classification
    #classifier = OneVsRestClassifier(XGBClassifier())
    #classifier = OneVsRestClassifier(SVC(kernel='linear')) #Support Vector Machine
    #classifier = OneVsRestClassifier(AdaBoostClassifier())
    classifier = OneVsRestClassifier(RandomForestClassifier())
    classifier.fit(X_train, y_train) # train classifier
    print('classifier trained')

# evaluate: make prediction
    y_pred = classifier.predict(X_test)
    print('prediction made')

# calculate f-1 score (weighted)
    mlb = MultiLabelBinarizer() #transforms list of labels in a binary matrix

    f1 = f1_score(y_test, y_pred, average= 'weighted')
    #target_class = ["class scientific", "class popular scientific", "class disinformative", "class alternative scientific"]
    target_class = mlb.classes
    class_rep = classification_report(y_test, y_pred, target_names=target_class)

    print(f"F1 Score (Weighted): {f1}")
    print("\nClassification Report:\n", class_rep)


if __name__ == "__main__":
    main()












