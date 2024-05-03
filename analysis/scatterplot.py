#matplotlib inline
import scattertext as st
import re, io
from pprint import pprint
import pandas as pd
import numpy as np
from scipy.stats import rankdata, hmean, norm
import spacy
from IPython.display import IFrame
from IPython.core.display import display, HTML
from scattertext import CorpusFromPandas, produce_scattertext_explorer
#display(HTML("<style>.container { width:98% !important; }</style>"))
from nltk.corpus import stopwords
from langdetect import detect

######################################
##### load English language package ###
######################################
nlp = spacy.load('en_core_news_sm')
# If this doesn't work, please uncomment the following line and use a regex-based parser instead
#nlp = st.whitespace_nlp_with_sentences

df_all = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-13_fewshot_testing.csv')
df_all.columns =['text', 'category_id']

#print(df_all.shape)
###########################################
##### keep only Desinfo and GMS texts #####
###########################################
#df_wiki = df_all.loc[df_all[''].isin([1])]
#df_desinfo = df_all.loc[df_all['lable'].isin([0])]
#df_wiki = df_wiki.tail(500)
#df = df_desinfo.append(df_wiki)
df = df_all

######################################
###### keep only non-English text ####
######################################
counter = 0
for line in df['text']:
    try:
        if detect(line) == 'en':
            df = df.drop([counter])
    except:
        continue
    counter +=1

print('nachher', df.shape)
print(df.head(5))

