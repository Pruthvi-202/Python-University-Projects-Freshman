"""
Title: GuduruPruthvirajIP3.py
Author: Pruthviraj Guduru
Date: 9/30/2024

"""
import sys

#This function welcomes the user.
def welcome():
    print("Welcome to CSU Botany's awareness campaign about the most dangerous US plants.")

#This function asks for color type.
def color():
    print("A = Purple")
    print("B = Green")
    print("C = Other")
    print("What is the plant's color")
    colortype = ""
    colortype = input("Choose A, B, or C:")
    colortype = colortype.upper()
    while not(colortype == "A" or colortype == "B" or colortype == "c"):
        sys.exit("Option not available")
    return colortype
    
#This function asks for shape type.
def shape():
    print("A = Star Shape")
    print("B = Circle Shape")
    print("C = Other Shape")
    print("What is the plant's shape")
    shapetype = ""
    shapetype = input("Choose A, B, or C:")
    shapetype = shapetype.upper()
    while not(shapetype == "A" or shapetype == "B" or shapetype == "C"):
        sys.exit("Option not available")
    return shapetype

#This function does everything.   
def main():
    welcome()
    if (color() == "A" and shape() == "A"):
        print("This plant is a Castor Oil Plant, and is dangerous and toxic.")
    elif (color() == "B" and shape() == "B"):
        print("This plant is a Manchineel Tree, and is dangerous and toxic.")
    else:
        print("This plant is not recognized, but be careful")

main()

    
