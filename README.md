# 2022 Hackathon
# This program is used to keep track of books that a teacher has in their classroom, as well as which students have checked out a book. Teachers can look up books by ISBN 10 or 13 and the program will add it to a list. They can also transfer the book to another teacher. 
# The program is command line based for right now, i tried to make it inuitive to use.
but in the proecess made some componants break. Which is sort of a reoccuring theme. Individual pieces work well, it just doesnt all work well together. 
# User input is not validated, nor are edge cases. Please stick to the provided options in the prompts of the program. 
## There are 2 hard coded ISBNs at the top of main.py for you to use, if you would like. They are A Series Of Unfortunate Events, books 1 and 2 of the series. 
## getbooks.py contains the majority of the code that does stuff. 
## users.py contains definitions for person, student, and teacher. 
## bookclass.py contains the class definitions of what a book is. 
## helperfunctions.py contains helper functions used by the interface to interact with the functions in getbooks.py 
## main.py is the main function that is used for testing with some sort of interface.

# in order of the menu
## adding a book will add the book to the current user's list (0)
## checking out a book will move the book from the teacher's list into the student's list. (1)

## returning a book will move the book from the student's list to the teacher's list (2)

## transfering a book will transfer ownership between teacher 1 and teacher 2. This function is probably broken in the user interface. (3)

## Print the books in the current Users Posession. Will also display if there is no list to print. This will display above the next printed menu, so you may have to scroll up to see it. (4)

## changing user is how you test who has what books with the print statement. (5)
### currently there are 3 users set up, 2 teachers (named) and 1 student (unamed) 
### there is no number 6 intentionally. 
## clearing the screen is helpful if you have too much output (option 7)
## Loading a book from file _should_ have the books repopulate the list so as to not readd them all the time. This worked in individual function testing, but not with the gui. 
## Saving changes to a file will save the book as a .csv that can be used to reload from later. This save function works as intended. (9)

## please always start by adding a book. There is a hard coded line that is commented out if you would like to skip adding a book every time you run it 
## Also transfering or checking out a book with either no book in the list, will crash it. Please ensure that the count of the books is more than 1 before attempting a value that is not 0. I set these up as general functions to make things easier to work with in the long term. Since my goal is to expand this project to be other things than just books, it makes sense to do it this way for now. 

# final thoughts
## this project was pretty huge and I bit off more than i could chew. But I had a good time and I will continue working on this even after the hackathon ends, as it is a program my wife would like to use for her classroom. Now that I have attempted this, I have a much better understanding of how to put together a better version next time. 
