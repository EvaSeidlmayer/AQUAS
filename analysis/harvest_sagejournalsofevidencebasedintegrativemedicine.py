#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("retrieve text from PDF-URLs "
                   "Journal of Evidence-Based Integrative Medicine")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import requests
import pandas as pd
import re
from pypdf import PdfReader
import urllib
import glob



def download_pdf(url):
    path = "data/2024-05-02_dummy_anthropo-PDF.pdf"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')

    r = urllib.request.urlopen(req).read().decode('utf-8')
    with open(path, 'w', encoding="utf-8") as f:
        f.write(r)
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}
    # response = requests.get(url, headers=headers)
    response = urllib.request.urlopen()
    pdf = open(path, 'wb')
    pdf.write(response.content)
    pdf.close()
    '''
    print('rrrrrrrrrrrrrrr', r)





    return path


def pdf_to_text(path):
    # load pdf
    print('convert pdf to txt')
    print(path)
    try:
        reader = PdfReader(path, strict=False)
        print('ppppppppppp', reader)
        page = reader.pages[0]
        pdf_text = page.extract_text()
        print(pdf_text)
        return pdf_text


    except Exception as e:
        print(e)
        print('WARNING NO PDF')
        return None


def clean_text(pdf_txt):
    cleaned_txt = ' '.join(pdf_txt.split())

    try:
        cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_txt)
    except Exception as e:
        print(e)

    return cleaned_txt



def compile_infos(pdf_txt, df, text_id, pdf, tag):
    row = pd.DataFrame({'category_id':'alternative_science',
                        'text_id':text_id,
                        'tags': tag,
                        'venue':'',
                        'data_source':'sage_journalevidencebasedintegrativemedicine',
                        'url': pdf,
                        'text':pdf_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df


def main():
    # initiate df with information columns
    df = pd.DataFrame(columns=['category-id', 'text_id', 'tags', 'venue', 'data-source', 'url', 'text'])

    '''
    # read csv with URLS
    urls_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/alternative_sagejournalofevidencebasedintegrativemedicine_urls-2.csv').reset_index()

    # loop through each document-url
    for index, row in urls_df.iterrows():
        i += 1

        url = row[2]
        print(url)
        text_id = url.split('pdf/')[1].split('?')[0]
        tag = row[1]

        # download pdf in dummy
        #path = download_pdf(url)
     '''
    pdfs = glob.glob('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/raw_content/JBIM-2/vergessen/*')
    for pdf in pdfs:
        tag = ''
        text_id = pdf.split('JBIM-2/')[1]
        pdf_txt = pdf_to_text(pdf)
        print(pdf_txt)
        cleaned_txt = clean_text(pdf_txt)

        df = compile_infos(cleaned_txt, df, text_id, pdf, tag)


    df.to_csv('data/data-set-topic-wise_2024/content/alternative_sagejournalofevidencebasedintegrativemeicine_text-3.csv ', mode ='a', index=False, header=False)
    print('done')



if __name__ == '__main__':
    main()
