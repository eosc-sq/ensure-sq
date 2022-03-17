#!/usr/bin/env python
# coding: utf-8

import csv

ROOT = '../'
RAW_PATH = f'{ROOT}/raw'
DOC_PATH = f'{ROOT}/docs'

filename = 'papers_original_filtered_DG'
#filename = 'papers_original'

with open(f'{RAW_PATH}/{filename}.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for article in data:
    print(article[1])
