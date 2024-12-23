#My name is Pruthviraj Guduru. The date is 8/26/2024.
#The program will be able to convert pounds to kilograms.

print("Welcome, how are you today?")
print("This program will convert pounds to kilograms for you!")
    #This function allows the input to be more precise.
x = input("Please enter the weight of the object, in pounds:")
x = float(x)
    #This function allows the output to be rounded up, which is a requirement.
    #The y serves as an output to a mathematical function.
    #The round function rounds the "y" variable to the first decimal place. 
y = x / 2.205
y = round(y,1)

print(x , "pounds is about", y ,"kilograms.")
print("Have a good day!")
