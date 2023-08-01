#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Under GNU GPL3 license
# mcolom and SQ SG3 members


import csv


def get_cite_tag():
    ''' Maps Paper_ID to the Latex cite tag
    '''
    cite_tag = {}
    with open('Latex-CiteTag.csv', encoding='utf-8', newline='') as csvf:
        csv_read = csv.DictReader(csvf)
        for cite in csv_read:
            cite_tag[cite['PaperID']] = cite['CiteTag']

    return cite_tag


def get_section(cat_def, all_attr):
    ''' Get LaTex subsection for a given category
    '''
    latex_str = ''
    latex_cite_tag = get_cite_tag()
    for attrib in all_attr:
        if attrib["Attribute_type"] == cat_def:
            paperids = attrib["Paper_ID"].split(':')
            cite_tag = []
            for paperid in paperids:
                cite_tag.append(latex_cite_tag[paperid])

            str_tag = ','.join(cite_tag)
            latex_str += f'\\textbf{{{attrib["EOSC-TF_Codename"]}}}: {attrib["EOSC-TF_Name"]}: {attrib["Characteristics"]}\n\n'
            latex_str += '\\begin{itemize}\n'
            latex_str += f'    \\item {attrib["EOSC-TF_Definition"]} \\cite[{str_tag}]\n'
            latex_str += f'    \\item {attrib["RS_level"]}\n'
            if attrib["RS_type"]:
                latex_str += f'    \\item {attrib["RS_type"]}\n'

            latex_str += '\\end{itemize}\n\n'

    return latex_str


if __name__ == '__main__':
    categories = {'Source Code Metrics': 'EOSC-SCMet',
                  'Time Metrics': 'EOSC-TMet',
                  'Qualitative': 'EOSC-Qual',
                  'DevOps-SW release and management': 'EOSC-SWRelMan',
                  'DevOps - Testing': 'EOSC-SWTest',
                  'Service Operability': 'EOSC-SrvOps'
              }

    latex_str = ''
    all_attr = []
    csv_file = 'Quality_Models.csv'
    with open(csv_file, encoding='utf-8', newline='') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            all_attr.append(row)

    for cat_def, cat_code in categories.items():
        latex_str += f'\\subsection{{{cat_def}: Attribute type: {cat_code}}}\n\n'
        latex_str += get_section(cat_def, all_attr)

    print(latex_str)
    with open('../latex/09-appendix.tex', 'w', encoding='utf-8') as ftex:
        ftex.write(latex_str)
