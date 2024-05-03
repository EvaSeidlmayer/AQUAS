#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = " harvest Industry documents of University of California database (https://www.industrydocuments.ucsf.edu/) via SolR "
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import requests
import argparse
import csv
from pandas import read_csv
import pysolr
import json



import requests


def get_tempfile(url, output_file):
    response = requests.get(url)
    with open(output_file, 'wb') as f:
        f.write(response.content)





def read_infos(output_file):
    with open(output_file) as f:
        d = json.load(f)
        next_cursormark = d['nextCursorMark']
        number = d['response']['numFound']
        #print(number)

        #print(next_cursormark)

        return next_cursormark


#industrydoc = json.loads(output_file)
#print(industrydoc)
#json_data = industrydoc.read()
#print(json_data['nextCursorMark'])


def main():
    cursormark = '*'
    i = 1
    url =   f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"scientific article"&wt=json&cursorMark={cursormark}&sort=id%20desc'
    url_5 = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"Science"&wt=json&cursorMark={cursormark}&sort=id%20desc'
    url_4 = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"report, scientific"&wt=json&cursorMark={cursormark}&sort=id%20desc'
    url_3 = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"scientific article"&wt=json&cursorMark={cursormark}&sort=id%20desc'
    url_2 = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=(type:"scientific article" AND type:"report, scientific")&wt=json&cursorMark={cursormark}&sort=id%20desc'
    url_1 = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=tobacco&wt=json&cursorMark={cursormark}&sort=id%20desc'
    output_file = f'data/2024_tobacco_industry_documents/2023-12-07_industrydocuments_{i}.json'


    for i in range(600):
        get_tempfile(url, output_file)
        next_cursormark = read_infos(output_file)
        i +=1
        cursormark = next_cursormark

        url = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"scientific article"&wt=json&cursorMark={cursormark}&sort=id%20desc'
        #url = f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=tobacco&wt=json&cursorMark={cursormark}&sort=id%20desc'
        #url= f'https://metadata.idl.ucsf.edu/solr/ltdl3/query?q=type:"science"&wt=json&cursorMark={cursormark}&sort=id%20desc'

        new_output_file = f'data/2024_tobacco_industry_documents/2024-01-11_tobacco_type_scientificarticle_{i}.json'
        output_file = new_output_file
        print(output_file)


if __name__ == '__main__':
    main()
