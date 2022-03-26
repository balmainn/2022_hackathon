from getbooks  import *
from bookclass import *
from helperfunctions import *
from users import *

#used only for clear
import os

#isbn of the book we want to add to our collection. left here for ease of use
isbn = "9781405281782" 
isbn2 = "9780060758073"
#create 2 teachers and a student
teacher = Teacher("Jamie Hyneman")
teacher2 = Teacher("Adam Savage")
student = Student("Student")
#create a users list that is not used for changing users
usersList = []
usersList.append(teacher)
usersList.append(teacher2)
usersList.append(student)
#initialize our while loop and set the current user to be teacher. 
baseMenu = 'a'
currentUser = teacher
while(baseMenu != 'x'):
    
    print("Welcome to the Classroom Book Management System.\n")
    print(f"You are signed in as {currentUser.name} your selected role is {currentUser.role}\n")
    print("0: add a book")
    print("1: Check Out a Book")
    print("2: Return a book")
    print('3: Transfer ownership of a book to another teacher.')
    print('4: Print books in your possession')
    print('5: Sign in as a different user')
    print('7: clear the screen')
    print('8: Load book list from file')
    print('9: save changes to file')
    print('x: exit')
    baseMenu = input("Plese select your choice: ")
#I dislike python not having case/switch statements, but this will do. 

#these are all helper functions located in helperfunctions.py.
#they really just print out other stuff and make it so the functions in getbooks.py will work nicely. 
    if (baseMenu == '0'):
        enterBook(teacher)
    elif (baseMenu == '1'):
        if(currentUser.role == "teacher"):
            checkOutHelper(currentUser,student)
        else:
            checkOutHelper(teacher, currentUser)
    elif (baseMenu == '2'):
        returnBookHelper(teacher,student)
    elif (baseMenu == '3'):
        transferBookHelper(teacher, teacher2)
    elif (baseMenu == '4'):    
        printAllBooks(currentUser.booksInPossession)
    elif (baseMenu == '5'):    
        currentUser = changeUser(usersList)
    elif (baseMenu == '7'):
        os.system("clear")
    elif (baseMenu == '8'):    
        loadHelper(currentUser)
    elif (baseMenu == '9'):    
        saveHelper(currentUser)
    
   
    else: print("invalid choice")
