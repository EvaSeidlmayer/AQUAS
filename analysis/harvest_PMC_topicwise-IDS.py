#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest PMID via Entrez-API from MEDLINE data directory"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "



import requests
import argparse


def get_PMID(file, mesh):
    print('111')
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term={mesh}[MeSH%20Terms]+AND+medline[sb]&retmode=json&retmax=1000"
    response = requests.get(url)
    data = response.json()

    # Extract PMIDs
    count = data["esearchresult"]['count']
    print(count)
    runs = int(count)/1000
    runs += 1
    print(runs)

    for i in range(int(runs)):
        item_numer_start = 1000*i+1
        print(item_numer_start)

        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term={mesh}[MeSH%20Terms]+AND+medline[sb]&retmode=json&retmax=1000&retstart={item_numer_start}"
        response = requests.get(url)
        data = response.json()

        # Extract PMIDs
        pmids = data["esearchresult"]["idlist"]
    
        # Save PMIDs to a text file
        for pmid in pmids:
            file.write(pmid + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mesh_term')
    args = parser.parse_args()
    mesh = args.mesh_term
    print(mesh)

    with open(f"data/data-set-topic-wise_2024/content/raw_content/pmids_{mesh}.txt", "w") as file:
        get_PMID(file, mesh)
    print('done')


if __name__ == '__main__':
    main()
