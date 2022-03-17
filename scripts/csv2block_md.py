#!/usr/bin/env python
# coding: utf-8

import csv

ROOT = '../'
RAW_PATH = f'{ROOT}/raw'
DOC_PATH = f'{ROOT}/docs'

filein = 'papers_original_filtered_DG'
fileout = 'papers_original'

with open(f'{RAW_PATH}/{filein}.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
idx = 0
str_write = ''
for article in data:
    str_write = (str_write + '\n# ' + str(idx) + ' - ' + article[1] + '\n'
                 '\n## ' + article[0] + '\n'
                 '\n## ' + article[4] + '\n\n'
                 '' + article[5] + '\n\n'
                 '| MD  | ER  | MC  | VL  | DG  |\n'
                 '| --- | --- | --- | --- | --- |\n'
                 '|  |  |  |  |  |\n'
                 '---\n'
                )

    if not ((idx+1) % 20):
        fileout = 'papers_batch_' + str(idx)
        with open(f'{DOC_PATH}/papers_batch_{str(idx)}.md', 'w') as f:
            f.write(str_write)

        str_write = ''

    if idx == 146:
        fileout = 'papers_batch_' + str(idx)
        with open(f'{DOC_PATH}/papers_batch_{str(idx)}.md', 'w') as f:
            f.write(str_write)

        str_write = ''

    idx = idx + 1

