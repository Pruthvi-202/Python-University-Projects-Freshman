
def welcome_message():
    print("Welcome to the zoo")
    print("Our ticket price for visitors 12 years and up is $15.00")
    print("Children under 12 years old gets a 40% discount.")

def calculate_discount(x):
    discount = (x * 15) * (0.60)
    discount = round(discount,2)
    return discount

def calculate_total_cost(x,y):
    older_cost = (y - x) * 15
    older_cost = round(older_cost,2)
    total = calculate_discount(x) + older_cost
    total = round(total,2)
    return total

def main():
    welcome_message()
    y = int(input("How many visitors are there in total? "))
    x = int(input("How many vistors are younger than 12? "))
    calculate_discount(x)
    calculate_total_cost(x,y)
    print("The total cost for your visit is $", calculate_total_cost(x,y))

main()

