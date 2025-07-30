#!/usr/bin/env python
# Script to use csv module
import csv
# Exploring the dataset
FILENAME = 'credit_card.csv'

# Exploration of the columns which are there

try:
    with open(FILENAME) as fh:
        csv_reader = csv.reader(fh)
        for row in csv_reader:
            # Do not print if first element in a row is ''
            for row_item in row:
                if row_item == '':
                    row_item = 'NA'
            print(row)
        
except FileNotFoundError:
    print("Csv file not found")
