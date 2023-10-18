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

#cols = ["category_id", "text_id", "venue", "data_source", "url", "tags", "title", "text"]
cols= ['category_id', 'text']


# scientifi-scc
def compile_scientific():
    scientific_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/scientific_PMC-PDF_basic-data_2023-09-21.csv', sep=',', usecols=cols)
    scientific_df = scientific_df.sample(frac=1)
    print('number of science paper:', len(scientific_df))
    return scientific_df

def compile_pop():
    # popular scientific
    popscience_df_1 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/popscience_wikipedia-text_2023-10-07.csv', sep=',', usecols=cols)
    popscience_df_2 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/popscience_medlineplus_text_2023-10-07.csv', sep=',', usecols=cols)
    # mayoclinic!
    popscientific_df = pd.concat([popscience_df_1, popscience_df_2], ignore_index= True)
    popscientific_df = popscientific_df.sample(frac=1)
    print('number of popscience paper:', len(popscientific_df))
    return popscientific_df

def compile_disinfo():
    breitbart1_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_breitbart-abortion_text_2023-09-22.csv', sep=',', usecols=cols)
    breitbart2_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_breitbart-transgender_text_2023-09-21.csv', sep=',', usecols=cols)
    mercola1 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_Mercola_text_2023-09-22.csv', sep=',', usecols=cols)
    mercola2 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_Mercola_text_2023-09-25.csv', sep=',', usecols=cols)
    mercola3 = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_Mercola_text_2023-10-05.csv', sep=',', usecols=cols)
    healthnews_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_healthnews_2023-09-29.csv', sep=',', usecols=cols)
    health_impact_news_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_healthimpactnews_2023-10-03.csv', sep=',', usecols=cols)

    disinfo_df = pd.concat([breitbart1_df, breitbart2_df], ignore_index=True)
    mercola = pd.concat([mercola1, mercola2], ignore_index=True)
    mercola = pd.concat([mercola, mercola3], ignore_index=True)
    disinfo_df = pd.concat([disinfo_df, mercola], ignore_index=True)
    disinfo_df = pd.concat([disinfo_df, healthnews_df], ignore_index=True)
    disinfo_df = pd.concat([disinfo_df, health_impact_news_df], ignore_index=True)
    disinfo_df = disinfo_df.sample(frac=1)
    print('number of desinfo paper:', len(disinfo_df))

    return disinfo_df

# alternative
def compile_alternative():
    alt1_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/alternative_homeopathicjournal_PDFs.csv', sep=',', usecols=cols)
    alt2_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/alternative_Indian-research-Homeopathy_PDF-2023-08-25.csv', sep=',', usecols=cols)
    alt3_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/alternative_PAAM-goetheaneum-PDF-2023-10-07.csv', sep=',', usecols=cols)
    alt_df= pd.concat([alt1_df, alt2_df], ignore_index=True)
    alternative_df = pd.concat([alt_df, alt3_df], ignore_index=True)
    alternative_df = alternative_df.sample(frac=1)
    print('number of alternative science paper:', len(alternative_df))
    return alternative_df


def main():

    scientific_df = compile_scientific()
    popscientific_df = compile_pop()
    disinfo_df = compile_disinfo()
    alternative_df = compile_alternative()

    number_disinfo = len(disinfo_df)

    final_dataset = pd.concat([scientific_df.head(number_disinfo), popscientific_df.head(number_disinfo)], ignore_index=True)
    final_dataset = pd.concat([final_dataset, disinfo_df], ignore_index=True)
    final_dataset = pd.concat([final_dataset, alternative_df.head(number_disinfo)], ignore_index=True)


    final_dataset.to_csv('data/2023-10_final_dataset.csv', index=False)

    print('number of final data set', len(final_dataset))
    print('done')

if __name__ == "__main__":
    main()

