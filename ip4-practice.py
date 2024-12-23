"""
Author: Pruthvi Guduru
Project: ip4-practice
Date: 10/11/2024
"""
# This function prints a welcome statment.
def welcome():
    print("Welcome to the Python Sundae Machine!")

#This function returns the flavor type.
def flavor_type():
    f = input("What flavor do you want: strawberry, vanilla, or chocolate:")
    f = f.lower()
    while not(f == "strawberry" or f == "vanilla" or f == "chocolate"):
        print("Sorry ",f, " is not a valid option.")
        f = input("What flavor do you want: strawberry, vanilla, or chocolate:")
    return f

#This function returns the amount of scoops.
def scoop_amount():
    s = ""
    s = int(input("How many scoops do you want? (1-3):"))
    while not(s == 1 or s == 2 or s == 3):
        print("Sorry ",s," is not between 1 and 3 inclusively.")
        s = ""
        s = input("How many scoops do you want? (1-3):")
    return s

#This function returns the amount of sprinkles.
def sprinkles_amount():
    p = ""
    p = int(input("How many sprinkles do you want? (0-99)"))
    while not (p>=0 and p<=99):
        print("Sorry ",p," is not between 0 and 99 inclusively.")
        p = ""
        p = int(input("How many sprinkles do you want? (0-99)"))
    return p

#This function runs everything
def main():
    welcome()
    x = flavor_type()
    y = scoop_amount()
    z = sprinkles_amount()
    print("Here is your order:")
    print("    Ice cream ", x)
    print("    # Scoops ", y)
    print("    Sprinkles ", z)
    x = input("Would you like another sundae? (Y/N):")
    x = x.upper()
    if x == "Y":
        main()
    if x == "N":
        print("Thank you!")
    else:
        print()
    
#This line executes the function.      
main()
