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
'''
df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-08-06_LSoLF-24-v2.csv',usecols=['text', 'category_id'], delimiter=",")
print(len(df))
df.dropna(inplace=True)

df['category_id'] = df['category_id'].replace('scientific', 'scientific texts')
df['category_id'] = df['category_id'].replace('popular', 'popular texts')
df['category_id'] = df['category_id'].replace('disinfo', 'dinformative texts')
df['category_id'] = df['category_id'].replace('alternative_science', 'alternative science texts')



print('len complete corpus', len(df))
print( df.groupby(by=['category_id']).sum())
'''
df = pd.read_csv('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-08-06_LSoLF-24-v2.csv',usecols=['text', 'data-source'], delimiter=",")
df.dropna(inplace=True)
print(len(df))
print( df.groupby(by=['data-source']).sum())

X = pickle.load(open('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/2024-08-7_FSoLS-24-v2_gensim_embedding_.p', 'rb'))


# transform document vectors
X_embedded = TSNE(n_components=2, perplexity=100, learning_rate=3000).fit_transform(X)

print('X_embedded.shape', X_embedded.shape)
y = df['data-source'].to_list()
print(len(y))

sns.color_palette("mako", as_cmap=True)

sns.relplot(x = X_embedded[:,0], y= X_embedded[:,1], hue=y, style=y, palette='mako')


#plt.show()
plt.savefig('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/2024-08-22_tsne-representation_datasource_FSoLS-24-v2.png')