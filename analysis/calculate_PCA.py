#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "PCA"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "



# importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from gensim.models.doc2vec import Doc2Vec
from sklearn.decomposition import PCA
import seaborn as sns


model = pickle.load(open(
    '/AQUS/AQUAS/data/data-set-topic-wise_2024/content/doc2vec_tsne_PCA/2024-10-17_FSoLS-24-v4_gensim_embedding_.p', 'rb'))
df = pd.read_csv(
    '/AQUS/AQUAS/data/data-set-topic-wise_2024/content/final_set/final-set_super-balanced_all-infos_2024-10-21_LSoLF-24-v4.csv', usecols=['text', 'category_id'], delimiter=",")
df.dropna(inplace=True)
print(type(model))



df['category_id'] = df['category_id'].replace('scientific', 'scientific texts')
df['category_id'] = df['category_id'].replace('popular', 'popular texts')
df['category_id'] = df['category_id'].replace('disinfo', 'dinformative texts')
df['category_id'] = df['category_id'].replace('alternative_science', 'alternative science texts')
y = df['category_id'].to_list()
print('label list', len(y))

# Get the vector representation of each document in the corpus
vectors = [model.dv[i] for i in range(len(model.dv))]

# Perform PCA on the vectors
pca = PCA(n_components=2)
principal_components = pca.fit_transform(vectors)

# Perform PCA on the vectors
pca = PCA(n_components=2)
principal_components = pca.fit_transform(vectors)


# Print the explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

sns.color_palette("mako", as_cmap=True)

sns.relplot(x = principal_components[:,0], y= principal_components[:,1], hue=y, style=y, palette='mako')

'''
# Create a scatter plot of the first two principal components
#plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=labels)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Doc2Vec Vectors')
plt.colorbar()
'''
plt.show()