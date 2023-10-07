#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest data from  https://healthimpactnews.com and add it to data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_infos(row, i):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = row
    i =+ 1


    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get article text
    try:
        text = soup.get_text()

    except Exception as e:
        print(e)



    try:
        txt = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
    except Exception as e:
        print(e)
    clean = txt.replace('\n', '').replace('\r', '')
    print(clean)


    article_title = get_article_title(url)

    infos = pd.DataFrame({'category_id': 'disinfo',
                          'text_id': 'BeforeItsNews:' + str(article_title),
                          'venue': '',
                          'data_source': 'BeforeItsNews',
                          'url': [url],
                          'tags': '',
                          'text': [clean]})

    return infos, i



def get_article_title(url):
    try:
        article_title = url.split('https://beforeitsnews.com/v3/list/v2_')[1]
        return article_title
    except Exception as e:
        print(e)









def main():
    urls_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/disinfo_beforeitsnews_urls.csv' , sep=',')
    urls_df.drop_duplicates(inplace=True)
    print(urls_df.tail())
    print('nachher', urls_df.shape)
    i = 0
    infos_df = pd.DataFrame(columns=['category_id','text_id','venue','data_source','url','tags','text'])
    for index, row in urls_df.iterrows():
        row = str(row[0])
        infos, i = get_infos(row, i)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


        infos_df.to_csv('data/disinfo_beforeitsnews_2023-10-04.csv', index=False)
    print(i)
    print('done')



if __name__ == '__main__':
    main()
