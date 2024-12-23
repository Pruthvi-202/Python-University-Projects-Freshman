#This is the first offical Independent Programming Test.
print("Welcome, how are you today?")

#For this part, the user inputs how many people are in their group.
#It is whole number only.
x = int()
x = input("How many people dined together: ")

#"y" is the total cost of the meal.
#The user's input can contain decimals.
y = float()
y = input("How much  was the cost of the group's meal in dollars: $ ")

#The tip can also be inputed with decimals.
z = float()
z = input("How much tip do you want to offer in dollars: $ ")

#The total cost adds up both the cost of all the meals and the tip.
#The cost is rounded to two decimal places. 
totalcost = float(y) + float(z)
totalcost = round(totalcost, 2)
print("The total cost of the meal is: $", totalcost)

#The cost of each meal is divided by the number of people in the group.
#The cost is rounded to two decimal places. 
costofeachmeal = totalcost / int(x)
costofeachmeal = round(costofeachmeal, 2)
print("The cost for each person is: $", costofeachmeal)
