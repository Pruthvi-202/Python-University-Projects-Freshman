"""
Program: GuduruPruthvirajBonusAssignment.py
Author: Pruthviraj Guduru
Date: 9/19/2024
"""

#This function welcomes the user.
def welcome():
    print("Welcome to the Travel Cost Splitter Calculator!")

#This function adds up the total cost.
def totalcost(totalfuelcost,additional):
    total = totalfuelcost + additional
    total = round(total,2)
    return total

#This function returns the cost per person.
def percost(people,totalfuelcost,additional):
    totals = totalfuelcost + additional
    totals = round(totals,2)
    costperperson = totals / people
    costperperson = round(costperperson,2)
    return costperperson

#This function runs other function and makes everything work, including user input.
def main():
    welcome()
    people = int(input("How many people are travelling? "))
    totalfuelcost = float(input("Enter the total fuel cost in dollars: $"))
    totalfuelcost = round(totalfuelcost,2)
    additional = float(input("Enter any additional cost in dollars: $"))
    additional = round(additional,2)
    totalcost(totalfuelcost,additional)
    percost(people,totalfuelcost,additional)
    print("The total cost of the travel is $",totalcost(totalfuelcost,additional)) 
    print("The cost per traveler is $",percost(people,totalfuelcost,additional))

#The line below calls the main function.
main()
    
