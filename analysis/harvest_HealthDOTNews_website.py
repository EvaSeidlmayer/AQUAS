#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest data from https://natural.news and add it to data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_infos(tags, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get article text
    try:
        text = soup.get_text()

    except Exception as e:
        print(e)

    try:
        text = text.replace('\n', ' ').replace('\r', ' ')
        #.replace('Your NameYour emailMessage or CancelSCIENCEFOODHEALTHMEDICINEPOLLUTIONCANCERCLIMATE', ' '))
        #print(text)
    except Exception as e:
        print(e)

    try:
        clean_text = text.split('RECENT NEWS & ARTICLES')[0]
    except Exception as e:
        print(e)

    try:
        cleaner_text = clean_text.split('Sources include:')[0]
    except Exception as e:
        print(e)

    try:
        text = re.sub('[^a-zA-Z0-9 \n\.]', ' ', text)
    except Exception as e:
         print(e)

    try:
        text = re.split('Submit a correction', text)[0].strip()
    except Exception as e:
        print(e)

    article_title = get_article_title(url)

    infos = pd.DataFrame({'category_id': 'disinfo',
                          'text_id': 'HealthDOTNews:' + str(article_title),
                          'tags': tags,
                          'venue': '',
                          'data_source': 'HealthDOTNews',
                          'url': [url],

                          'text': [text]})

    return infos


def get_article_title(url):
    try:
        article_title = url.split('https://www.health.news')[1]
        return article_title
    except Exception as e:
        print(e)
    try:
        article_title = url.split('https://www.climate.news')[1]
        return article_title
    except Exception as e:
        print(e)
    try:
        article_title = url.split('https://www.censoredscience.news')[1]
        return article_title
    except Exception as e:
        print(e)
    try:
        article_title = url.split('https://www.medicine.news')[1]
        return article_title
    except Exception as e:
        print(e)
    try:
        article_title = url.split('https://www.pollution.news')[1]
        return article_title
    except Exception as e:
        print(e)
    try:
        article_title = url.split('https://www.cancer.news')[1]
        return article_title
    except Exception as e:
        print(e)


def main():
    urls_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/disinfo_HealthDOTNews_urls_2023.csv', sep=',')
    urls_df.drop_duplicates(inplace=True)

    #urls_df['deduplicate'] = urls_df['url'].replace(regex='https?://\S+/', value = '')
    #urls_df['deduplicate'] = urls_df['deduplicate'].replace(regex=['((?:19|20)\\d\\d)-(0?[1-9]|1[012])-([12][0-9]|3[01]|0?[1-9])-'], value='')
    #print('vorher', urls_df.shape)
    #urls_df = urls_df.drop_duplicates(subset=['deduplicate'] )
    #print(urls_df.tail())
    #print('nachher', urls_df.shape)
    #i = 0
    infos_df = pd.DataFrame(columns=['category_id','text_id','tags','venue','data_source','url','text'])
    for index, row in urls_df.iterrows():
        url = str(row[1])
        tags = str(row[0])

        infos = get_infos(tags, url)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


        infos_df.to_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/raw_content/disinfo_HealthDOTNews_text_2023.csv', index=False)
    print('done')



if __name__ == '__main__':
    main()
