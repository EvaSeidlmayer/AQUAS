#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "calculation of average text length"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd



def calculate_avarage_text_length(lengths_id, i, df_id):
    for index, row in df_id.iterrows():
        try:
            length = len(row['text'])
            lengths_id += length
            i += 1
        except Exception as e:
            print(e)


        average_length = lengths_id/i

        return average_length

def main():
    df = pd.read_csv(
        '/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-10-21_LSoLF-24-v4.csv')
    ids = ['scientific', 'popular', 'alternative_science', 'disinfo']

    for id in ids:
        lengths_id = 0
        i = 0
        df_id = df.loc[df['category_id'] == f'{id}']
        average_length = calculate_avarage_text_length(lengths_id, i, df_id)
        print(f"average text length of {id}:", average_length)

if __name__ == '__main__':
    main()
