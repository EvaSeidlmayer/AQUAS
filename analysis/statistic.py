#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = ("calculate statistics on data corpus")
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
from nltk.corpus import inaugural
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
import textstat
import sys


df = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-13_fewshot_testing.csv')
all_text = df['text']
#print(df.head())

#########################################################################################################
############################ calculate flesch's score of readabilty #####################################
# Flesch, R. F. (1979). How to write plain English: A book for lawyers and consumers. Harpercollins #####
#########################################################################################################
'''
scientific_df = df.loc[df['category_id'] == 'scientific']
science_text = scientific_df['text']
science_value = 0
number = 0
for i, text in all_text.items():
    value = textstat.flesch_reading_ease(text)
    science_value += value
    number += 1
print('Flesch s reading score for all texts:', science_value/i)
sys.exit()
#science_text = ''.join(science_text_list)


pop_df = df.loc[df['category_id'] == 'popular_science']
pop_text = pop_df['text']
pop_value = 0
number  = 0
for i, text in pop_text.items():
    value = textstat.flesch_reading_ease(text)
    pop_value += value
    number +=1

print('Flesch reading score for pop texts:', pop_value/i)



disinfo_df = df.loc[df['category_id'] == 'disinfo']
disinfo_txt = disinfo_df['text']
disinfo_value = 0
number = 0
for i, text in disinfo_txt.items():
    value = textstat.flesch_reading_ease(text)
    disinfo_value += value
    number += 1
print('Flesch reading score for disino texts:', disinfo_value/i)

alternative_science_df = df.loc[df['category_id'] == 'alternative_science']
alt_txt = alternative_science_df['text']
alt_txt_value = 0
number = 0
for i, text in alt_txt.items():
    value = textstat.flesch_reading_ease(text)
    alt_txt_value += value
    number += 1
print('Flesch reading score for alt texts:', alt_txt_value/i)
'''
'''
alternative_science_df = df.loc[df['category_id'] == 'alternative_science']
alt_txt = alternative_science_df['text']
alt_txt_list = []
for i, text in alt_txt.items():
    alt_txt_list.append(text)
alt_science_text = ''.join(alt_txt_list)


print('Flesch reading score for scientific texts:', textstat.flesch_reading_ease(science_text))
print('Flesch reading score for pop texts:', textstat.flesch_reading_ease(pop_text))
print('Flesch reading score for disinfo texts:', textstat.flesch_reading_ease(disinfo_text))
print('Flesch reading score for alt science texts:', textstat.flesch_reading_ease(alt_science_text))
'''


'''
#remove stoppwords
token_list = []
print('oooooo',type(science_text))
for token in science_text:
    token_list.append(token)
filtered_sentence = []
for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word)
print(len(filtered_sentence))
print(len(token_list))
'''

nlp = English()  # or spacy.load('a_model')
nlp.add_pipe("simple_corpus_stats")


#######################
#### science_texts ####
#######################
print('statistic disinfo texts')

for doc in nlp.pipe(all_text):
    # ➡️ do your pipeline stuff! ➡️
    pass

corpus_stats = nlp.get_pipe("simple_corpus_stats")

# check if a token has been processed through this pipeline
token = "apple"
if token in corpus_stats:
    token_count = corpus_stats[token]
    print(f"'{token}' mentioned {token_count} times")

only_seen_once = len(corpus_stats.hapax_legomena)
percent_of_vocab = only_seen_once / corpus_stats.vocab_size
print(f"{percent_of_vocab*100:.1f}% tokens only occurred once.")

only_seen_twice = len(corpus_stats.dis_legomena)
percent_of_vocab_2x = only_seen_twice / corpus_stats.vocab_size
print(f"{percent_of_vocab_2x*100:.1f}% tokens occurred twice.")

# corpus_stats.vocabulary is a collections.Counter 🔢
print(*corpus_stats.vocabulary.most_common(5), sep="\n")

mean_doc_length = sum(corpus_stats.doc_lengths) / corpus_stats.corpus_length
print(f"Mean doc length: {mean_doc_length:.1f}")
