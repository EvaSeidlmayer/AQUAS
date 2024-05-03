#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = " get linked url from a given website url "
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "



import scrapy
from scrapy.linkextractors import LinkExtractor
import requests
from bs4 import BeautifulSoup
import argparse
import csv

argparser = argparse.ArgumentParser()
argparser.add_argument("url")
argparser.add_argument("output")
args = argparser.parse_args()


with open(f'/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/{args.output}', 'a') as file:

    url= args.url
    print('bbbbbb', url)
    #url = 'https://medlineplus.gov/healthtopics.html'
    #url = "http://www.naturalnews.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        try:
            if href.startswith("https"):
                print(href)
                file.write(href)
                file.write('\n')
            elif href.startswith("/"):
                print(url + href)
                file.write(url + href)
                file.write('\n')
        except Exception as e:
            print(e)



