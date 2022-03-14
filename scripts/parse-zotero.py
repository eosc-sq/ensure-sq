#!/usr/bin/env python3

# -*- encoding: utf-8 -*-
#
# Copyright 2022 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#

"""Produce a Markdown table from zotero library, json format
"""

import json
fjson = 'EOSC_IQRS.json'
with open(fjson, 'r') as f:
    docs = json.load(f)

print('| In Zotero | URL | Title |')
print('| --- | --- | --- |')

for doc in docs:
    if 'URL' in doc.keys():
        print('| Yes |', doc['URL'], '|', doc['title'], '|')
    else:
        print('NOURL', doc['title'])


