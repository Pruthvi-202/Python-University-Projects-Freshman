
"""
Title: Project3.py
Authors: Jude Pontes, D'Antario Whitehead, John Idell, Pruthvi Guduru
Date: 10/4/2024

"""
#These imports will be used to perform calculations and create the graph.
import math
import turtle

#This function welcomes the user.
def welcome():
    print("Welcome to the Garden Plot Calculator.")
    print("All of the numbers calculated will be in feet.")

#This function calculates the total square area for the garden.
def garden_square(length):
    area = length**2
    area = round(area,1)
    return area

#This function calculates the square area of the fountain.
def fountain_square_footage(radius):
    area = math.pi * (radius**2)
    area = round(area,1)
    return area

#This function calculates the square area of the flower bed.
def flower_bed_square_footage(length, radius):
    garden_area = length ** 2
    garden_area = round(garden_area,1)
    fountain_area = math.pi * (radius **2)
    fountain_area = round(fountain_area,1)
    square_footage = garden_area - fountain_area
    square_footage = round(square_footage,1)
    return square_footage

#This function calculates the amount of soil needed. 
def soil_amount(length,radius,depth):
    garden = length ** 2
    garden = round(garden,1)
    fountain = math.pi * (radius ** 2)
    fountain = round(fountain,1)
    amount = (garden - fountain) * depth
    amount = round(amount,1)
    return amount

#This function is a yes or no function and creates a diagram of the garden with the fountain.
def graph(length,radius):
    length = round(length,1)
    radius = round(radius,1)
    desicion = ""
    desicion = input("Would you like to see a picture of the garden(Y/N):")
    desicion = desicion.upper()
    if desicion == "Y":
        wn = turtle.Screen()
        wn.title("Garden Plot")
        

        garden = turtle.Turtle()
        garden.pensize(2)
        
        garden.fillcolor("Orange")
        garden.begin_fill()
        for i in range(4):
            garden.forward((length*10))
            garden.left(90)
        garden.end_fill()

        fountain = turtle.Turtle()
        fountain.pensize(2)

        fountain.penup()
        fountain.goto(((length*10)/2),((length*10 - radius*20)/2))
        fountain.pendown()
        fountain.fillcolor("Blue")
        fountain.begin_fill()
        fountain.circle((radius*10))
        fountain.end_fill()
    

        print("Have a nice day.")

    else:
        print("Have a nice day.")

        
        
#This function calls everything.
def main():
    welcome()
    length = float(input("Please enter the length of one of the side of the garden:"))
    length = round(length,1)
    print("You entered", length)
    radius = float(input("Please enter the radius of the fountain:"))
    radius = round(radius,1)
    print("You entered", radius)
    depth = float(input("Please enter the depth of the flower bed:"))
    depth = round(depth,1)
    print("You entered",depth)
    print("The total square footage of the garden is", garden_square(length))
    print("The total square footage of the fountain is", fountain_square_footage(radius))
    print("The total square footage of the flower bed is", flower_bed_square_footage(length,radius))
    print("The flower bed needs", soil_amount(length,radius,depth), "cubic feet of soil")
    graph(length,radius)

main()

#This coding for this project took around 6 hours to complete.
