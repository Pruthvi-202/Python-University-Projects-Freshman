"""
Author: Pruthvi Guduru
Title: GuduruPruthvirajIP6.py
Date: 11/8/2024
"""
#This function adds spices to the list.
def addSpice():
    spice_list = []
    y = input("Please enter the spice to add: ")
    spice_list = spice_list.append(y)
    return(spice_list,main())
    
#This function checks for a spice and deletes in from the list.
def deleteSpice(addSpice):
    spice_list = []
    z = input("Please enter the spice to delete: ")
    if z in spice_list:
        spice_list = spice_list.remove(z)
        return(spice_list,main())
    else:
        print("Could not remove", '"',z,'"',",it was not found")
        main()
        
#This function lists the spices in alphabetical order.
def sortSpices(addSpice,deleteSpice):
    spice_list = spice_list.sort()
    return (new,main)

#This function displays all of the spices when the program runs.
def displaySpices(addSpice,deleteSpice,sortSpices):
    if spice_list == []:
        print("Spices: None")
    else:
        print("Spices:",spice_list)
#This function runs everything
def main():
    print("Welcome to the Spice Tracker App.")
    print("Spices: None")
    #displaySpices(addSpice,deleteSpice(addSpice()),sortSpices(addSpice()),deleteSpice(addSpice()))
    print("Options:")
    print("A) Add a new spice")
    print("D) Delete a spice")
    print("S) Sort all spices")
    print("Q) Quit")
    x = input("Please choose from the above options: ")
    x = x.lower()
    if x == "a":
        addSpice()
        displaySpices(addSpice,deleteSpice,sortSpice)
    elif x == "d":
        deleteSpice(addSpice)
        displaySpices(addSpice,deleteSpice,sortSpice)
    elif x == "s":
        sortSpices(addSpice,deleteSpice(addSpice))
        displaySpices(addSpice,deleteSpice,sortSpices)
    elif x == "q":
        print("Happy Cooking")
    else:
        print("Sorry,", '"',x,'"',"is not a valid option.")
        main()

#This line executes the program.
main()
