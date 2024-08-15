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
import urllib
import glob
import PyPDF2



def download_pdf(url):
    path = "data/2024-07-08_dummy_anthropo-PDF.pdf"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5'}
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
            return path
    else:
        print(f"Failed to download PDF. HTTP Status Code: {response.status_code}")




def get_page_number(path):
    print('check number of pages')
    file = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(file)
    page_number = len(pdfReader.pages)
    print(page_number)
    return page_number


def pdf_to_text(pdf, page_number):
    # load pdf
    print('convert pdf to txt')
    try:
        with open(pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            pdf_text = ''

            for page_num in range(page_number):
                page = reader.pages[page_num]
                pdf_text += page.extract_text() + '\n'


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



def compile_infos(pdf_txt, df, text_id, url, tag):
    row = pd.DataFrame({'category_id':'alternative_science',
                        'text_id':text_id,
                        'tags': tag,
                        'venue':'',
                        'data-source':'JEBIM',
                        'url': url,
                        'text':pdf_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df


def main():
    # initiate df with information columns
    df = pd.DataFrame(columns=['category_id', 'text_id', 'tags', 'venue', 'data-source', 'url', 'text'])
    '''
    pdfs = glob.glob('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/raw_content/JEBIM/*')
    for pdf in pdfs:
        tag = ''
        text_id = pdf.split('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/raw_content/JEBIM/')[1]
        '''

    input_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/urls/alternative_sagejornalofevidencebasedintegrativemedicne_urls_all.csv')

    for index, infos in input_df.iterrows():

        tag = infos[0]
        url = infos[1]
        text_id = url.split('https://journals.sagepub.com/doi/pdf/')[1].split('?download=true')[0]
        print('text_id', text_id)
        print('tag', tag)
        print('url', url)

        path = download_pdf(url)
    # get number of pages of pdf
        page_number = get_page_number(path)
        print(page_number)

        pdf_txt = pdf_to_text(path, page_number)


        cleaned_txt = clean_text(pdf_txt)

        df = compile_infos(cleaned_txt, df, text_id, url, tag)


    df.to_csv('data/data-set-topic-wise_2024/content/raw_content/FSoLS-24-v2/alternative_sagejournalofevidencebasedintegrativemedicine_all_text_2024-07-08.csv', mode ='a', index=False, header=False)
    print('done')



if __name__ == '__main__':
    main()
