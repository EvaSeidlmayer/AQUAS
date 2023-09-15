#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("get data from https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/ oline archive which contains PDF of Open "
                   "access articles indexed in Pub Med Central")
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
import csv
from time import sleep


def aggrgate_all_links(base_url):
    # construct all possible combinations in archive
    complete_links = []

    range = ['00/', '01/', '02/', '03/', '04/', '05/', '06/', '07/', '08/', '09/', 'a0/', 'b0/', 'c0/', 'd0/', 'e0/', 'f0/',
             '10/', '11/', '12/', '13/', '14/', '15/', '16/', '17/', '18/', '19/', 'a1/', 'b1/', 'c1/', 'd1/', 'e1/', 'f1/',
             '20/', '21/', '22/', '23/', '24/', '25/', '26/', '27/', '28/', '29/', 'a2/', 'b2/', 'c2/', 'd2/', 'e2/', 'f2/',
             '30/', '31/', '32/', '33/', '34/', '35/', '36/', '37/', '38/', '39/', 'a3/', 'b3/', 'c3/', 'd3/', 'e3/', 'f3/',
             '40/', '41/', '42/', '43/', '44/', '45/', '46/', '47/', '48/', '49/', 'a4/', 'b4/', 'c4/', 'd4/', 'e4/', 'f4/',
             '50/', '51/', '52/', '53/', '54/', '55/', '56/', '57/', '58/', '59/', 'a5/', 'b5/', 'c5/', 'd5/', 'e5/', 'f5/',
             '60/', '61/', '62/', '63/', '64/', '65/', '66/', '67/', '68/', '69/', 'a6/', 'b6/', 'c6/', 'd6/', 'e6/', 'f6/',
             '70/', '71/', '72/', '73/', '74/', '75/', '76/', '77/', '78/', '79/', 'a7/', 'b7/', 'c7/', 'd7/', 'e7/', 'f7/',
             '80/', '81/', '82/', '83/', '84/', '85/', '86/', '87/', '88/', '89/', 'a8/', 'b8/', 'c8/', 'd8/', 'e8/', 'f8/',
             '90/', '91/', '92/', '93/', '94/', '95/', '96/', '97/', '98/', '99/', 'a9/', 'b9/', 'c9/', 'd9/', 'e9/', 'f9/',
             'aa/', 'ba/', 'ca/', 'da/', 'ea/', 'fa/', 'ab/', 'bb/', 'cb/', 'db/', 'eb/', 'fb/','ac/', 'bc/', 'cc/', 'dc/',
             'ec/', 'fc/', 'ad/', 'bd/', 'cd/', 'dd/', 'ed/', 'fd/', 'ae/', 'be/', 'ce/', 'de/', 'ee/', 'fe/','af/', 'bf/',
             'cf/', 'df/', 'ef/', 'ff/']

    for ending_1 in range:
        for ending_2 in range:
            url =base_url + ending_1 + ending_2
            complete_links = get_urls(url, complete_links)
            print('Current number of aggregated links:', len(complete_links))
    print('Number of all links:',len(complete_links))

    with open('data/science_PMC_complete_url_list_2023-09-15.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(complete_links)
    return complete_links


def get_urls(url, complete_links):
    # Requests URL and get response object
    response = requests.get(url)

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')


    for link in links:
        if '.pdf' in str(link):
            complete_link = url + str(link).split('</a>', -1)[0].split('>', -1)[1]
            complete_links.append(complete_link)

    return complete_links

def download_pdf(complete_link, i):
        # Get response object for link
        response = requests.get(complete_link)

        # Write content in pdf file dummy
        path = "data/dummy_science_PMC-PDF.pdf"
        pdf = open(path, 'wb')
        pdf.write(response.content)
        pdf.close()

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

def identify_text_id(complete_link):
    """
    https//doi.org/10.* refers to referenced papers not to DOI of the original paper
    """
    if "PMC" in complete_link:
        pattern__ = 'PMC[^.]+'
        try:
            pmc = re.search(pattern__, complete_link).group(0)
            text_id = pmc
        except:
            text_id = ''

    else:
        text_id = ''

    return text_id


def compile_infos(pdf_txt, df, text_id, complete_link, i):
    row = pd.DataFrame({'category_id':'scientific',
                        'text_id':text_id,
                        'venue':'',
                        'data_source':'PMC',
                        'url':complete_link,
                        'tags':'',
                        'title':'',
                        'text':pdf_txt}, index=[0])
    df = pd.concat([df, row], ignore_index=True)
    return df

def main():

    # arcive url
    base_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/'

    # initiate index
    i = 0


    #initiate df with information columns
    df = pd.DataFrame(columns=['category-id','text-id','venue','data-source','url','tags','title', 'text'])

    # compile all possible urls in archive
    complete_links = aggrgate_all_links(base_url)

    # loop through each document-url
    for complete_link in complete_links:
        i += 1
        print("From complete number", len(complete_links), "Processing file:", i)

        # download pdf in dummy
        path = download_pdf(complete_link, i)

        # parse pdf to string
        pdf_txt = pdf_to_text(path)

        # preprocess string
        cleaned_txt = clean_text(pdf_txt)

        # seach for doi, PMC-id
        text_id = identify_text_id(complete_link)

        # compile information  df
        df = compile_infos(cleaned_txt, df, text_id, complete_link, i)
    sleep(2)

    #print(df)
    df.to_csv('data/scientific_PMC-PDF-2023-09-15_00.csv', mode ='a', index=False, header=False)
    print('done')



if __name__ == '__main__':
    main()