#################################
##### cleaning other parts from text #############
#################################
df['lable'] = df['lable'].astype(str).str.replace('0', 'Desinfo')
df['lable'] = df['lable'].astype(str).str.replace('1', 'Wikipedia')
df['text'] = df['text'].apply(lambda x: x.replace('ref', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('https', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('ref http', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('978', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('[', ' '))
df['text'] = df['text'].apply(lambda x: x.replace(']', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('{', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('}', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('|', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('<', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('>', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('|-', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('*', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('=', ''))
df['text'] = df['text'].apply(lambda x: x.replace('→', ''))
df['text'] = df['text'].apply(lambda x: x.replace('·', ''))
df['text'] = df['text'].apply(lambda x: x.replace('+', ''))
df['text'] = df['text'].apply(lambda x: x.replace('#', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('&', ' '))
df['text'] = df['text'].apply(lambda x: x.replace(':/', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('/m', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('†', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('/div', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('left', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('nbsp', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('text-align center', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('text-align left', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('at', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('pl', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('weblinks', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('ipa-text', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('books', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('hauptartikel', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('isbn', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('redirect', ' '))

#############################
##### remove stop words #####
#############################
stop_words = set(stopwords.words('english'))
new_words = ['us', 'oder', 'fr', 'gb', 'siehe', 'br', 'it', 'siehe', 'right', '/math', 'text align', 'nlts', 'fn', 'links', 'books.google.de',
             'hrsg', 'hrsg.',  'isbn 3', 'deu', 'nts','p.',  'weblinks', 'text-align', 'isbn -3', '--', 'center', 'url', 'abgerufen' ,
             'eeeeee', 'align &', '/sup']

stop_words.update(new_words)
for line in df['text']:
    x = []
    for w in line.split():
        if not w in stop_words:
            x.append(w)
    df['text'] = df['text'].replace(line, str(x))




print(df.shape)
print("Document Count")
print(df.groupby('lable')['text'].count())
print("Word Count")
print('-1')
df.groupby('lable').apply(lambda x: x.text.apply(lambda x: len(x.split())).sum())
print('0')

df['parsed'] = df.text.apply(nlp)
print('1')
print('nachher')
print(df.head(5))

corpus = st.CorpusFromParsedDocuments(df, category_col='lable', parsed_col='parsed').build()
print('2')
term_freq_df = corpus.get_term_freq_df()

######################################
##### choose GMS or Wikipedia #########
######################################
print(term_freq_df.iloc[5])
#term_freq_df['desinfo_precision'] = term_freq_df['Desinfo freq'] * 1./(term_freq_df['Desinfo freq'] + term_freq_df['GMS freq'])
term_freq_df['desinfo_precision'] = term_freq_df['Desinfo freq'] * 1./(term_freq_df['Desinfo freq'] + term_freq_df['Wikipedia freq'])
term_freq_df['desinfo_freq_pct'] = term_freq_df['Desinfo freq'] * 1./term_freq_df['Desinfo freq'].sum()
term_freq_df['desinfo_hmean'] = term_freq_df.apply(lambda x: (hmean([x['desinfo_precision'], x['desinfo_freq_pct']])
                                                                   if x['desinfo_precision'] > 0 and x['desinfo_freq_pct'] > 0
                                                                   else 0), axis=1)
print('3')
print(term_freq_df.sort_values(by='desinfo_hmean', ascending=False).iloc[:10])
print('4')


def normcdf(x):
    return norm.cdf(x, x.mean(), x.std())
term_freq_df['desinfo_precision_normcdf'] = normcdf(term_freq_df['desinfo_precision'])
term_freq_df['desinfo_freq_pct_normcdf'] = normcdf(term_freq_df['desinfo_freq_pct'])
term_freq_df['desinfo_scaled_f_score'] = hmean([term_freq_df['desinfo_precision_normcdf'], term_freq_df['desinfo_freq_pct_normcdf']])
term_freq_df.sort_values(by='desinfo_scaled_f_score', ascending=False).iloc[:10]
print('5')



term_freq_df['desinfo_corner_score'] = corpus.get_corner_scores('Desinfo')
term_freq_df.sort_values(by='desinfo_corner_score', ascending=False).iloc[:10]
print('6')

term_freq_df = corpus.get_term_freq_df()

######################################
##### chose GMS or Wikipedia #########
######################################
#term_freq_df['GMS Score'] = corpus.get_scaled_f_scores('GMS')
term_freq_df['Wikipedia Score'] = corpus.get_scaled_f_scores('Wikipedia')
term_freq_df['Desinfo Score'] = corpus.get_scaled_f_scores('Desinfo')


######################################
##### chose GMS or Wikipedia #########
######################################
#print("Top 10 GMS terms")
#pprint(list(term_freq_df.sort_values(by='GMS Score', ascending=False).index[:20]))
print("Top 10 Wikipedia terms")
pprint(list(term_freq_df.sort_values(by='Wikipedia Score', ascending=False).index[:20]))
print("Top 10 Desinfo terms")
pprint(list(term_freq_df.sort_values(by='Desinfo Score', ascending=False).index[:20]))
print('7')



'''
html = st.produce_scattertext_explorer(corpus,
                                       category='Desinfo',
                                       category_name='Desinfo',
                                       not_category_name='GMS',
                                       minimum_term_frequency=5,
                                       width_in_pixels=1000,
                                       transform=st.Scalers.log_scale_standardize)
'''

######################################
##### chose GMS or Wikipedia #########
######################################
'''
html = produce_scattertext_explorer(corpus,
                                    category='Desinfo',
                                    category_name='Desinformations Texte',
                                    #not_category_name='GMS - Wissenschaftliche Texte',
                                    not_category_name='Wikipedia - Lexikalische Texte',
                                    width_in_pixels=1000,
                                    jitter=0.1,
                                    minimum_term_frequency=10,
                                    transform=st.Scalers.percentile,
                                    metadata=df['lable'])

'''

html = produce_scattertext_explorer(corpus,
                                    category='Desinfo',
                                    category_name='Desinformations Texte',
                                    not_category_name='Lexikalischee Texte',
                                    width_in_pixels=1000,
                                    minimum_term_frequency=5,
                                    transform=st.Scalers.log_scale_standardize,
                                    metadata=df['lable'])
print('8')
file_name = 'ScattertextLog_Desinfo-Wikipedia_2021-06-30.html'
open(file_name, 'wb').write(html.encode('utf-8'))
IFrame(src=file_name, width = 1200, height=700)


print('9')
