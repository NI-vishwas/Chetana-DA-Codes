#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 1.0
# Script to demonstrate loops in Python

# Loops demonstration

# For
# When you know number of iterations or steps 
for i in range(1,10,2):
    print(i)

# While
i = 1
while i < 10:
    print(i)
    # i = i + 1
    i += 1

# We intentionally want an infinte loop
# while 1
tracker = 0
while True:
    print('hello')
    tracker += 1
    if tracker == 10:
        break
    else:
        print('vishwas')

# Can be applied to strings
username = 'vishwas'
for i in range(len(username)):
    k = username[i]
    print(k, end='*')

# for loop on strings
username = 'vishwas'
for chr in username:
    print(chr, end='-')
print()