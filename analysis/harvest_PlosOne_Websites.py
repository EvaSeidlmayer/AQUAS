#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "transfer url data from Plos One webpage with patient information and adding to data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import csv
import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup


infos_df = pd.DataFrame(columns=['category-id', 'text-id', 'text'])

url = 'https://everyone.plos.org/2023/04/25/world-malaria-day-a-community-effort-to-achieve-zero/'
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get article text
    try:
        text = soup.get_text()
        text = text.replace('\n', '').replace('\r', '')
        #cleaned_text = text.replace("MedlinePlusSkip navigation National Library of MedicineMenuHealth TopicsDrugs & SupplementsGeneticsMedical TestsMedical EncyclopediaAbout MedlinePlusSearchSearch MedlinePlusGOAbout MedlinePlusWhat's NewSite MapCustomer SupportHealth TopicsDrugs & SupplementsGeneticsMedical TestsMedical EncyclopediaEspaÃ±olYou Are Here:Home						Health Topics", " ")
        info = pd.DataFrame({'category-id': 1, 'text-id': [url], 'text': [text]})
        print(info)
        infos_df = pd.concat([infos_df, info], ignore_index=True)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

infos_df.to_csv('data/science_plosone_text.csv', index=False)