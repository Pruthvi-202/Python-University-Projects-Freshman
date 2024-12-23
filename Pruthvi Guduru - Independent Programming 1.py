print("Welcome, how are you?")

x = int()
x = input("How many people dined together: ")

y = float()
y = input("How much  was the cost of the group's meal in dollars :$ ")

z = float()
z = input("How much tip do you want to offer in dollars :$ ")

totalcost = float(y) + float(z)
totalcost = round(totalcost, 2)
print("The total cost of the meal is : $", totalcost)

costofeachmeal = totalcost / int(x)
costofeachmeal = round(costofeachmeal, 2)
print("The cost for each person is : $", costofeachmeal)
