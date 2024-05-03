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

corpus_df = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-13_fewshot_testing.csv', delimiter=",")
print('len complete corpus', len(corpus_df))


X = pickle.load(open('/AQUS/AQUAS/data/data-set_2023/2023-10-18_gensim_embedding_.p', 'rb'))


# transform document vectors
X_embedded = TSNE(n_components=2, perplexity=100, learning_rate=3000).fit_transform(X)

print(X_embedded.shape)
y = corpus_df['category_id'].to_list()

sns.color_palette("mako", as_cmap=True)

sns.relplot(x = X_embedded[:,0], y= X_embedded[:,1], hue=y, style=y, palette='mako')


#plt.show()
plt.savefig('data/2023-10-19_tsne-representation_doc2vec_gensim')