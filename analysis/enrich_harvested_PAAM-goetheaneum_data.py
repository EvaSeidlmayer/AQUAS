#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("enrich data produced by harvest_anthroposohic_getheaneumlist_PDF.py with article-title, venue, tags by Crossref")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
import subprocess
import jsonlines
import re


def get_infos_from_crossref(doi):
    subprocess.run(f"curl https://api.crossref.org/works/{doi} --output tmp.json".split())
    try:
        with jsonlines.open('./tmp.json') as reader:
            for obj in reader:

                # harvest publication title and ISSN from Crossref
                for titel in obj['message']['title']:
                    title = titel
                try:
                    for issn in obj['message']['ISSN']:
                        venue = 'ISSN:' + str(issn)
                except:
                    venue = ''

                try:
                    for subject in obj['message']['subject']:
                        tags = subject
                except:
                    tags = ''
                return title, venue, tags
    except jsonlines.jsonlines.InvalidLineError:
        print('WARNING NO Crossref file')
        return None



def main():
    df = pd.read_csv('/AQUAS/data/alternative_PAAM-goetheaneum-PDF-2023-09-19.csv')

    for index, row in df.iterrows():
        doi = row['text_id']
        print(doi)


        title, venue, tags = get_infos_from_crossref(doi)
        if None in (title, venue, tags):
            continue

        df.loc[df.index == index, 'text_id'] = doi
        df.loc[df.index == index, 'title'] = title
        df.loc[df.index == index, 'venue'] = venue
        df.loc[df.index == index, 'tags'] = tags
        df['text'] = re.sub('[^a-zA-Z0-9 \n\.]', '', df['text'].str)

    df.to_csv('data/anthropo_PAAM-goetheaneum-PDF-2023-09-19', index=None, header=None )


if __name__ == '__main__':
    main()

