#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "get data on health topics from WHO webpage (https://www.who.int/health-topics/); urls scraped by scrape_website-urls.py"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_infos(row):
    if row.startswith('https://www.who.int/health-topics/'):
        url = ''.join(row)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # get article text
            try:
                text = soup.get_text()
                text = text.replace('\n', '').replace('\r', '').replace('→', '')
                text = text.strip()
                text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
                article_title = get_article_title(url)

                infos = pd.DataFrame({'category-id': 'popular_science',
                                      'text-id': 'WHO',
                                      'venue': '',
                                      'data-source': 'WHO: ' + article_title,
                                      'url': [url],
                                      'tags': '',
                                      'text': [text]})
                return infos

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


def get_article_title(url):
    article_title = url.split('https://www.who.int/health-topics/')[1]
    return article_title



def main():
    urls_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/popscience_who_urls.csv', skiprows=[3] , sep=',')
    urls_df.drop_duplicates(inplace=True)

    print(urls_df)
    infos_df = pd.DataFrame(columns=['category-id','text_id','venue','data-source','url','tags','text'])
    for index, row in urls_df.iterrows():
        row = str(row[0])

        infos = get_infos(row)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


    infos_df.to_csv('data/popscience_WHO_text_2023-09-20.csv', index=False)
    print('done')



if __name__ == '__main__':
    main()
