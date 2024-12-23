"""
Program: GuduruPruthvirajIP2.py
Author: Pruthvi Guduru
Date: 9/20/2024

"""

def welcome():
    """ This function welcomes the user."""
    print("Welcome to the CSU Train Station Calculator")
    print("A train ticket costs $60.98")
    print("Bags cost $5.25 for each bag.")
    print("Beverages are $1.99 for each beverage.")

def tickets(ticket):
    """ This function calculates the total cost of the tickets."""
    totaltickets = ticket * 60.98
    totaltickets = round(totaltickets,2)
    return totaltickets

def luggage(bag):
    """ This function calculates the total cost of the baggage."""
    totalluggage = bag * 5.25
    totalluggage = round(totalluggage,2)
    return totalluggage

def beverages(beverage):
    """ This function calculates the total cost of the beverages."""
    totalbeverages = beverage * 1.99
    totalbeverages = round(totalbeverages,2)
    return totalbeverages

def withsalestax(subtotal):
    """ This function calcultes the total cost of everything with the tax."""
    salestax = subtotal * 1.08
    salestax = round(salestax,2)
    return salestax

def main():
    """ This function takes all the other fucntions above and runs them.
    It also takes in user input."""
    welcome()
    ticket = int(input("How many tickets do you need? "))
    bag = int(input("How many bags do you have? "))
    beverage = int(input("How many beverages do you want? "))
    tickets(ticket)
    luggage(bag)
    beverages(beverage)
    subtotal = tickets(ticket) + luggage(bag) + beverages(beverage)
    subtotal = round(subtotal,2)
    withsalestax(subtotal)
    print("Your subtotal is $",subtotal)
    print("Your total cost overral is $", withsalestax(subtotal))

#This command tells the program to run the main function.
main()
