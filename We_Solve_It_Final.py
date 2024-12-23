"""
Project: We_Solve_It_.py
Team: Jude Pontes, Pruthvi Guduru
Date Last Updated: 11/19/2024
About: This program is used to provide the user helpful information about hurricanes and floods.
"""

#I imported 'sys' in case the user wants to leave the program and close down the system.
import sys

# This function welcomes the user and explains what the program is used for.
# This function does not have any parameters.
# This function also gives some basic items the user can use regardless of the disaster.
def welcome():
    print("Hello, welcome to our disaster preparation and guidance program.")
    print("For now, we will be providing helpful information for only hurricanes and floods.")
    print("Below are hotlines you can call if you need any form of help during a disaster:")

    hotlines = ["1-800-304-9320 : Disaster Recovery Help and Referrals", "1-800-985-5990 : Immediate Crisis Counseling", "211 : Disaster Evacuation Information", "911 : Police Assistance"]
    for number in hotlines:
        print(" ", number)

    print(' ')

    basic_list = ['Whistle','Water Bottles','Flashlight','Batteries','First Aid Kit','Rain Jacket','Electronic Device','Packaged Food and Food Cans']
    print("Here are some basic items that will help you for any type of disaster:")
    for item in basic_list:
        print(" ", item)

    save_checklist(basic_list)

    print(" ")
    print("If you want to know about hurricanes, type in 'h' or 'H'.")
    print("If you want to know about floods, type in 'f' or 'F'.")
    print("If you want to exit the program, type in 'x' or 'X'.")
    print(' ')

# This function saves the checklist to a file.
# The parameter items is a list of items to be saved in the file.
def save_checklist(items):
    with open("preparedness_checklist.txt", "w") as file:
        file.write("Disaster Preparedness Checklist:\n")
        for item in items:
            file.write(f"- {item}\n")
    print("Checklist saved to 'preparedness_checklist.txt'.")
   
#This function is used when the user wants to learn more about the hurricanes.
#This function does not have any parameters.
#First, it asks the user to input the wind speed in their area, so they will know what type of hurricane they will witness in order to prepare.
#Second, it asks the user to input the state in which they live to check approximatly how long the hurricane will last and when the hurricanes will usually attack. This helps prepare the user.
def hurricane():
    user_input = int(input("Type in the wind speeds in terms of miles per hour(numbers only):"))
    user_input = round(user_input,0)
    if (user_input <= 73):
        print("Your area most likely won't deal with a hurricane, but still remain cautious.")
        print(" ")
    elif (user_input >= 74 and user_input <= 95):
        print("This is a Category 1 Hurricane.")
        print("Prepare your property and remain indoors.")
        print("Prepare an emergency plan and gather all of your supplies.")
        print("Stay away from glass")
        print(" ")
        print("After the hurricane ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials.")
        print(" ")
    elif (user_input >= 96 and user_input <=110):
        print("This is a Category 2 Hurricane.")
        print("Prioritize securing your home by boarding up windows, moving to the lowest interior room away from windows.")
        print("Gather all of your supplies and make sure lights and phones are fully charged.")
        print(" ")
        print("After the hurricane ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials.")
        print(" ")
    elif (user_input >= 111 and user_input <= 129):
        print("This is a Category 3 Hurricane.")
        print("Evacuating is recommended.")
        print("Figure out where your evacuation zones are.")
        print("Be very careful when driving as there can be moving waters on the roads.")
        print(" ")
        print("After the hurricane ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials.")
        print(" ")
    elif (user_input >= 130 and user_input <= 156):
        print("This is a Category 4 Hurricane.")
        print("Evacuate immediatley. Wind speeds of this strength can lead to very disasterous damages.")
        print("Be very careful when driving and try to remain as calm as possible")
        print(" ")
        print("After the hurricane ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials.")
        print(" ")
    elif (user_input >= 157):
        print("This is a Category 5 Hurricane.")
        print("Evacuate immediatley. This is the strongest form of hurricane. Seek shelter elsewhere.")
        print("Move up to higher elevation if possible")
        print("Prepare all you supplies and look out for coast guard and any other rescue organization.")
        print(" ")
        print("After the hurricane ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials.")
        print(" ")
    elif (user_input >0):
        print("Incorrect Input, please try again.")
        hurricane()

    eastern_pacific_hurricane_states = ['california','nevada','utah','arizona','colorado','new mexico']
    atlantic_hurricane_states = ['maine','new hampshire','massachusetts','rhode island','connecticut','new jersey','delware','maryland','virginia','north carolina','south carolina','georgia','florida','mississippi','louisiana','alabama']
    central_pacific_hurricane_state = ['hawaii']
    state_input = input("Type in the U.S state that you reside in(no abbreviations): ")
    state_input = state_input.lower()

    if (state_input in eastern_pacific_hurricane_states):
        print("Your hurricane season will occur from May 15 to November 30")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (state_input in atlantic_hurricane_states):
        print("Your hurricane season will occur from June 1 to November 30")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (state_input in central_pacific_hurricane_state):
        print("Your hurricane season will occur from June 1 to November 30")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    else:
        print("Your state will most likely not be affected by hurricanes.")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
           
