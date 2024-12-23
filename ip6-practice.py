"""
Author: Pruthvi Guduru
Title: ip6-practice.py
Date: 11/4/2024
"""

#This function welcomes the user.
def welcome():
    print("Welcome to the MyBookInventory App")
    
#This function adds a title to the list of books.
def add(booklist):
    entry = input("Please enter a book title to add:")
    print("Added",'"',entry,'"')
    booklist = booklist.append(entry)
    
#This function deletes a title from the list of books.
def delete(booklist):
    entry = input("Please enter a book title to delete:")
    if entry in booklist:
        print("Deleted",'"',entry,'"')
        booklist = booklist.remove(entry)
        return(booklist,main())
    else:
        print("Note, could not remove",'"',entry,'"',"it was not found.")
    
#This function prints out all of the books in the list.
def lists(booklist):
    print("All book titles","(",len(booklist),")",":")
    for i in booklist:
        print(i)

#This function runs everything.
def main():
    booklist = []
    while True:
        print("Options:")
        print("A) Add a new book title")
        print("D) Delete a book title")
        print("L) List all of the book titles")
        print("Q) Quit")
        options = input("Please choose from the above options: ")
        mod = options.lower()
        if mod == "a":
            add(booklist)
        elif mod == "d":
            delete(booklist)
        elif mod == "l":
            lists(booklist)
        elif mod == "q":
            print("Stay Safe!")
        else:
            print("Sorry",options,"is not a valid option.")


#This line executes everything.
main()

