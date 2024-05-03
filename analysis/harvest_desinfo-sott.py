#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "transfer content data from desinfo url.csv; content from https://signsofthetimes.org.au/category/wellbeing/"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re




def get_infos(row):
    if row.startswith('https:'):
        url = ''.join(row)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=hdr)
            soup = BeautifulSoup(response.text, 'html.parser')


            # get article text
            try:
                text = soup.get_text()
                text = text.replace('\n\n', '').replace('\r', '')

                clean = text.split('Subscribe to our eNewsletter', )[0]
                clean = clean.replace('Current Faith Wellbeing Science & Tech Culture Podcast Fun eNews Subscribe Donate', '').replace('Search', '').replace('A Christian Perspective on the World Today', '').replace('LOG IN', '')
                clean = clean.replace('Current Faith Wellbeing Science & Tech Culture Podcast Fun eNews Subscribe Donate', '')
                clean = clean.replace('Welcome! Log into your account', '').replace('Forgot your password?', '').replace('Recover your password', '').replace('Signs of the Times', '').replace('Subscribe Donate ENews', '')

                article_title = get_article_title(url)

                infos = pd.DataFrame({'category_id': 'disinfo',
                                      'text_id': 'SOTT:'+article_title,
                                      'venue': '',
                                      'data_source': 'SOTT',
                                      'url': [url],
                                      'tags': '',
                                      'text': [clean]})
                return infos

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


def get_article_title(url):
    article_title = url.split('https://signsofthetimes.org.au')[1]
    return article_title



def main():
    urls_df = pd.read_csv('/AQUS/AQUAS/data/disinfo/desinfo_sott_urls.csv', sep=',')
    urls_df.drop_duplicates(inplace=True)

    infos_df = pd.DataFrame(columns=['category_id','text_id','venue','data_source','url','tags','text'])
    for index, row in urls_df.iterrows():
        row = str(row[0])

        infos = get_infos(row)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


        infos_df.to_csv('data/disinfo_sott_text_2023-09-24.csv', mode='w', index=False)
    print('done')



if __name__ == '__main__':
    main()
