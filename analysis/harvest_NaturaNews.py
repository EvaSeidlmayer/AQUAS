#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest data from https://www.naturalnews.com and add it to data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_infos(row, i):
    print(row)
    tag = row[0]
    url = row[1]
    i =+ 1

    article_title = get_article_title(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get article text
    try:
        text = soup.get_text()

    except Exception as e:
        print(e)

    print(text)


    cleaned_txt = ' '.join(text.split())
    cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_txt)



    infos = pd.DataFrame({'category_id': 'disinfo',
                          'text_id': 'NaturalNews:' + str(article_title),
                          'venue': '',
                          'data_source': 'NaturalNews',
                          'url': [url],
                          'tags': [tag],
                          'text': [cleaned_txt]})

    return infos, i


def get_article_title(url):
    try:
        article_title = url.split('https://www.naturalnews.com')[1]
        return article_title
    except Exception as e:
        print(e)

    return article_title


def main():
    urls_df = pd.read_csv('/AQUS/AQUAS/data/data-set-topic-wise_2024/disinfo_naturalnews_urls.csv', sep=',')
    urls_df.drop_duplicates(inplace=True)




    print('vorher', urls_df.shape)
    i = 0
    infos_df = pd.DataFrame(columns=['category_id','text_id','venue','data_source','url','tags','text'])
    for index, row in urls_df.iterrows():
        infos, i = get_infos(row, i)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


        infos_df.to_csv('data/data-set-topic-wise_2024/disinfo_naturalnews_2024-04-11.csv', index=False)
    print(i)
    print('done')



if __name__ == '__main__':
    main()