#This function is for when the user wants to know more about floods.
#This function does not have any parameters.
#This function asks the user for the water level in their area to offer advice on the severity of the flood and how to survive before, during, and after the flood.
def flood():
    flood_input = float(input("Type in the water level of the flood in feet: "))
    flood_input = round(flood_input,1)

    if (flood_input >= 0 and flood_input < 1.6):
        print("This is a very low flood")
        print("Try evacuating or moving to a safe shelter.")
        print("Be wary of electrical openings.")
        print("Stay away from bridges that are surrounded by fast moving waters.")
        print(" ")
        print("After the flood ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Avoid driving, if possible")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials, local radios, and disaster radios.")
        print(" ")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (flood_input >= 1.6 and flood_input < 3.3):
        print("This is a low level flood")
        print("Try evacuating or moving to a safe shelter.")
        print("Be wary of electrical openings.")
        print("Stay away from bridges that are surrounded by fast moving waters.")
        print(" ")
        print("After the flood ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Avoid driving, if possible")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials, local radios, and disaster radios.")
        print(" ")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (flood_input >= 3.3 and flood_input < 6.6):
        print("This is a medium level flood.")
        print("Evacuate immediatly if told to do so.")
        print("Do not touch any electrical openings.")
        print("Stay away from bridges that are surrounded by fast moving waters.")
        print(" ")
        print("After the flood ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Avoid driving, if possible")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials, local radios, and disaster radios.")
        print(" ")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (flood_input >= 6.6 and flood_input < 16.4):
        print("This is a high level flood.")
        print("Try to move to higher ground and stay there, while help arrives.")
        print("Be wary of electrical openings.")
        print("Be wary of animals")
        print("Stay away from bridges that are surrounded by fast moving waters.")
        print(" ")
        print("After the flood ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Avoid driving, if possible")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials, local radios, and disaster radios.")
        print(" ")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    elif (flood_input >= 16.4):
        print("This is a severe level flood.")
        print("Try to move to higher ground and stay there, while help arrives.")
        print("Be wary of electrical openings.")
        print("Be wary of animals.")
        print("Stay away from bridges that are surrounded by fast moving waters.")
        print(" ")
        print("After the flood ends, wear protective chlothing and do not come in contact with any form of electricity.")
        print("Avoid driving, if possible")
        print("Take pictures of damages done to your belongings and property, and report it to your insurance provider.")
        print("Try to stay in a group with others that you can trust.")
        print("Do not try to come in contact with floodwater as the water can contain dangerous pathogens.")
        print("Be on the look out for special information and orders by your local officials, local radios, and disaster radios.")
        print(" ")
        permission = input("Would you like to check for another disaster(y/n):")
        permission = permission.lower()
        if permission == 'y':
            print(" \n \n ")
            main()
        else:
            print("Goodbye, stay safe!")
            sys.exit()
    else:
        print("Incorrect input. Please try again.")
        flood()

#This function runs everything. It does not have any parameters.
def main():
    welcome()
    user_input = input("Enter the type of disaster you are trying to research: ")
    user_input = user_input.lower()
    if user_input == "h":
        hurricane()
    elif user_input == 'f':
        flood()
    elif user_input == 'x':
        print("Goodbye, stay safe!")
        sys.exit()
    while user_input != 'h' or user_input != 'f' or user_input != 'x':
        print("Incorrect input, please try again.")
        print(" \n \n ")
        main()

# This function executes everything.        
main()
