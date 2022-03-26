from getbooks import *

#helper function for getBooks. 
def enterBook(user):
    done = "n"
    booklist = []
    while done == "n":
        book = Book()
        #comment out this line if you dont want to manually enter an ISBN each run.
        isbn = input("enter the ISBN 10 of the book you want to add.\n")
        #and uncomment this one. 
        #isbn = "9781405281782"
        title, authors, description, pages, ISBN10, ISBN13 = getBooks(isbn)
        book.updateBook(title, authors, description, pages, ISBN10, ISBN13,user)
        booklist.append(book)
       
        done = input("are you done adding books (y or n)")

    if (len(user.booklist) == 0):
        user.booklist = booklist
        user.booksOnHand = booklist
        user.booksInPossession = booklist

#helper function for saving
def saveHelper(user):
    print("saving list to file.")
    saveBooksToFile(user.booksInPossession, user)

#helper function for checking a book out (transferring the possessor)
def checkOutHelper(currentUser,transferee):
    numBooks = len(currentUser.booksInPossession)
    print("which book would you like to check out?")
    print(f"You currently have {numBooks} books in your posession.")
    transferNumber = input(f"please select a number from 0-{numBooks-1}: ")
    checkout(currentUser.booksInPossession[int(transferNumber)],transferee,currentUser)

#helper function for return Book. the borrower is the current user. 
def returnBookHelper(owner,borrower):
    numBooks = len(borrower.booksInPossession)
    print("which book would you like to return?")
    print(f"You currently have {numBooks} books in your posession.")
    transferNumber = input(f"please select a number from 0-{numBooks-1}: ")
    returnBook(borrower.booksInPossession[int(transferNumber)],owner,borrower)

#helper function for book transfer
def transferBookHelper(transferee, owner):

    numBooks = len(owner.booksInPossession)
    print("which book would you like to check out?")
    print(f"You currently have {numBooks} books in your posession.")
    transferNumber = input(f"please select a number from 0-{numBooks-1}: ")
    bookTransfer(owner.booksInPossession[int(transferNumber)],transferee,owner)


#helper function for loading from a file
def loadHelper(user):
    print("loading books from file.")
    booklist = loadBooks(user)
    user.booksInPosession = booklist
    user.booksOnHand = booklist
    user.booklist = booklist

#changes the current user 
def changeUser(usersList):
    print("what user do you want to change to?")
    i = 0
    for user in usersList:
        print(f"{i}: {user.name}")
        i = i +1
    choice = input("selection: ")
    return usersList[int(choice)]