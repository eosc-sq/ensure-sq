#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Under GNU GPL3 license
# mariojmdavid and SQ SG3 members


import csv

if __name__ == '__main__':

    latex_str = ''
    csv_file = 'sq-charact.csv'
    with open(csv_file, encoding='utf-8', newline='') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            latex_str += f'\\textbf{{{row["Characteristic"]}}}: {row["Definition"]} \\textbf{{Notes}}: {row["Notes"]}\n\n'

    print(latex_str)
    with open('../latex/qual-char.tex', 'w', encoding='utf-8') as ftex:
        ftex.write(latex_str)
