#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Under GNU GPL3 license
# mcolom and SQ SG3 members

'''
Data structure from the CSV -> variable eosc_val
{
    <EOSC-TF_Codename>: {'EOSC-TF_Name': <EOSC-TF_Name>,
                         'EOSC-TF_Definition': <EOSC-TF_Definition>,
                         'Characteristics': <Characteristics>,
                         'RS_level': <RS_level>,
                         'RS_type': <RS_type>,
                         'Paper_ID': <Paper_ID>
                        }
}
'''

import csv
# import pprint


def get_cite_tag():
    '''Maps Paper_ID to the Latex cite tag
    '''
    cite_tag = {}
    with open('Latex-CiteTag.csv', encoding='utf-8', newline='') as csvf:
        csv_read = csv.DictReader(csvf)
        for cite in csv_read:
            cite_tag[cite['PaperID']] = cite['CiteTag']

    return cite_tag


def latex_table_column_names(columns):
    '''
    Return a string with the LaTeX table header.
    The header contains the given columns.
    '''
    str_table_head = '\\tablehead{\\hline '
    for i, col in enumerate(columns):
        str_table_head += f'\\textbf{{{columns[i]}}} '
        if i != len(columns) - 1:
            str_table_head += '& '

    str_table_head += '\\\\ \\hline}'
    return str_table_head


def latex_table_rows(list_attr):
    '''
    Return a string with a row formatter in LaTeX
    '''
    latex_cite_tag = get_cite_tag()
    str_tbl = ''
    for qual_attr in list_attr:
        str_tbl += '        '
        str_tbl += f'\\cite{{{latex_cite_tag[qual_attr[0]]}}}'
        str_tbl += ' & ' + qual_attr[1] + ' & ' + qual_attr[2] + ' & ' + qual_attr[3]
        str_tbl += '\\\\ \\hline\n'

    return str_tbl


def get_latex_table(eosc_key, eosc_val):
    '''
    Print a LaTeX table from a given attribute
    '''
    latex_tab = ''
    latex_tab = f'\\textbf{{{eosc_key}}}: {eosc_val["EOSC-TF_Name"]}: {eosc_val["Characteristics"]}'
    columns = 'Reference', 'Codename', 'Name', 'Definition'   # Columns in the table
    str_table = f"""
\\nopagebreak[4]
\\begin{{center}}
    {latex_table_column_names(columns)}
    \\tabletail{{\\hline}}
    \\tiny
    \\begin{{supertabular}}{{|p{{0.10\\linewidth}}|p{{0.10\\linewidth}}|p{{0.20\\linewidth}}|p{{0.60\\linewidth}}|}} \\hline
{latex_table_rows(eosc_val["Orig_Attr"])}    \\end{{supertabular}}
\\end{{center}}
"""

    latex_tab += str_table
    return latex_tab


def get_category(models):
    '''Get LaTex subsection for a given category'''
    latex_section = ''
    for eosc_key, eosc_val in models.items():
        latex_section = latex_section + get_latex_table(eosc_key, eosc_val) + '\n'

    return latex_section


if __name__ == '__main__':
    categories = {'EOSC-SCMet': 'Attribute type: Source Code Metrics',
                  'EOSC-TMet': 'Attribute type: Time Metrics',
                  'EOSC-Qual': 'Attribute type: Qualitative',
                  'EOSC-SWRelMan': 'Attribute type: DevOps-SW release and management',
                  'EOSC-SWTest': 'Attribute type: DevOps - Testing',
                  'EOSC-SrvOps': 'Attribute type: Service Operability'}

    # All models, according to their type
    # For example, EOSC-SCMet... for source code metrics
    # Read all models
    latex_str = ''
    models = {}
    csv_file = 'Quality_Models.csv'
    with open(csv_file, encoding='utf-8', newline='') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            eosc_cn = row['EOSC-TF_Codename']
            orig_attr = (row['Paper_ID'], row['Codename'], row['Name'], row['Definition'])
            if eosc_cn in models.keys():
                models[eosc_cn]['Orig_Attr'].append(orig_attr)
            else:
                models[eosc_cn] = {'EOSC-TF_Name': row['EOSC-TF_Name'],
                                    'Characteristics': row['Characteristics'],
                                    'Orig_Attr': [orig_attr]
                        }

    latex_str += f'\\subsection{{{categ}: {name_def}}}\n\n'
    latex_str += get_category(models)
    # pprint.pprint(models)

    with open('../latex/09-appendix.tex', 'w', encoding='utf-8') as ftex:
        ftex.write(latex_str)
