#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "analyze decision tree rules from  random forrest"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import glob
import pandas as pd
import re
import itertools

rules_list = []
df_all = pd.DataFrame()
for name in glob.glob('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/RF_decisiontree/2024-10-29_random-forest-tree-rules_*_FSoLS-24-v4.text'):
    df = pd.read_csv(name)
    df.columns = ['term']
    df = df.stack().str.replace(r'|---', '').unstack()
    df = df.stack().str.replace(r'|   |', '').unstack()
    df = df.stack().str.replace(r'|', '').unstack()
    df = df.stack().str.replace('<=', '').unstack()
    df = df.stack().str.replace('>', '').unstack()
    df = df.stack().str.replace('truncated branch of depth', '').unstack()
    df_all = pd.concat([df_all, df])
    #print(df_all)
    items = df.iloc[:, 0].tolist()
    #print(items)
    #df_all.to_csv('data/data-set-topic-wise_2024/RF_decisiontree/2024-10-30_random-forrest_FSoLS-24-v4.csv')

    for term in items:
        cleaned_data = term.strip()

        cleaned_data = cleaned_data.split(' ')[0]
        cleaned_data = cleaned_data.replace('class:', '').strip()
        cleaned_data = cleaned_data.replace('\n', '')
        rules_list.append(cleaned_data)


#print(len(rules_list))

# Initialize counts as a dictionary
counts = {}

# Iterate over each term in the list
for term in rules_list:
    if term in counts:
        counts[term] += 1  # Increment count by 1 if term exists
    else:
        counts[term] = 1   # Initialize count to 1 if term does not exist
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
print(counts)
