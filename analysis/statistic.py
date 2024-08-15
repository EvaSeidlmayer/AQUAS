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


df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-08-06_LSoLF-24-v2.csv')
all_text = df['text'].dropna()


#print(df.head())

#########################################################################################################
############################ calculate flesch's score of readabilty #####################################
# Flesch, R. F. (1979). How to write plain English: A book for lawyers and consumers. Harpercollins #####
#########################################################################################################

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
for i, text in sc_txt.items():
    i += 1
    value = textstat.flesch_reading_ease(text)
    sc_txt_value += value
    number += 1
print('1. Flesch reading score for scientific texts:', sc_txt_value/i)


pop_df = df.loc[df['category_id'] == 'popular']
pop_text = pop_df['text'].dropna()
pop_value = 0
number  = 0
for i, text in pop_text.items():
    value = textstat.flesch_reading_ease(text)
    pop_value += value
    number +=1

print('2. Flesch reading score for pop texts:', pop_value/i)



disinfo_df = df.loc[df['category_id'] == 'disinfo']
disinfo_txt = disinfo_df['text'].dropna()
disinfo_value = 0
number = 0
for i, text in disinfo_txt.items():
    value = textstat.flesch_reading_ease(text)
    disinfo_value += value
    number += 1
print('3. Flesch reading score for disino texts:', disinfo_value/i)

alternative_science_df = df.loc[df['category_id'] == 'alternative_science']
alt_txt = alternative_science_df['text'].dropna()
alt_txt_value = 0
number = 0
for i, text in alt_txt.items():
    value = textstat.flesch_reading_ease(text)
    alt_txt_value += value
    number += 1
print('4. Flesch reading score for alt texts:', alt_txt_value/i)


''''
alternative_science_df = df.loc[df['category_id'] == 'alternative_science']
alt_txt = alternative_science_df['text']
alt_txt_list = []
for i, text in alt_txt.items():
    alt_txt_list.append(text)
alt_science_text = ''.join(alt_txt_list)

sc_txt = ', '.join(sc_txt.astype(str))
pop_text = ', '.join(pop_text.astype(str))
disinfo_txt = ', '.join(disinfo_txt.astype(str))
alt_txt = ', '.join(alt_txt.astype(str))


print('Flesch reading score for scientific texts:', textstat.flesch_reading_ease(sc_txt))
print('Flesch reading score for pop texts:', textstat.flesch_reading_ease(pop_text))
print('Flesch reading score for disinfo texts:', textstat.flesch_reading_ease(disinfo_txt))
print('Flesch reading score for alt science texts:', textstat.flesch_reading_ease(alt_txt))

'''

'''
#remove stoppwords
token_list = []
#print('oooooo',type(science_text))
for token in sc_txt:
    token_list.append(token)
filtered_sentence = []
for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word)
print(len(filtered_sentence))
print(len(token_list))
'''
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
'''