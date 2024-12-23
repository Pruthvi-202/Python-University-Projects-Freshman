import sys

#This function welcomes people
def welcome():
    print("Welcome to the Activity Selector")

#This function asks for people
def who():
    n = ""
    n = input("Please enter who the activity is for (individual, couple, or group):")
    n = n.lower()
    while not(n == "individual" or n == "couple" or n == "group"):
        sys.exit("Sorry not a valid choice for the type of company. Good bye.")
    return n

#This function asks for location.
def location():
    x= ""
    x = input("Please enter the location for the activity(indoors, outdoors, or lake):")
    x = x.lower()
    if (x == "indoors" or x == "outdoors" or x == "lake"):
        return x
    else:
        sys.exit("Sorry not a valid choice for the location. Good bye.")

#This function shows activity.
def activity(n,x):
    if (n == "individual" and x == "indoors"):
        print("The activity selected is homework.")
    elif (n == "individual" and x == "outdoors"):
        print("The activity selected is biking.")
    elif (n == "couple" and x == "outdoors"):
        print("The activity selected is to watch the sunset.")
    elif (n == "group" and x == "indoors"):
        print("The activity selected is escape room.")
    elif (n == "group" and x == "outdoors"):
        print("The activity selected is to Roast marshmallows.")
    elif (n == "group" and x == "lake"):
        print("The activity selected is canoeing")
    else:
        print("No activity was selected.")

#This function calls everything.
def main():
    welcome()
    activity(who(),location())

main()
