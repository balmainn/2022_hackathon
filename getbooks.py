
import requests
import json as js
from bookclass import *

#this function takes an ISBN and grabs information about it using the google books api. 
#returns the most important objects from the json request. 

def getBooks(isbn):
#the default api url that we will interface 
    googleapi = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

#combine the googleapi with the isbn to get a responce
    resp = requests.get(googleapi + isbn)

#convert the response to text
    text = resp.text

#create a dictionary by loading it 
    js_dict = js.loads(text)

#get the things out of the json object that we care about. 
    items = js_dict.items()
    title = js_dict['items'][0]['volumeInfo']['title']
    author = js_dict['items'][0]['volumeInfo']['authors']
    description = js_dict['items'][0]['volumeInfo']['description']
    pages = js_dict['items'][0]['volumeInfo']['pageCount']
    ISBN_10_13 = js_dict['items'][0]['volumeInfo']['industryIdentifiers'] 
    ISBN10 = ISBN_10_13[0]['identifier']
    ISBN13 = ISBN_10_13[1]['identifier']
    #thumb = js_dict['items'][0]['volumeInfo']['imageLinks']['smallThumbnail'] #future project, display thumbnail with this link.
    return title, author, description, pages, ISBN10, ISBN13

 #debugging print statement used to add more things
    #print(js_dict['items'][0]['volumeInfo'].keys())


#def saveBooks(name, book):
    #with open(f'{name}_booklist.csv','w') as f:
def saveBooksToFile(bookList,person):
    with open(f'{person.name}_booklist.csv','w') as f:        
        for book in bookList:
            f.write(f"{book.owner}, {book.possessor}, {book.title},{book.authors},{book.pages},{book.ISBN_10},{book.ISBN_13}, {book.description}\n")


#takes a person and loads their booklist
def loadBooks(person):

    booklist = []
    #open the persons booklist file
    with open(f'{person.name}_booklist.csv', newline="") as f: 
       
        info = f.readlines()
        #for every line in our file split it by , and put it into a variable
        for line in info:
            book = Book()
            data = line.split(',')
            owner = data[0]
            possessor = data[1]
            title = data[2]
            authors = data[3]
            pages  = data[4]
            ISBN10 = data[5]
            ISBN13 = data[6]
            description = data[7]
            #update the book with the contents
            book.updateBook(title, authors, description, pages, ISBN10, ISBN13,person)
            booklist.append(book)
      
    return booklist

#prints all of the books for a given list. 
def printAllBooks(booklist):
    if len(booklist)== 0:
        print("no books to print!")
        return

    else:
        for book in booklist:
            book.printBook()

#user validation and the ability to enter books by things other than isbn 10 need to be added.
#search feature is needed
def enterBook(user):
    done = "n"
    booklist = []
    while done == "n":
        book = Book()
        #isbn = input("enter the ISBN 10 of the book you want to add.\n")
        isbn = "9781405281782"
        title, authors, description, pages, ISBN10, ISBN13 = getBooks(isbn)
        book.updateBook(title, authors, description, pages, ISBN10, ISBN13,user)
        booklist.append(book)
       
        done = input("are you done adding books (y or n)")

    if (len(user.booklist) == 0):
        user.booklist = booklist
        user.booksOnHand = booklist
        user.booksInPossession = booklist
    
    #todo check for duplicates. 

#returns the owner of the book.
def WhoOwnsThisBook(book):
    return book.owner

def checkOutHelper(currentUser,transferee):
    numBooks = len(currentUser.booksInPossession)
    print("which book would you like to check out?")
    print(f"You currently have {numBooks} books in your posession.")
    transferNumber = input(f"please select a number from 0-{numBooks-1}: ")
    checkout(currentUser.booksInPossession[int(transferNumber)],transferee,currentUser)

#a person can check out a book. 
def checkout(book,checker, owner):
    #make sure that the book exists in the list before trying to lend it out. 
    for b in owner.booksInPossession:
        if b.ISBN_10 == book.ISBN_10:
            book.possessor = checker.name
            removeBookFromList(owner.booksInPossession,book)
            lentList = list(owner.booksLentOut)
            lentList.append([checker.name, book])
            owner.booksLentOut = tuple(lentList)
            checker.booksInPossession.append(book)
            break
        else: pass
#helper function for return Book. the borrower is the current user. 
def returnBookHelper(book,owner,borrower):
    numBooks = len(borrower.booksInPossession)
    print("which book would you like to return?")
    print(f"You currently have {numBooks} books in your posession.")
    transferNumber = input(f"please select a number from 0-{numBooks-1}: ")
    returnBook(borrower.booksInPossession[int(transferNumber)],owner,borrower)
#return the book to its rightful owner. 
def returnBook(book,owner,borrower):
    #the owner is now in possession of the book once again
    book.possessor = book.owner 
    #remove the book from the lending list 
    lentList = list(owner.booksLentOut)
    #print(lentList)
    i = 0
    for b in lentList:
        if(b[1].ISBN_10 == book.ISBN_10):
            del lentList[i]
            break
        
        else:
            i= i+1
    owner.booksInPossession.append(book)
    owner.booksLentOut = tuple(lentList)

    #remove the book from the borrower's list
    removeBookFromList(borrower.booksInPossession,book)

#only teachers can transfer ownership to another teacher. 
#this will be abstracted in the future to include lesson plans. 
def bookTransfer(book, transferee, authorizer):
    if (authorizer.role == "teacher" and transferee.role == "teacher"):
        book.owner = transferee.name 
        book.possessor = transferee.name
        removeBookFromList(authorizer.booksInPossession, book)
        transferee.booksInPossession.append(book)
    else:
        print("error, students cannot transfer books.")

#removes a book from a list by examining the ISBN 10
def removeBookFromList(booklist,bookToRemove):
    i = 0
    for book in booklist:
        if ((book.ISBN_10) == (bookToRemove.ISBN_10)):
            del booklist[i]
            break
        else:
            i = i +1    




#searching for books template 
"""
def searchByTitle(title):
    titleAPI = https://www.googleapis.com/books/v1/volumes?q=title:'
    resp = requests.get(googleapi + title)

    #convert the response to text
        text = resp.text

    #create a dictionary by loading it 
        js_dict = js.loads(text)
    #this is a giant list of all search results. need to refine and make pretty. 
    #have user select value 0-x where x is the max search results. 
    #it will then take the ISBN of this book and give it to getBooks. 
    #also add an option to add multiple separated by comma.     
"""