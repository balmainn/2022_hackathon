#This is done in this way for further abstraction later down the road. 

class Person:
    def __init__(self): 
        self.name = ""
        self.role = "" #empty role for permissions


class Teacher(Person):
    def __init__(self, name):
        self.name = name
        self.role = "teacher"
        self.booklist = [] #all books
        self.booksInPossession = [] #the books currently in the classroom 
        self.teachingMaterials = [] #(lesson plans)
        self.booksLentOut = () #books currently on loan. tuple of book and a person
    

class Student(Person):

    def __init__(self, name):
        self.name = name
        self.role = "student"
        self.booksInPossession = []
