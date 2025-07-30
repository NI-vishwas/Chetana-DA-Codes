#!/usr/bin/env python3
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to handle csv files using csv module

import csv

def read_csv_file(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        print(f"Content of '{filename}':")
        for row in csv_reader:
            print(row)

if __name__ == '__main__':
    fname = input("Enter the csv file to read: ")
    read_csv_file(fname)
