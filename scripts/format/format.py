#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Under GNU GPL3 license
# mcolom and SQ SG3 members

import csv

def row_table_column_names_latex(columns):
    '''
    Return a string with the LaTeX table header.
    The header contains the given columns.
    '''
    s = '\\tablehead{{ \\hline '
    
    for i, col in enumerate(columns):
        s += f'\\textbf{{{columns[i]}}} '
        if i != len(columns) - 1:
            s += f'& '
    
    s += '\\\\ \\hline }}'
    return s
            
def row_table_column_fields_latex(row, columns):
    '''
    Return a string with a row formatter in LaTeX
    '''
    s = ''    
    for i, col in enumerate(columns):
        s += f'{row[col]} '
        if i != len(columns) - 1:
            s += f'& '
    s += '\\\\ \\hline'
    return s    

def print_row_latex(row, columns):
    '''
    Print a LaTeX table from a given row
    '''

    print(f"""
$\\rightarrow$ \\textbf{{ToDo}}
\\begin{{center}}
    {row_table_column_names_latex(columns)}
    \\tabletail{{ \\hline }}
    \\small
    \\begin{{supertabular}}{{|p{{0.10\\linewidth}}|p{{0.10\\linewidth}}|p{{0.70\\linewidth}}|}}
        \\hline
        {row_table_column_fields_latex(row, columns)}
    \\end{{supertabular}}
\\end{{center}}
""")

all_qmodels_filename = 'All Quality Models - Detail-All QModels.csv'
columns = 'Paper ID', 'EOSC-TF Codename', 'Definition' # Columns in the table we show

# All models, according to their type
# For example, EOSC-SCMet... for source code metrics
models = {}

# Read all models
with open(all_qmodels_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if row['Paper ID']:
            
            codename = row['EOSC-TF Codename'].strip()
            if codename:
                if codename in models:
                    models[codename].append(row)
                else:
                    models[codename] = [row, ]

# Source code metrics
print("% *** Source code metrics")
for model in models:
    if model.startswith("EOSC-SCMet"):
        for row in models[model]:
            print_row_latex(row, columns)
print()

# Time metrics
print("% *** Time metrics")
for model in models:
    if model.startswith("EOSC-TMet"):
        for row in models[model]:
            print_row_latex(row, columns)
print()
