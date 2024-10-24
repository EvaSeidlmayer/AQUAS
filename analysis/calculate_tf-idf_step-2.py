#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("calculate TGF-IDF for FSoLS-24-v2 and v3 datatset with nltk "
                   "separated in two steps due to long time of processing"
                   "this is step 1 ending up with TF-csv for all four categories ")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "



from itertools import islice

from fontTools.colorLib.builder import populateCOLRv0
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import nltk
import ssl
import math


def load_dfs():
    science_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/tfidf/2024-10-21_science_flat_list_prepared_tfidf_FSoLS-24-v4.csv')
    pop_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/tfidf/2024-10-21_popular_flat_list_prepared_tfidf_FSoLS-24-v4.csv')
    alt_science_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/tfidf/2024-10-21_alt_science_flat_list_prepared_tfidf_FSoLS-24-v4.csv')
    disinfo_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/tfidf/2024-10-21_disinfo_flat_list_prepared_tfidf_FSoLS-24-v4.csv')
    return science_df, pop_df, alt_science_df, disinfo_df

def merge_dfs(science_df, pop_df, alt_science_df, disinfo_df):
    # left join all dataframes:
    science_pop_df = science_df[["word", "TF"]].merge(
        pop_df[["word", "TF"]],
        on="word",
        how="outer",
        suffixes=("_sci", "_pop")).fillna(0)

    science_pop_alt_df = science_pop_df.merge(
        alt_science_df[["word", "TF"]],
        on="word",
        how="outer").fillna(0)
    science_pop_alt_df.rename(columns={"TF": "TF_alt"}, inplace=True)

    all_df = science_pop_alt_df.merge(
        disinfo_df[['word', 'TF']],
    on="word",
    how= "outer").fillna(0)
    all_df.rename(columns={"TF": "TF_dis"}, inplace=True)
    return all_df

def calculate_idf(all_df):
    # count in how many documents each word appears:
    all_df["dfi"] = all_df[["TF_sci", "TF_pop", "TF_alt", "TF_dis"]].ne(0).sum(axis=1)
    return all_df

def calculate_tfidf(all_df):
    all_df["TF-IDF_sci"] = all_df["TF_sci"] * all_df["dfi"].apply(
        lambda x: math.log10(3 / x))
    all_df["TF-IDF_pop"] = all_df["TF_pop"] * all_df["dfi"].apply(
        lambda x: math.log10(3 / x))
    all_df["TF-IDF_alt"] = all_df["TF_alt"] * all_df["dfi"].apply(
        lambda x: math.log10(3 / x))
    all_df["TF-IDF_dis"] = all_df["TF_dis"] * all_df["dfi"].apply(
        lambda x: math.log10(3 / x))
    return all_df

def visualize_sci(all_df):
    # create 2 dataframes with the top 10 words for each method:
    TF_IDF_sci =all_df[["word", "TF-IDF_sci"]].sort_values(by="TF-IDF_sci",
                                                                              ascending=False).head(25)
    TF_sci = all_df[["word", "TF_sci"]].sort_values(by="TF_sci", ascending=False).head(25)

    # plot:

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

    # barplot:
    ax1.barh(TF_sci["word"], TF_sci["TF_sci"], color="#f0027f", edgecolor="#f0027f")
    ax2.barh(TF_IDF_sci["word"], TF_IDF_sci["TF-IDF_sci"], color="#386cb0", edgecolor="#386cb0")

    # title:
    ax1.set_title("FSoLS-24-v4 Scientific texts TF")
    ax2.set_title("FSoLS-24-v4 Scientific texts TF-IDF")
    ax2.set_xticks([0, 0.001, 0.002, 0.003])

    for ax in fig.axes:  # iterate over ax1, ax2, ax3 to:
        ax.invert_yaxis()  # invert the y axis;
        ax.grid(False)  # eliminate grid;
        ax.title.set_color('black')  # set title font color to white;
        ax.tick_params(axis='x', colors='black')  # set x axis font color to white;
        ax.tick_params(axis='y', colors='black')  # set y axis font color to white;
        ax.set_facecolor('#00000000')  # set ax background color to #2E3031;
        ax.spines["top"].set_visible(False)  # eliminate spines;
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        #ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_color('black')

    # fig background color:
    #fig.patch.set_facecolor('#2E3031')
    fig.patch.set_facecolor('#00000000')
    # layout:
    fig.tight_layout()
    plt.show()

