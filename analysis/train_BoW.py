#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("classify FSoLS-24-v2 - FSoLS-25-v5 datatset with BoW")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024-2025 by Eva Seidlmayer"
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
from scipy.sparse import issparse
from collections import Counter
import joblib

def load_dataset(input_file_csv):
    # Load dataset

    df = pd.read_csv(input_file_csv, sep=",", usecols = ['text', 'category_id'])
    df = df.replace(r'^\s*$', np.nan, regex=True)
    #df = df.dropna()
    df = df.sample(frac=1)
    df = df.astype(str)
    texts = df["text"].to_list()
    labels = df["category_id"].to_list()
    category_counts = Counter(labels)
    print('category counts:', category_counts)
    print("data input lists created")
    return texts, labels

def vectorize_text(texts):
    vectorizer = CountVectorizer() # converts texts into a matrix of token counts
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

def binarize_ml_targets(labels):
    mlb = MultiLabelBinarizer() #transforms list of labels in a binary matrix
    labels = [[label] for label in labels]  # Convert each label into a list
    y = mlb.fit_transform(labels)
    return y, mlb

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_csv")
    args = parser.parse_args()

# load dataset
    texts, labels = load_dataset(args.input_file_csv)

# Convert text to Bag-of-Words representation
    X, vectorizer = vectorize_text(texts)
    print('texts vectorized')

# Binarize the multi-label targets
    y, mlb = binarize_ml_targets(labels)
    print('labels binarized')

# Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print('dataset split')

# Initialize  and train  classifier
    classifier = OneVsRestClassifier(LogisticRegression(max_iter=500, multi_class='multinomial', solver='lbfgs')) #fits one classifier per label and allows for multi-label classification
    #model = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
    #classifier = OneVsRestClassifier(XGBClassifier())
    #classifier = OneVsRestClassifier(SVC(kernel='linear')) #Support Vector Machine
    #classifier = OneVsRestClassifier(AdaBoostClassifier())
    #classifier = OneVsRestClassifier(RandomForestClassifier())
    classifier.fit(X_train, y_train) # train classifier
    joblib.dump(classifier,
                '2025-01-10_FSoLF-25-v5_LRG_classifier.pkl')
    joblib.dump(vectorizer, '2025-01-10_FSoLF-25-v5_LRG_vectorizer.pkl')
    print('classifier trained and dumped')


    # evaluate: make prediction
    y_pred = classifier.predict(X_test)
    print('prediction made')

# calculate f-1 score (weighted)
    f1 = f1_score(y_test, y_pred, average= 'weighted')
    class_rep = classification_report(y_test, y_pred, target_names=mlb.classes_)

    print(f"F1 Score (Weighted): {f1}")
    print("\nClassification Report:\n", class_rep)

# understand the importance of words
    top_n = 50
    feature_names = vectorizer.get_feature_names_out()
    print('feature names', feature_names)

    # For each category, display the top N most important words
    for i, clf in enumerate(classifier.estimators_):
        category_name = mlb.classes_[i]
        feature_importance = clf.coef_.flatten()
    # Sort the features by their importance (absolute value) for the current category
        sorted_indices = np.argsort(np.abs(feature_importance))[::-1]


         # Get the top N words for this category
        top_features = [(feature_names[idx], feature_importance[idx]) for idx in sorted_indices[:top_n]]


            # Display the top words with their coefficients
        print(f"\nCategory xxx: {category_name}")
        for word, coef in top_features:
            print(f"Word: {word}, Coefficient: {coef:.4f}")




if __name__ == "__main__":
    main()












