#!/usr/bin/env python3
#
# Email: vishwasks.reach@gmail.com
# Author: vishwas Singh
# Script demonstrating OOPs in python


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Title: {self.title} | author: {self.author}")

class Magazine(Book):
    def __init__(self, title, author):
        super().__init__(title,author)

p1 = Magazine("pride & prejudice", "jane austen")
#print(p1.title)
#print(p1.author)
p1.display_book()
p2 = Magazine("Ramayana", "Valmiki")
#print(p2.title)
#print(p2.author)
p2.display_book()
