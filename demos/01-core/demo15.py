#!/usr/bin/env python3
#
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to demonstrate file handling
# using 'with' statement
# Version: 1.0


# Take the path of the file
fname = input("Enter the full path of the file: ")
with open(fname, 'x') as fh:
    fh.write("This is a Python Course")

