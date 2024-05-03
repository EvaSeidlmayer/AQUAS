#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest Open Citation for passive citations (cited-by). Infos on the API: https://opencitations.net/index/api/v1 "

__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import pandas as pd
import requests
import argparse


def get_doi(pmid):
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        if data:
            try:
                ids = data['result'][f'{pmid}']['articleids']
                try:
                    doi = next((item for item in ids if item.get('idtype') == 'doi'), {}).get('value')
                except Exception as e:
                    print(e)
                print('retrieved DOI:', doi)
                return doi
            except Exception as e:
                print(e)
        else:
            #print(f"No article found for PMID {pmid}")
            return None
    else:
        #print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
def get_citedby(doi, token):
    API_CALL = f"https://opencitations.net/index/api/v1/references/{doi}"
    HTTP_HEADERS = {"authorization": token}

    response = requests.get(API_CALL, headers=HTTP_HEADERS)
    try:
        data = response.json()
        citedby = len(data)
        return citedby
    except Exception as e:
        print(e)
        return None




def main():
    token = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('PMID_file')
    parser.add_argument('mesh')
    args = parser.parse_args()


    pmid_file = open(args.PMID_file, 'r')
    Lines = pmid_file.readlines()
    mesh = args.mesh
    df = pd.DataFrame(columns= ['pmid','doi','citedby'])

    for pmid in Lines:
        pmid = pmid.replace('\n', '')
        doi = get_doi(pmid)
        if doi is not None:
            citedby = get_citedby(doi, token)
            infos = {'pmid': pmid, 'doi' : doi, 'citedby': citedby}
            df = pd.concat([df, pd.DataFrame([infos])], ignore_index=True)
        else:
            print("No DOI detected.")
    print(df.shape)
    number_df = df.shape[0]
    ten_most = number_df/10
    ten_most = round(ten_most)
    print(ten_most)
    df['citedby'] = df['citedby'].astype(str).astype(int)

    #df['citedby'] = pd.to_numeric(df['citedby'], errors='coerce')
    df_ten_most = df.nlargest(ten_most, 'citedby')
    print(df_ten_most)
    df_ten_most.to_csv(f'data/data-set-topic-wise_2024/content/raw_content/df_ten_most_{mesh}.csv', index= False)

    print('done')

if __name__ == '__main__':
    main()
