#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "tsne"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "



from yellowbrick.text import TSNEVisualizer
import pandas as pd
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data

corpus_df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_2024-06-13.csv', delimiter=",")
corpus_df.dropna(inplace=True)
print('len complete corpus', len(corpus_df))


X = pickle.load(open('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/2024-06-18_gensim_embedding_.p', 'rb'))


# transform document vectors
X_embedded = TSNE(n_components=2, perplexity=100, learning_rate=3000).fit_transform(X)

print('X_embedded.shape', X_embedded.shape)
y = corpus_df['category_id'].to_list()
print(len(y))
sns.color_palette("mako", as_cmap=True)

sns.relplot(x = X_embedded[:,0], y= X_embedded[:,1], hue=y, style=y, palette='mako')


#plt.show()
plt.savefig('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/2024-06-18_tsne-representation_doc2vec_gensim')