#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 1.0
# Script to extract domain of an email id
# Ex: 
# Enter valid Email Id: vishwasks.reach@gmail.com
# Domain is 'com' 

# vishwasks.reach@gmail.com
user_email = input("Enter valid Email Id: ")

# ['vishwasks.reach', 'gmail.com' ]
subdomain = user_email.split('@')[1]

maindomain = subdomain[subdomain.find('.')+1:]
print(f"Domain is '{maindomain}'")
