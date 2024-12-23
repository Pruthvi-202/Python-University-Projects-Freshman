"""
Title: GuduruPruthvirajIP4
Author: Pruthvi Guduru
Date: 10/14/2024
"""
import sys

#This function welcomes the user.
def welcome():
    print("Welcome! We want to share some information about the vitamin benefits!")

#This function takes in input from the user and outputs a statement depending on that number.
def getValidInput():
    number = int(input("Please enter a number from 1-5 for a selection or enter 0 if you want to quit:"))
    if (number == 0):
        print("Goodbye! Have a nice day!")
        sys.exit("")
        
    while (number<0 or number>5):
        print("Invalid number! Please enter a number from 0 to 5.")
        getValidInput()
        
    while (number>0 and number<5):
        if (number == 1):
            print("Vitamin A protects eyes from night blindness and age-related decline.")
            getValidInput()
        elif (number == 2):
            print("Vitamin B6 promotes brain health and reduces Alzheimer's risk.")
            getValidInput()
        elif (number == 3):
            print("Vitamin B12 may improve heart health by decreasing homocysteine.")
            getValidInput()
        elif (number == 4):
            print("Vitamin C protects your health from cardiovascular issues, cancer, and strokes.")
            getValidInput()
        elif (number == 5):
            print("Vitamin D reduces the risk of diabetes.")
            getValidInput()

#This function calls the other functions and prints out everything that is necessary.
def main():
    welcome()
    getValidInput()

#This line calls the main function.
main()
