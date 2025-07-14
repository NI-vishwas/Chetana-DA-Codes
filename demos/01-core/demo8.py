#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 1.0
# Script demonstrating usage of while with a string

name = "Vishwas Singh"
length_of_name = len(name)

tracker = 0
while tracker < length_of_name:
    print(name[tracker], end="-")
    tracker += 1

print()