#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "doc2vec embedding corpus data"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "




import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import pickle
import gensim
import pandas as pd

# Set file names for train and test data
df = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-13_fewshot_testing.csv')

scientific_df = df.loc[df['category_id'] == 'scientific']
pop_df = df.loc[df['category_id'] == 'popular_science']
disinfo_df = df.loc[df['category_id'] == 'disinfo']
alternative_science_df = df.loc[df['category_id'] == 'alternative_science']

print('len corpus dataframe', len(df))

text = df['text'].tolist()
test_file = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-13_fewshot_testing.csv')
test_file = df['text'].tolist()



def read_corpus(text, tokens_only=False):
    for i, line in enumerate(text):
        tokens = gensim.utils.simple_preprocess(line)
        if tokens_only:
            yield tokens
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

train_corpus = list(read_corpus(text))
test_corpus = list(read_corpus(test_file, tokens_only=True))


print(train_corpus[:2])

model = gensim.models.doc2vec.Doc2Vec(vector_size=60, min_count=2, epochs=400)
model = gensim.models.doc2vec.Doc2Vec(vector_size=60, min_count=2, epochs=5)

# Build a vocabulary
model.build_vocab(train_corpus)

model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

# train model and create corpus representation
vecs = []
ranks = []
second_ranks = []
for doc_id in range(len(train_corpus)):
    inferred_vector = model.infer_vector(train_corpus[doc_id].words)
    vecs.append(inferred_vector)
corpus_matrix_MEDLINE1 = pd.DataFrame(vecs)
print(type(corpus_matrix_MEDLINE1))
pickle.dump(corpus_matrix_MEDLINE1, open('data/2023-10-18_gensim_embedding_.p', 'wb'))
print('matrix created and dumped')
