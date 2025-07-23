#!/usr/bin/env python3
#
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to demonstrate file handling
# Version: 1.0


# Take the path of the file
fname = input("Enter the full path of the file: ")
fh = open(fname)
lines = fh.readlines()

for line in lines:
    print(line, end="")
