#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "aggregate data from all categories to one set"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import csv
import sys
import pandas as pd

cols = ['category-id', 'text']
science_df_1 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2022-12-19.csv', sep=',', usecols=cols)
science_df_plosone = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/scientific_PlosONE_text.csv', sep=',', usecols=cols)
science_df_2 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-02-26.csv', sep=',', usecols=cols)
science_df = pd.concat([science_df_1, science_df_plosone], ignore_index=True)
science_df = pd.concat([science_df, science_df_2])
science_df_3 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-02-27.csv', sep=',', usecols=cols)
science_df_4 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-02-28.csv', sep=',', usecols=cols)
science_df_5 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-03-01.csv', sep=',', usecols=cols)
science_df_6 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-03-04.csv', sep=',', usecols=cols)
science_df_7 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-03-05.csv', sep=',', usecols=cols)
science_df_8 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/PMC-doi_text-2023-03-06.csv', sep=',', usecols=cols)

science_df = pd.concat([science_df, science_df_3])
science_df = pd.concat([science_df, science_df_4])
science_df = pd.concat([science_df, science_df_5])
science_df = pd.concat([science_df, science_df_6])
science_df = pd.concat([science_df, science_df_7])
science_df = pd.concat([science_df, science_df_8])
#print(science_df.head())
print('number of science paper:', len(science_df))

sys.exit()
popscience_df_1 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/popscience_wikipedia-text.csv', sep=',', usecols=cols)
popscience_df_2 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/popscience_medlineplus_text.csv', sep=',', usecols=cols)
popscience_df = pd.concat([popscience_df_1, popscience_df_2], ignore_index= True)
print('number of popscience paper:', len(popscience_df))

poynter_cols = ['label', 'text']
desinfo_df_1 = pd.read_csv('/AQUAS/data/desinfo_alternativenews_text.csv', sep=',', usecols=cols)
desinfo_df_2 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/desinfo_collectiveevolution_text.csv', sep=',', usecols=cols)
desinfo_df_3 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/desinfo_healthcancer_text.csv', sep=',', usecols=cols)
desinfo_df_4 = pd.read_csv('/AQUAS/data/desinfo_alternativenews_text.csv', sep=',', usecols=cols)
desinfo_df_5 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/kaggle/Covid19-misinformation/poynter_data.csv', sep=',', usecols= poynter_cols)
desinfo_df_5 = desinfo_df_5.replace(['misleading', 'false'], 3)
desinfo_df = pd.concat([desinfo_df_1, desinfo_df_2], ignore_index = True)
print(desinfo_df_5.head())
desinfo_df = pd.concat([desinfo_df, desinfo_df_3], ignore_index= True)
desinfo_df = pd.concat([desinfo_df, desinfo_df_4], ignore_index=True)
desinfo_df = pd.concat([desinfo_df, desinfo_df_5], ignore_index=True)
print('number of desinfo paper:', len(desinfo_df))

number_desinfo = len(desinfo_df)
ready_dataset = pd.concat([science_df.head(number_desinfo), popscience_df.head(number_desinfo)], ignore_index=True)
#print(ready_dataset.head())
ready_dataset = pd.concat([ready_dataset, desinfo_df], ignore_index=True)
print('number of final data set', len(ready_dataset))



ready_dataset.to_csv('data/2023-07_ready_dataset_inklPoynter.csv', index=False)
print('done')