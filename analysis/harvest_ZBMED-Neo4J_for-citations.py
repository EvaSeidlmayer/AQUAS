#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest Neo4J Data Base, including Open citation and Knowledge Environment for passive citations (cited-by). "

__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "

import requests
import argparse


def get_citedby(line):
    print(line)
    url = f'http://134.95.56.132/app/refs?id=M{line}'
    response = requests.get(url)
    data = response.json()
    tar = data['tar']
    print(tar)

    '''
    # Extract PMIDs
    count = data["esearchresult"]['count']
    print(count)
    runs = int(count) / 1000
    runs += 1
    print(runs)

    pmids = data["esearchresult"]["idlist"]

        # Save PMIDs to a text file
        for pmid in pmids:
            file.write(pmid + "\n")
    '''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('PMID_file')
    args = parser.parse_args()

    pmid_file = open(args.PMID_file, 'r')
    Lines = pmid_file.readlines()
    for line in Lines:
        get_citedby(line)


    print('done')


if __name__ == '__main__':
    main()
