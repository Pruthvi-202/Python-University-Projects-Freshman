"""
Author: Pruthvi Guduru
Title: GuduruPruthvirajIP5.py
Date: 10/25/2024
"""

#This function prints the welcome statement.
def welcome():
    print("Welcome to the CSU English Plural Maker!")

#This function determines whether input is valid or not.
def getValidInput(use):
    number = "0123456789"
    
    if (use == "q") or (use == "Q"):
        print("Goodbye!")

    else:
        for w in use:
            if (w == " ") or (w in number) :
                print("This word has a number or space in it, please try again.")
                use = input("Please enter a word with no spaces or numeric digits (or q to quit): ")
                getValidInput(use)
            else:
                makePlural(use)
                use = input("Please enter a word with no spaces or numeric digits (or q to quit): ")
                getValidInput(use)

#This function takes the valid input, lowercases it, and then pluralizes it
def makePlural(use):
    mod = use.lower()
    modlist = "soxz"
    consonants = "bcdfghjklmnpqrstvwxyz"
    if (mod[-1] in modlist) or ((mod[-2]+mod[-1]) == "ss") or ((mod[-2]+mod[-1]) == "sh") or ((mod[-2]+mod[-1]) == "ch"):
        print(mod + "es")
    elif(mod[-1] == "y") and (mod[-2] in consonants):
        print(mod)
    else:
        print(mod + "s")
        

#This function executes everthing.
def main():
    welcome()
    use = input("Please enter a word with no spaces or numeric digits (or q to quit): ")
    getValidInput(use)


main()
            
        
