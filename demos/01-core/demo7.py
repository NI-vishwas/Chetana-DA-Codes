#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 1.0
# Script to take 10 numbers from the user & print their sum, average

total = 0
average = 0

for i in range(10):
    num = float(input('Enter the number: '))
    total += num

average = total / 10
print(f'The Sum is: {total}')
print(f'The average is: {average}')