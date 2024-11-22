#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("calculate statistics on data corpus")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
import textstat


df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-10-21_LSoLF-24-v4.csv')
all_text = df['text'].dropna()


#print(df.head())

#########################################################################################################
############################ calculate flesch's score of readabilty #####################################
# Flesch, R. F. (1979). How to write plain English: A book for lawyers and consumers. Harpercollins #####
#########################################################################################################



'''
#scientific_df = df.loc[df['category_id'] == 'scientific']
#science_text = scientific_df['text'].dropna()
all_value = 0
number = 0

for i, text in all_text.items():
    i += 1
    if isinstance(text, str):
        value = textstat.flesch_reading_ease(text)
        all_value += value
        number += 1
    else:
        ...

print('Flesch s reading score for all texts:', all_value/i)

science_df = df.loc[df['category_id'] == 'scientific']
sc_txt = science_df['text'].dropna()
sc_txt_value = 0
number = 0
text_length = 0
for i, text in sc_txt.items():
    i += 1
    value = textstat.flesch_reading_ease(text)
    text = text.split()
    length = len(text)
    text_length += length
    sc_txt_value += value
    number += 1
    #print('1. length', length)
average_length = text_length/number
print('number of sci items', number, 'number of words', text_length)
print('1. Flesch reading score for scientific texts:', sc_txt_value/i)
print('1. sci text  length:', average_length)


text_length = 0
pop_df = df.loc[df['category_id'] == 'popular']
pop_text = pop_df['text'].dropna()
pop_value = 0
number  = 0
for i, text in pop_text.items():
    value = textstat.flesch_reading_ease(text)
    pop_value += value
    number +=1
    text = text.split()
    length = len(text)
    text_length += length
average_length = text_length / number
print('number of pop items', number, 'number of words', text_length)
print('2. Flesch reading score for pop texts:', pop_value/i)
print('2. pop text  length:', average_length)
'''




alternative_science_df = df.loc[df['category_id'] == 'alternative_science']
alt_txt = alternative_science_df['text'].dropna()
alt_txt_value = 0
number = 0
text_length = 0
for i, text in alt_txt.items():
    value = textstat.flesch_reading_ease(text)
    alt_txt_value += value
    number += 1
    text = text.split()
    length = len(text)
    text_length += length
    if length > 11000:
        print(length, text[0:100])
print('3. Flesch reading score for alt texts:', alt_txt_value/i)
average_length = text_length/number
print('number of alt items', number, 'number of words', text_length)
print('3. alt text  length:', average_length)


'''
disinfo_df = df.loc[df['category_id'] == 'disinfo']
disinfo_txt = disinfo_df['text'].dropna()
disinfo_value = 0
text_length = 0
number = 0
for i, text in disinfo_txt.items():
    value = textstat.flesch_reading_ease(text)
    disinfo_value += value
    number += 1
    text = text.split()
    length = len(text)
    text_length += length
print('4. Flesch reading score for disino texts:', disinfo_value/i)
average_length = text_length/number
print('number of disinfo items', number, 'number of words', text_length)
print('4. disinfo text  length:', average_length)

'''