def visualize_pop(all_df):
    # create 2 dataframes with the top 10 words for each method:
    TF_IDF_pop =all_df[["word", "TF-IDF_pop"]].sort_values(by="TF-IDF_pop",
                                                                              ascending=False).head(25)
    TF_pop = all_df[["word", "TF_pop"]].sort_values(by="TF_pop", ascending=False).head(25)

    # plot:

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

    # barplot:
    ax1.barh(TF_pop["word"], TF_pop["TF_pop"], color="#f0027f", edgecolor="#f0027f")
    ax2.barh(TF_IDF_pop["word"], TF_IDF_pop["TF-IDF_pop"], color="#386cb0", edgecolor="#386cb0")

    # title:
    ax1.set_title("FSoLS-24-v4 Popular scientific texts TF")
    ax2.set_title("FSoLS-24-v4 Popular scientific texts TF-IDF")
    ax2.set_xticks([0, 0.001, 0.002, 0.003])

    for ax in fig.axes:  # iterate over ax1, ax2, ax3 to:
        ax.invert_yaxis()  # invert the y axis;
        ax.grid(False)  # eliminate grid;
        ax.title.set_color('black')  # set title font color to white;
        ax.tick_params(axis='x', colors='black')  # set x axis font color to white;
        ax.tick_params(axis='y', colors='black')  # set y axis font color to white;
        ax.set_facecolor('#00000000')  # set ax background color to #2E3031;
        ax.spines["top"].set_visible(False)  # eliminate spines;
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        # ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_color('black')

    # fig background color:
    fig.patch.set_facecolor('#00000000')
    # layout:
    fig.tight_layout()
    plt.show()

def visualize_alt(all_df):
    # create 2 dataframes with the top 10 words for each method:
    TF_IDF_alt =all_df[["word", "TF-IDF_alt"]].sort_values(by="TF-IDF_alt",
                                                                              ascending=False).head(25)
    TF_alt = all_df[["word", "TF_alt"]].sort_values(by="TF_alt", ascending=False).head(25)

    # plot:

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

    # barplot:
    ax1.barh(TF_alt["word"], TF_alt["TF_alt"], color="#f0027f", edgecolor="#f0027f")
    ax2.barh(TF_IDF_alt["word"], TF_IDF_alt["TF-IDF_alt"], color="#386cb0", edgecolor="#386cb0")

    # title:
    ax1.set_title("FSoLS-24-v4 Alternative scientific texts TF")
    ax2.set_title("FSoLS-24-v4 Alternative scientific texts TF-IDF")
    ax2.set_xticks([0, 0.001, 0.002, 0.003])

    for ax in fig.axes:  # iterate over ax1, ax2, ax3 to:
        ax.invert_yaxis()  # invert the y axis;
        ax.grid(False)  # eliminate grid;
        ax.title.set_color('black')  # set title font color to white;
        ax.tick_params(axis='x', colors='black')  # set x axis font color to white;
        ax.tick_params(axis='y', colors='black')  # set y axis font color to white;
        ax.set_facecolor('#00000000')  # set ax background color to #2E3031;
        ax.spines["top"].set_visible(False)  # eliminate spines;
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        # ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_color('black')

    # fig background color:
    fig.patch.set_facecolor('#00000000')
    # layout:
    fig.tight_layout()
    plt.show()


def visualize_dis(all_df):
    # create 2 dataframes with the top 10 words for each method:
    TF_IDF_dis =all_df[["word", "TF-IDF_dis"]].sort_values(by="TF-IDF_dis",
                                                                              ascending=False).head(25)
    TF_dis = all_df[["word", "TF_dis"]].sort_values(by="TF_dis", ascending=False).head(25)

    # plot:
    fig, (ax1) = plt.subplots()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

    # barplot:
    ax1.barh(TF_dis["word"], TF_dis["TF_dis"], color="#f0027f", edgecolor="#f0027f")
    ax2.barh(TF_IDF_dis["word"], TF_IDF_dis["TF-IDF_dis"], color="#386cb0", edgecolor="#386cb0")

    # title:
    ax1.set_title("FSoLS-24-v4 Disinformative texts TF")
    ax2.set_title("FSoLS-24-v4 Disinformative texts TF-IDF")
    ax2.set_xticks([0, 0.001, 0.002, 0.003])

    for ax in fig.axes:  # iterate over ax1, ax2, ax3 to:
        ax.invert_yaxis()  # invert the y axis;
        ax.grid(False)  # eliminate grid;
        ax.title.set_color('black')  # set title font color to white;
        ax.tick_params(axis='x', colors='black')  # set x axis font color to white;
        ax.tick_params(axis='y', colors='black')  # set y axis font color to white;
        ax.set_facecolor('#00000000')  # set ax background color to #2E3031;
        ax.spines["top"].set_visible(False)  # eliminate spines;
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        # ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_color('black')

    # fig background color:
    fig.patch.set_facecolor('#00000000')
    # layout:
    fig.tight_layout()
    plt.show()

def main():

    science_df, pop_df, alt_science_df, disinfo_df = load_dfs()
    all_df = merge_dfs(science_df, pop_df, alt_science_df, disinfo_df)

    all_df = calculate_idf(all_df)
    all_df = calculate_tfidf(all_df)
    visualize_sci(all_df)
    visualize_pop(all_df)
    visualize_alt(all_df)
    visualize_dis(all_df)
    print(all_df.head(25))





if __name__ == "__main__":
    main()