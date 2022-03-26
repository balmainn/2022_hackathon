from users import *
class Book:
    #initialize the book to be generically empty. 
    def __init__(self):
        self.title = ""
        self.authors = []
        self.pages = 0 
        self.ISBN_10 = 0
        self.ISBN_13 = 0
        self.description = ""
        self.owner = ""
        self.possessor = ""
        #need due date

    #standard all in one print method
    def printBook(self):
        print(f"Owner: {self.owner}, Possessor: {self.possessor}\nTitle: {self.title}\n Authors: {self.authors}\n Pages:{self.pages} ISBN 10: {self.ISBN_10}\n ISBN 13: {self.ISBN_13}\n Description: {self.description}")
    
    
    #update the componants of the book. 
    #intentional difference between ISBN_10 and ISBN10 for differentiation purposes. 
    def updateBook(self, title, authors, description, pages, ISBN10, ISBN13,person):
        self.title = title
        self.authors = authors
        self.pages = pages
        self.ISBN_10 = ISBN10
        self.ISBN_13 = ISBN13
        self.description = description
        self.owner = person.name 
        self.possessor = person.name