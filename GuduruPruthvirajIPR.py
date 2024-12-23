"""
Author: Pruthviraj Guduru
Title: GuduruPruthvirajIPR.py
Date: 11/15/2024
"""
import sys

def welcome():
    print("Welcome to the Word Analyzer!")
def addWord(word_list):
    word = input("Enter a word to add: ")
    word = word.upper()
    word_list.append(word)
    print("Added",word)

def deleteWord(word_list):
    index = int(input("Enter the index of the word to delete: "))
    if index in range(0,len(word_list)):
        word_list.remove(word_list[index])
        print("Deleted",index)
    else:
        print("Not a valid index")

def printWords(analyzeWords):
    analyzeWords(word_list)

def analyzeWords(word_list):
    print("#", "Word", "Vowels", "Consonants")
    for word in words_list:
        print(word_list[word], word)
        

def main():
    word_list = []
    while True:
        print("Select option:")
        print(" A) Add a new word.")
        print(" D) Delete a word.")
        print(" P) Print all words.")
        print(" Q) Quit the program.")
        option = input("Option? ")
        option = option.lower()
        if option == "a":
            addWord(word_list)
        elif option == "d":
            deleteWord(word_list)
        elif option == "p":
            printWords(word_list)
        elif option == "q":
            print("Ending analysis!")
            sys.exit()
        else:
            print("Not a valid option. Try again.")

#main()
#realNum = 43569.1234
#print('{:.2f}'.format(realNum))
red = 'gdfga'
print(red.count('g'))
list = ['g','e','f','g']
print(list.index('g'))
