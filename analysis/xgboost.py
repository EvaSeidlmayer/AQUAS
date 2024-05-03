#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("calculate xgboost on data corpus")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
from nltk.corpus import inaugural
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
import xgboost as xgb
import numpy as np
import argparse



def load_dataset(input_file_csv):
    # Load dataset
    df = pd.read_csv(input_file_csv, sep=",")
    #df = df.replace(r'^\s*$', np.nan, regex=True)
    #df = df.dropna()
    df = df.sample(frac=1)
    #data = df(np.arange(12).reshape((2779, 1)), columns=['text'])
    data = df(np.reshape((2779, 1)), columns=['text'])
    # label = df(np.random.randint(4, size=2779))
    label = df(np.random.randint(4, size=2779))
    dtrain = xgb.DMatrix(data, label=label)

    print("data input lists created")
    return data, label, dtrain






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_csv")
    args = parser.parse_args()
    data, label, dtrain = load_dataset(args.input_file_csv)
    print(len(data))
    print(type(label))

'''
    learning_rate = 3e-5
    epochs = EPOCH_AMOUNT

    
    tokens = tokenize(texts)
    labels_conv = convert_labels(labels)
    split_ratio = calc_split_ratio(labels_conv)
    print("SPLIT RATIO:", split_ratio)
    (
        train_inputs,
        val_inputs,
        train_masks,
        val_masks,
        train_labels,
        val_labels,
    ) = split_train_val_data(tokens, split_ratio, labels_conv)

    train_inputs = torch.tensor(train_inputs)
    val_inputs = torch.tensor(val_inputs)
    train_masks = torch.tensor(train_masks)
    val_masks = torch.tensor(val_masks)
    train_labels = torch.tensor(train_labels)
    val_labels = torch.tensor(val_labels)

   

   
'''


if __name__ == "__main__":
    main()
