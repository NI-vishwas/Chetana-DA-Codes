#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 2.0
# Script to calculate Simple Interest using the formula
# si = (p * t * r)/100
#

principal = float(input('Enter the principal amount: '))
t = int(input('Enter the time in months: '))
rate_of_interest = float(input('Enter the Rate of Interest in decimals: ')) # Here rate of interest is 7%

simple_interest = (principal * t * rate_of_interest)/100
#print('Simple Interest is: ')
#print(simple_interest)
print('Simple interest is: %.2f'%(simple_interest)) # Output: 1648.40 
# Other format specifiers are %i, %c, %s, %d

print(f'Simple interest is: {simple_interest: .2f}') # Output: 1648.40 

