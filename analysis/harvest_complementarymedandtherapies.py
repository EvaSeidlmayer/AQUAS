#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("retrieve text from PDF-URLs "
                   "## BMC Complementary Medicine and Therapies")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import requests
import pandas as pd
import re
from pypdf import PdfReader



def download_pdf(url, i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}

    # Get response object for link
    response = requests.get(url, headers=headers)


    # Write content in pdf file dummy
    path = "data/2024-04-11_dummy_anthropo-PDF.pdf"
    pdf = open(path, 'wb')
    pdf.write(response.content)
    pdf.close()

    return path


def pdf_to_text(path):
    # load pdf
    print('convert pdf to txt')
    try:
        reader = PdfReader(path, strict=False)

        page = reader.pages[0]
        pdf_text = page.extract_text()
        return pdf_text


    except Exception as e:
        print(e)
        print('WARNING NO PDF')
        return None


def clean_text(pdf_txt):
    cleaned_txt = ' '.join(pdf_txt.split())
    cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_txt)

    return cleaned_txt



def compile_infos(pdf_txt, df, text_id, url, i, tag):
    row = pd.DataFrame({'category_id':'alternative_science',
                        'text_id':text_id,
                        'venue':'',
                        'data_source':'CompMedTherapies',
                        'url': url,
                        'tags':tag,
                        'text':pdf_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df


def main():

    # read csv with URLS
    urls_df = pd.read_csv(
        '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/alternative_complementarymedandtherapies_urls.csv').reset_index()
    i = 0

    #initiate df with information columns
    df = pd.DataFrame(columns=['category-id','text_id','venue','data-source','url','tags','text'])

    # loop through each document-url
    for index, row in urls_df.iterrows():
        i += 1
        url = row['url']
        text_id = url.split('pdf/')[1].split('?')[0]
        tag = row['topic']

        # download pdf in dummy
        path = download_pdf(url, i)
        # parse pdf to string
        pdf_txt = pdf_to_text(path)

        if pdf_txt is None:
            continue
        # preprocess string
        cleaned_txt = clean_text(pdf_txt)



        # compile information  df
        df = compile_infos(cleaned_txt, df, text_id, url, i, tag)

    #print(df)
    df.to_csv('data/data-set-topic-wise_2024/content/alternative_CompMedTherapies_texts.csv', mode ='a', index=False, header=False)
    print('done')



if __name__ == '__main__':
    main()
