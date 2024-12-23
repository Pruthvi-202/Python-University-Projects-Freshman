#This is IP Practice 2 and is meant to calculate the cost of flying an airplane.
#Made by Pruthvi Guduru
def welcome():
    print("Welcome to CSU Airlines")
    print("Tickets are $399.99 each." "\nCarry-on bags cost $34.99 each.")
    print("Checked baggage costs $59.99 per bag.")
   
#This is the function to calculate the cost of the carry on bags without tax.
#I input the user input(cab) for the amount of carry on bags they have.
def carry_on_bags(cab):
    costcab = cab * 34.99
    costcab = round(costcab,2)
    return costcab
#This is the function to calculate the cost of the checked bags without tax.
#I input the user input(cab) for the amount of checked bags they have.
def checked_bags(chb):
    checked = chb * 59.99
    checked = round(checked,2)
    return checked

#This calculates the total without the tax.
def subtotals(cab,chb):
    subtotals = 399.99 + carry_on_bags(cab) + checked_bags(chb)
    subtotals = round(subtotals,2)
    return subtotals
    
#This function only calcutes the sales tax for the total amount everything.
#This includes the ticket, the carry on bags, and the checked bags.
def salestax(cab,chb):
    sales_tax = (399.99 + carry_on_bags(cab) + checked_bags(chb)) * 0.09
    sales_tax = round(sales_tax,2)
    return sales_tax

#This function adds up all of the costs, including the tax.
#These lines welcomes the customer and shows the prices. 
#These are the variables I will be inputting into the functions.
#These variables ask for user input.
#This prints out the customer's reciept.
def main():
    welcome()
    cab = int(input("How many carry-on bags do you have? "))
    chb = int(input("How many checked bags? "))
    carry_on_bags(cab)
    checked_bags(chb)
    totals = subtotals(cab,chb) + salestax(cab,chb)
    totals = round(totals,2)
    print("Subtotal: $",subtotals(cab,chb))
    print("Sales tax: $",salestax(cab,chb))
    print("Total: $",totals)

main()


