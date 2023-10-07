#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "train datatset with BERT"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification
import numpy as np
import tensorflow as tf
import argparse
import os
from sklearn.metrics import f1_score


def load_dataset(input_file_csv):
    # Load dataset
    df = pd.read_csv(input_file_csv, sep=',')
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna()
    df = df.sample(frac=1)
    df = df.astype(str)
    texts = df['text'].to_list()
    labels = df['category_id'].to_list()
    print('data input lists created')
    return texts, labels


def tokenize(texts):
    # Load the tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Tokenize the text data
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="tf")
    print('texts are tokenized')
    return  inputs

def convert_labels(labels):
    # Convert labels to numerical values
    label_map = {'scientific': 0, 'popular_science': 1, 'disinfo': 2, 'alternative_science':3}
    labels = [label_map[label] for label in labels]
    labels_conv = tf.keras.utils.to_categorical(labels, num_classes=4)
    print('labels converted')
    return labels_conv

def calc_split_ratio(labels_conv):
    # 80% training 20% validation
    split_ratio = int(len(labels_conv) * 0.2)
    print('split_ratio defined')
    return split_ratio

def split_train_val_data(inputs, split_ratio, labels_conv):
    # Split the data into training and validation sets
    train_inputs, val_inputs = np.split(inputs['input_ids'], [split_ratio])
    train_masks, val_masks = np.split(inputs['attention_mask'], [split_ratio])
    train_labels, val_labels = np.split(labels_conv, [split_ratio])
    print('train/val -inputs, -masks, -labels created')
    return train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels

def fine_tune_BERT(train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels):
    # Fine-tune pre-trained BERT model
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)
    optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5, epsilon=1e-08, clipnorm=1.0)
    model.compile(optimizer=optimizer, loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
    model.fit([train_inputs, train_masks], train_labels, validation_data=([val_inputs, val_masks], val_labels), epochs=3, batch_size=8)
    print('BERT fine tuned')
    return model


def evaluate_model(model, val_inputs, val_masks, val_labels):
    # Evaluate  model
    results = model.evaluate([val_inputs, val_masks], val_labels, batch_size=8)

    output = model.predict([val_inputs, val_masks])
    predicted_labels = output.logits.argmax(axis=1)
    f1 = f1_score(val_labels.argmax(axis=1), predicted_labels, average='weighted')

    print("Validation Loss: {:.4f} Accuracy: {:.4f} F1-score: {:.4f}".format(*results, f1))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_csv')

    args = parser.parse_args()

    texts, labels = load_dataset(args.input_file_csv)
    inputs = tokenize(texts)
    labels_conv = convert_labels(labels)
    split_ratio = calc_split_ratio(labels_conv)
    train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels= split_train_val_data(inputs, split_ratio, labels_conv)
    model = fine_tune_BERT(train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels)
    evaluate_model(model, val_inputs, val_masks, val_labels)


main()