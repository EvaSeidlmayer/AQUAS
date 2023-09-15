#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("enrich PMC data produced by harvest_PMC_PDFs.py with doi by NCBI ID Converter https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/idconv.fcgi "
                   "and article-title, venue, tags by Crossref")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
import subprocess
import jsonlines


# curl is needed for the subprocess:
def get_doi_by_pmcid(pmcid):
        subprocess.run(f"curl https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={pmcid}&format=csv --output tmp.csv".split())

        content =  pd.read_csv('./tmp.csv')
        doi = content.iloc[0]['DOI']

        return doi

def get_infos_from_crossref(doi):
    subprocess.run(f"curl https://api.crossref.org/works/{doi} --output tmp.json".split())
    try:
        with jsonlines.open('./tmp.json') as reader:
            for obj in reader:

                # harvest publication title and ISSN from Crossref
                for titel in obj['message']['title']:
                    title = titel
                try:
                    for issn in obj['message']['ISSN']:
                        venue = 'ISSN:' + str(issn)
                except:
                    venue = ''

                try:
                    for subject in obj['message']['subject']:
                        tags = subject
                except:
                    tags = ''
                return title, venue, tags
    except jsonlines.jsonlines.InvalidLineError:
        print('WARNING NO Crossref file')
        return None


df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/scientific_PMC-PDF-2023-09-04_00.csv')

for index, row in df.iterrows():
    pmcid = row['text_id']

    doi = get_doi_by_pmcid(pmcid)
    title, venue, tags = get_infos_from_crossref(doi)
    if None in (title, venue, tags):
        continue

    df.loc[df.index == index, 'text_id'] = doi
    df.loc[df.index == index, 'title'] = title
    df.loc[df.index == index, 'venue'] = venue
    df.loc[df.index == index, 'tags'] = tags

df.to_csv('data/scientific_PMC-PDF-enrichted_2023-09-15.csv', index=None, header=None )


