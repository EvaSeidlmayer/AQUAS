#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "parse bulk download of PLOS One from https://plos.org/text-and-data-mining/"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import glob
import zipfile

'''
def get_doi_text(tree):
    try:
        doi = tree.find('.//article-id[@pub-id-type="doi"]')
        tex = tree.findall('.//sec/p')
        txt = ''
        for elem in tex:
            txt += elem.text.strip()
        row = pd.DataFrame({'category-id': 1,'text-id':[doi.text],'text':[txt]})
        return row
    except Exception as e:
        print('Exception', e)
'''

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('xml_folder_path')
    args = parser.parse_args()
    xml_files = glob.glob(args.xml_folder_path + '/*.xml')
    #df_list = (pd.read_xml(file, xpath='//body') for file in xml_files)
    for file in xml_files:
        xmlfile = pd.read_xml(file, xpath='//sec')
        print(xmlfile)


    '''
    df = pd.DataFrame(columns=['category-id', 'text-id','text'])
    with tarfile.open(args.tarfile) as tf:
        for member in tf:
            xf = tf.extractfile(member)
            tree = ET.parse(xf)
            data = get_doi_text(tree)
            try:
                df = pd.concat([df, data], ignore_index=True)
            except Exception as e:
                print(e)
    df[df['text'].str.strip().astype(bool)]
    df.replace('', np.nan, inplace=True)
    df.dropna(inplace=True)
    df.to_csv('data/PMC-doi_text-2023-02-28.csv', index=False)
    print('done')
    '''

if __name__ == '__main__':
    main()
