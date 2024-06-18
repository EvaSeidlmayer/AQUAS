#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = (
    "get data from https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/ oline archive which contains PDF of Open "
    "access articles indexed in Pub Med Central"
)
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




def get_urls(url, complete_links):
    # Requests URL and get response object
    response = requests.get(url)

    # Parse text obtained
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all hyperlinks present on webpage
    links = soup.find_all("a")

    for link in links:
        if ".pdf" in str(link):
            complete_link = url + str(link).split("</a>", -1)[0].split(">", -1)[1]
            complete_links.append(complete_link)

    return complete_links


def download_pdf(url, i):
    # Get response object for link
    response = requests.get(url)

    # Write content in pdf file dummy
    path = "dummy_PDF.pdf"
    pdf = open(path, "wb")
    pdf.write(response.content)
    pdf.close()

    return path


def pdf_to_text(path):
    # load pdf
    #print("convert pdf to txt")
    try:
        with open(path, "rb") as f:
            pdf = pdftotext.PDF(f)
            pdf_txt = "\n\n".join(pdf)
        return pdf_txt
    except pdftotext.Error:
        print('WARNING NO PDF')
        return None


def clean_text(pdf_txt):
    cleaned_txt = " ".join(pdf_txt.split())
    cleaned_txt = re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_txt)
    return cleaned_txt


def identify_text_id(complete_link):

    if "https://www.homoeopathicjournal.com/articles/" in complete_link:

        try:
            text_id = complete_link.split('https://www.homoeopathicjournal.com/articles/')[1]

        except:
            text_id = ""

    else:
        text_id = ""

    return text_id


def compile_infos(pdf_txt, df_all, text_id, complete_link, i):
    row = pd.DataFrame(
        {
            "category_id": "alternative_science",
            "text_id": text_id,
            "tags": "",
            "venue": "",
            "data-source": "homeopathicjournal",
            "url": complete_link,

            "title": "",
            "text": pdf_txt,
        },
        index=[0],
    )

    df_all= pd.concat([df_all, row], ignore_index=True)
    return df_all



def main():

    # initiate index
    i = 0

    # initiate df with information columns
    df_all = pd.DataFrame(
        columns=[
            "category_id",
            "text_id",
            "tags",
            "venue",
            "data_source",
            "url",
            "title",
            "text",
        ]
    )


    # loop through each document-url
    with open("/AQUS/AQUAS/data/alternative/alternative_homeopathicjournal_complete_urls.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        for links in reader_obj:
            i += 1
            print("Processing file:", i)
            link = ''.join(links)
            if ".pdf" in link:
                print(link)

                # download pdf in dummy
                path = download_pdf(link, i)

                # parse pdf to string
                pdf_txt = pdf_to_text(path)


                # preprocess string
                cleaned_txt = clean_text(pdf_txt)

                # seach for doi, PMC-id
                text_id = identify_text_id(link)


                # compile information  df
                df_all = compile_infos(cleaned_txt, df_all, text_id, link, i)

                df_all.to_csv(
                    "alternative_homeopathicjournal_PDFs.csv",
                    mode="w",
                    index=False,
                    header=True,
                )


        print("done")



if __name__ == "__main__":
    main()
