#!/usr/bin/env python3
#
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Handling csv files manually
# Version: 1.0

# Creating a csv file
# Take the path of the file
class User():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

if __name__ == '__main__':
    users = []
    for i in range(3):
        name = input("Enter the username: ")
        email = input("Enter the user email: ")
        phone = input("Enter the user phone: ")
        users.append(User(name, email, phone))

    fname = input("Enter the full path of the file: ")
    with open(fname, 'x') as fh:
        fh.write("name,email,phone\n")
        for user in users:
            fh.write("{0},{1},{2}\n".format(user.name, user.email, user.phone))

    print("Reading the csv file")
    with open(fname) as fh1:
        lines = fh1.readlines()
        for line in lines:
            print(line)

