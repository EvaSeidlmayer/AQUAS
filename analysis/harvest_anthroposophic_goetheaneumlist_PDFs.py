#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("retrieve text from URLs ")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pdftotext
import requests
import pandas as pd
import re
from csv import writer



def download_pdf(url, i):
    # Get response object for link
    response = requests.get(url)

    # Write content in pdf file dummy
    path = "data/dummy_anthtopo-PDF.pdf"
    pdf = open(path, 'wb')
    pdf.write(response.content)
    pdf.close()

    return path


def pdf_to_text(path):
    # load pdf
    print('convert pdf to txt')
    try:
        with open(path, 'rb') as f:
            pdf = pdftotext.PDF(f)
            pdf_txt = "\n\n".join(pdf)
        return pdf_txt

    except pdftotext.Error:
        print('WARNING NO PDF')
        return None


def clean_text(pdf_txt):
    cleaned_txt = ' '.join(pdf_txt.split())
    cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_txt)

    return cleaned_txt



def compile_infos(pdf_txt, df, text_id, url, i):
    row = pd.DataFrame({'category_id':'alternative_science',
                        'text_id':text_id,
                        'venue':'',
                        'data_source':'PAAM/Goetheaneum-list',
                        'url': url,
                        'tags':'',
                        'text':pdf_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df


def main():

    # read csv with URLS
    urls_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/antroposophic-medicine_urls.csv', skiprows=3).reset_index()
    print(urls_df.head())

    # initiate index
    i = 0

    #initiate df with information columns
    df = pd.DataFrame(columns=['category-id','text_id','venue','data-source','url','tags','text'])

    # loop through each document-url
    for index, row in urls_df.iterrows():
        i += 1
        print("Processing file:", i, 'DOI', row['doi'])

        # download pdf in dummy
        url = row['url']
        path = download_pdf(url, i)

        # parse pdf to string
        pdf_txt = pdf_to_text(path)

        if pdf_txt is None:
            continue

        # preprocess string
        cleaned_txt = clean_text(pdf_txt)

        # get doi
        text_id = row['doi']

        # compile information  df
        df = compile_infos(cleaned_txt, df, text_id, url, i)

    #print(df)
    df.to_csv('data/alternative_PAAM-goetheaneum-PDF-2023-10-07.csv', mode ='a', index=False, header=False)
    print('done')



if __name__ == '__main__':
    main()
