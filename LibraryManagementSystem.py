# Library Management System
# Class: Library, Student
import sys
class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayAvailableBooks(self):
        print("The books we have in the library are:")
        for book in self.availablebooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("you have now borrowed it.")
        else:
            print("Sorry, it's not in the library at the moment.")

    def addBook(self, returnedBook):
        self.availablebooks.append(returnedBook)
        print("Thanks for returning your borrowed book.")


class Student:
    def requestBook(self):
        print("Enter the name of the book you would like to check out:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you would like to return:")
        self.book = input()
        return self.book

def main():
    library = Library(["The Last Battle", "The Screwtape Letters", "The Great Divorce"])
    student = Student()
    done = False
    while not done:
        print(""" ====Library Menu===
               1. Display all available books
               2. Request a book
               3. Return a book
               4. Exit
               """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.displayAvailableBooks()
        elif choice == 2:
            library.lendBook(student.requestBook())
        elif choice == 3:
            library.addBook(student.returnBook())
        else:
            sys.exit()

main()