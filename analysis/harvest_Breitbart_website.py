#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "get data on health topics from Breitbart website ; urls scraped by scrape_website-urls.py"
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
    if row.startswith('https://www.breitbart.com/tag/abortion//'):
        url = ''.join(row)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # get article text
            try:
                text = soup.get_text()
                text = text.split('COMMENTS')[0]
                #text = text.split('Biden Impeachmentrussell brand2024 RaceBroken BorderWoke WildDem City CrimeUAW Strike')[1]


                text = text.replace('brand2024 RaceBroken BorderWoke Wild!Dem City CrimeUAW Strike', '').replace('AmericaWorld NewsVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill Exclusive VideoWiresPodcastsBreitbart', '')
                text = text.replace('Enable Accessibility', '').replace('Skip to Content', '').replace('Politics Entertainment Media Economy World London', '')
                text = text.replace('Biden', '').replace('Europe Border', '').replace('PoliticsEntertainmentMediaEconomyWorldLondon', '').replace('InspiredExclusive VideoWiresPodcastsBreitbart', '')
                text = text.replace('\n', '').replace('\r', '').replace('/ EuropeBorder / Cartel ChroniclesIsrael / Middle EastAfricaAsiaLatin', '').replace('Exclusive VideoWiresB', '')
                text = text.replace(' AmericaAll WorldVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill', '').replace(' BREITBART  AmericaWorld NewsVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill ', '')
                text = text.replace('InspiredExclusive VideoWiresPodcastsBreitbart', '').replace('News DailyB InspiredAbout', '').replace('UsPeopleNewsletters', '').replace('BREITBART', '').replace('Impeachmentrussell', '')
                print(text)
                text = text.replace('Cartel', '').replace('Chronicles Israel', '').replace('Middle East', '')
                #AfricaAsiaLatin AmericaAll WorldVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill Exclusive VideoWiresB Inspired BREITBARTEnable AccessibilityPoliticsEntertainmentMediaEconomyWorldLondon  EuropeBorder  Cartel ChroniclesIsrael  Middle EastAfricaAsiaLatin AmericaWorld NewsVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill Exclusive VideoWiresPodcastsBreitbart News DailyB InspiredAbout UsPeopleNewsletters BREITBARTBiden Impeachmentrussell brand2024 RaceBroken BorderWoke WildDem City CrimeUAW', '')

                                         #Cartel ChroniclesIsrael  Middle EastAfricaAsiaLatin AmericaAll WorldVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill Exclusive VideoWiresB Inspired BREITBARTEnable AccessibilityPoliticsEntertainmentMediaEconomyWorldLondon  EuropeBorder  Cartel ChroniclesIsrael  Middle EastAfricaAsiaLatin AmericaWorld NewsVideoTechSportsOn the HillOn the Hill ArticlesOn The Hill Exclusive VideoWiresPodcastsBreitbart News DailyB InspiredAbout UsPeopleNewsletters BREITBARTBiden Impeachmentrussell brand2024 RaceBroken BorderWoke WildDem City CrimeUAW Strike', '')
                text = text.strip()
                #text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
                article_title = get_article_title(url)

                infos = pd.DataFrame({'category_id': 'disinfo',
                                      'text_    id': 'Breitbart:'+article_title,
                                      'venue': '',
                                      'data_source': 'Breitbart',
                                      'url': [url],
                                      'tags': 'transgender',
                                      'text': [text]})
                return infos

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


def get_article_title(url):
    article_title = url.split('https://www.breitbart.com/tag/abortion//')[1]
    return article_title




def main():
    urls_df = pd.read_csv('/AQUS/AQUAS/data/disinfo/disinfo_breitbart-abortion_urls.csv', skiprows=[3], sep=',')
    urls_df.drop_duplicates(inplace=True)

    infos_df = pd.DataFrame(columns=['category_id','text_id','venue','data_source','url','tags','text'])
    for index, row in urls_df.iterrows():
        row = str(row[0])

        if row.startswith('https://www.breitbart.com/tag/abortion//author'):
            continue

        infos = get_infos(row)
        print('jkljkljkl', infos)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)


        infos_df.to_csv('data/disinfo_breitbart-abortion_text_2023-09-22.csv', index=False)
    print('done')



if __name__ == '__main__':
    main()
