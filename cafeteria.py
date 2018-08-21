# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:53:06 2018

@author: Ben.Olson
"""

from openpyxl import load_workbook
import ben.parser
import ben.account

# TODO: work on just getting data

# Load in the workbook
wb = load_workbook('./Book1.xlsx')

# Get sheet names
print("Name of sheet being analyzed: ", wb.sheetnames)

sheet = wb[wb.sheetnames[0]]

for row_index in range(1, sheet.max_row+1):
    for col_index in range(1, sheet.max_column+1): 
        ben.parser.gather_data(sheet.cell(row=row_index, column=col_index).value)
