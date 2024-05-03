#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "improve text data, esp. remove NBSP"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "




import pandas as pd

df = pd.read_csv('/AQUS/AQUAS/data/disinfo/desinfo_alternativenews_text.csv', index_col=False)
infos_df = pd.DataFrame(columns=['category-id', 'text-id', 'text'])

for i, row in df.iterrows():
    txt = row['text']
    clean_text = ' '.join(txt.split())
    info = pd.DataFrame({'category-id': row['category-id'], 'text-id': row['text-id'], 'text': clean_text}, index=[0])
    infos_df = pd.concat([infos_df, info], ignore_index=True)
infos_df.to_csv('data/desinfo_alternativenews_text_2023-08-23.csv', index=False)



