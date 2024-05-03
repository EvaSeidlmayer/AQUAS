#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("parse bulk download of PMC Open Access Subset [Internet]. Bethesda (MD): National Library of Medicine. "
                   "2003 - [cited 2023 Feb 08]. "
                   "Available from https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/.")
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
import tarfile


def get_doi_text(tree):
    try:
        #get doi
        doi = tree.find('.//article-id[@pub-id-type="doi"]')

        #get article text
        root = tree.getroot()
        txt = ''
        for body in root.findall('.//body/sec/p'):
            tex = body.text
            print(tex)

            for elem in tex:
                txt += elem.text
        # collect all infos together
        row = pd.DataFrame({'category-id':'scientific',
                            'text-id':[doi.text],
                            'text': txt})
        print(txt)
    except Exception as e:
        print('Exception', e)


def main():
    df = pd.DataFrame(columns=['category-id', 'text-id','text'])

    parser = argparse.ArgumentParser()
    parser.add_argument('xml_folder_path')
    args = parser.parse_args()
    #xml_files = glob.glob(args.xml_folder_path + '/*.xml')
    #df_list = (pd.read_xml(file, xpath='//body') for file in xml_files)
    with tarfile.open(args.xml_folder_path) as tf:
        for file in tf:
            xf = tf.extractfile(file)
            tree = ET.parse(xf)
            try:
                #doi = tree.find('.//article-id[@pub-id-type="doi"]').text
                #print(doi)
                #root = tree.getroot()
                #for body in root.findall('.//body/sec/p'):
                 #   print(body.text)


                #tex = tree.findall('.//body[@sec-id="p"]').attrib

                infos = get_doi_text(tree)
                try:
                    df = pd.concat([df, infos], ignore_index=True)
                except Exception as e:
                    print(e)
            except Exception:
                continue
    df.replace('', np.nan, inplace=True)
    df.dropna(inplace=True)
    df.to_csv('data/PMC-doi_text-2024-04-25.csv', index=False)
    print('done')

if __name__ == '__main__':
    main()
