from getbooks  import *
from bookclass import *
from users import *
#used only for clear
import os

#isbn of the book we want to add to our collection. 
isbn = "9781405281782" 
isbn2 = "9780060758073"

teacher = Teacher("Jamie Hyneman")
teacher2 = Teacher("Adam Savage")
student = Student("Student")
usersList = []
usersList.append(teacher)
usersList.append(teacher2)
usersList.append(student)
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
    print('9: save changes to file')
    print('x: exit')
    baseMenu = input("Plese select your choice: ")
#I dislike python not having case/switch statements, but this will do. 

    if (baseMenu == '0'):
        enterBook(teacher)
    elif (baseMenu == '1'):
        if(currentUser.role == "teacher"):
            checkOutHelper(currentUser,student)
        else
            checkOutHelper(teacher, currentUser)
    elif (baseMenu == '2'):
        returnBookHelper(teacher,currentUser)
    elif (baseMenu == '3'):
        pass
    elif (baseMenu == '4'):    
        printAllBooks(currentUser.booksInPossession)
    elif (baseMenu == '5'):    
        currentUser = changeUser(usersList)
    elif (baseMenu == '7'):
        os.system("clear")
#elif (baseMenu == '0'): 
#elif (baseMenu == '0'):    
    else: print("invalid choice")
