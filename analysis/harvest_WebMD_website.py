#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "transfer url data from WB MED https://www.webmd.com webpage with patient information and adding to data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_infos(tags, url):
        if url.startswith('https://www.webmd.com/'):
            #urls = ''.join(url)

            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', }
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')

                # get article text
                try:
                    text = soup.get_text()
                    text = text.replace('\n', ' ').replace('\r', ' ').replace('→', ' ')

                    try:
                        text = re.sub('[^a-zA-Z0-9 \n\.]', ' ', text)
                    except Exception as e:
                        print(e)
                    article_title = get_article_title(url)


                    infos = pd.DataFrame({'category_id': 'popular',
                                         'text_id': 'WebMD'+article_title,
                                          'tags': tags,
                                         'venue':'',
                                         'data-source':'WebMD',
                                         'url':[url],
                                         'text': [text]})
                    return infos

                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)



def get_article_title(url):
    article_title = url.split('https://www.webmd.com/' )[1]
    article_title = article_title.split('.pdf')[0]
    return article_title

def main():
    urls_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/popular_WebMD_urls-2.csv', sep=',')
    urls_df.drop_duplicates(inplace=True)
    infos_df = pd.DataFrame(columns=['category_id','text_id','tags','venue','data-source','url','text'])
    for index, row in urls_df.iterrows():
        tags = str(row[0])
        url = str(row[1])

        infos = get_infos(tags, url)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)



    infos_df.to_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/popular_WebMed_text-2.csv', index=False)
    print('done')
if __name__ == '__main__':
    main()