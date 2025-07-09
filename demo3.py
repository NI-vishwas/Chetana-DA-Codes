#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks.reach@gmail.com
# Version: 1.0
# Script to extract username from the valid email id
# Ex: 
# Enter valid Email Id: vishwasks.reach@gmail.com
# UserName is 'vishwasks.reach'

user_email = input("Enter valid Email Id: ")
username = user_email.split('@')[0]
print(f"UserName is '{username}'")
