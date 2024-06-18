#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest text by PMID via Entrez-API from MEDLINE data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import pandas as pd
import argparse
import requests
import xml.etree.ElementTree as ET
import regex as re
import os



def get_xml(pmcid):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&rettype=full&retmode=xml"
    response = requests.get(url)
    xml = response.text
    '''
    try:
        x = data["esearchresult"]["idlist"]
        print(x)
    except Exception as e:
        print(e)
    
    with open(f"test_2024-06-06_{pmcid}.xml", "w") as file:
        file.write(data)
    '''
    return xml

def get_text(xml):
    root = ET.fromstring(xml)
    journal_meta = []
    article_meta = []
    text = []

    for element in root.findall('.//journal-meta'):
        journal_meta.extend((element.itertext()))

    for element in root.findall('.//article-meta'):
        article_meta.extend((element.itertext()))

    for element in root.findall('.//body'):
        text.extend(element.itertext())

    return ''.join(journal_meta) + ''.join(article_meta) + ''.join(text)

def clean_text(article_text):
    cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', article_text)
    cleaned_txt = os.linesep.join([s for s in cleaned_txt.splitlines() if s.strip()])
    cleaner_text = cleaned_txt.replace('\n', '').replace('\r', '')

    return cleaner_text
def compile_infos(cleaner_text, pmcid, tag):

    infos = pd.DataFrame({'category_id': 'scientific',
                          'text_id': 'PMC' + str(pmcid),
                          'venue': '',
                          'tags': tag,
                          'data_source': 'PMC',
                          'url': '',
                          'text': cleaner_text}, index=[0])

    return infos

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('topic')
    args = parser.parse_args()

    infos_df = pd.DataFrame(columns=['category_id','text_id','tags','venue','data-source','url','text'])
    tag = args.topic

    pmids = pd.read_csv(args.input, usecols=['pmid'])
    pmids = pmids['pmid'].tolist()
    for pmcid in pmids:
        xml = get_xml(pmcid)
        article_txt = get_text(xml)
        cleaner_text = clean_text(article_txt)

        infos = compile_infos(cleaner_text, pmcid, tag)
        infos_df = pd.concat([infos_df, infos], ignore_index=True)

        infos_df.to_csv(f'data/data-set-topic-wise_2024/content/raw_content/scientific_pmc_{tag}.csv', index=False)
    print('done')


if __name__ == '__main__':
    main()
