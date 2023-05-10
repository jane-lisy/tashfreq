#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
builds lexicon from the texts in the texts folder
"""

import glob
import pandas as pd
import re

# merge all 9 texts

filenames = glob.glob('texts/*.csv')
col_names = ['order', 'title', 'sound', 'morpheme', 'm-gloss', 'category']

df = pd.concat([pd.read_csv(filename, names = col_names, header = 0) \
                for filename in filenames])

df = df[['sound', 'morpheme', 'm-gloss', 'category']]

# get duplicates labelled "N" first, then the rest
noun_df = df.loc[df['category'] == 'N']
noun_lexicon = noun_df.drop_duplicates()

lexicon = pd.concat([noun_lexicon, df]).drop_duplicates(subset = ['sound', 'morpheme'])
lexicon.to_csv('output/lexicon_all.csv', index = False)

# preprocess word_df
word_df = pd.read_csv('word_df.csv', header = 1)
word_list = word_df.values.tolist()

# flatten list and eliminate nans
word_list = [word for row in word_list for word in row if word == word]
# get unique wordforms
wordforms = set(word_list)

lexicon = lexicon.loc[lexicon['category'] == 'N']
lexicon['sound'] = lexicon['sound'].str.replace('ʷ', 'w')
wordforms = set([re.sub('ʷ', 'w', wordform) for wordform in wordforms])
oo_lexicon = lexicon.loc[~lexicon['sound'].isin(wordforms)]

