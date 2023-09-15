#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = (".")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pdftotext
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_urls(url):
    # Requests URL and get response object

    response = requests.get(url)
    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')

    complete_links = []
    for link in links:
        if 'cgi/viewcontent' in str(link):

            #get urls
            complete_link = str(link).split('href="', -1)[1].split('" target=')[0]
            complete_links.append(complete_link)
    return complete_links

def download_pdf(complete_link, i):
    # Get response object for link
    response = requests.get(complete_link)

    # Write content in pdf file
    path = "data/PDF_dummy.pdf"
    pdf = open(path, 'wb')
    pdf.write(response.content)
    pdf.close()
    print("File ", i, " downloaded")
    return path


def pdf_to_text(path):
    # load pdf
    print('convert pdf to txt')
    with open(path, 'rb') as f:
        pdf = pdftotext.PDF(f)
        pdf_txt = "\n\n".join(pdf)
    return pdf_txt

def clean_text(pdf_txt):
    cleaned_txt = ' '.join(pdf_txt.split())
    return cleaned_txt

def identify_doi(cleaned_txt):
    pattern = 'doi: [^ ]+'
    doi = re.search(pattern, cleaned_txt).group(0).split('doi: ', -1)[1]
    if re.search('/$', doi):
        pattern_ = 'doi: [^ ]+[ ][^ ]+'
        doi_2 = re.search(pattern_, cleaned_txt).group(0).split('doi: ',-1)[1]
        doi=doi_2.replace(' ', '')
    return doi


def compile_infos(cleaned_txt, df, doi, complete_link, i):
    print('this is dokument #', i)

    row = pd.DataFrame({'category-id':'scientific',
                        'text-id':doi,
                        'venue':'Indian-research-Homeopathy',
                        'data-source':'Indian-research-Homeopathy',
                        'url':complete_link,
                        'tags':'',
                        'text':cleaned_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df





def main():
    url = 'https://www.ijrh.org/journal/'
    df = pd.DataFrame(columns=['category-id','text-id','venue','data-source','url','tags','text'])


    complete_links = get_urls(url)
    i = 0
    # if present download file
    for complete_link in complete_links:

        i += 1
        print("Downloading file: ", i)
        path = download_pdf(complete_link, i)
        pdf_txt = pdf_to_text(path)
        cleaned_txt = clean_text(pdf_txt)
        doi = identify_doi(cleaned_txt)
        df = compile_infos(cleaned_txt, df, doi, complete_link, i)
    #print(pdf_txt)
    #print(df)
    print("All PDF files downloaded")
    df.to_csv('data/homeopathy_Indian-research-Homeopathy_PDF-2023-08-25.csv', index=False)
    print('done')



if __name__ == '__main__':
    main()
