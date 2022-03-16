#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from tabulate  import tabulate

ROOT = '../'
RAW_PATH = f'{ROOT}/raw'
DOC_PATH = f'{ROOT}/docs'

#filename = 'papers_original_filtered_DG'
filename = 'papers_original'

df = pd.read_csv(f'{RAW_PATH}/{filename}.csv', encoding="utf-8", engine='python')
df.reset_index(inplace=True)
df.rename(columns={'index':'ID'}, inplace=True)

def add_link(title, link):
    return f'[{title}]({link})'
df.insert(2, 'Linkable_Title', df.apply(lambda x: add_link(x['Title'], x['Link']), axis=1))

cols=df.columns
df2=pd.DataFrame([[':--- ',' :--- ',' :--- ',' :--- ',' :--- ',' :--- ',' :--- ',' :--- ']], columns=cols)

df3 = pd.concat([df2,df])
df3.drop(['Title','Link'], axis=1, inplace=True)
df3.to_csv(f'{DOC_PATH}/{filename}.md', sep='|', index=False)

