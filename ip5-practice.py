"""
Author: Pruthvi Guduru
Title: ip5-practice.py
Date: 10/21/2024
"""
#This function verfies the id.
def validation(x):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    if x == "q" or x == "Q":
        print("Stay Safe!")
        
    if len(x) == 7:
        for i in x[0:3]:
            if i in letters:
                if x[3] == "-":
                    for j in x[4:7]:
                        if j in digits:
                            print("Valid Password")
                        else:
                            print("Invalid label - does not end with 3 digits.")
                            x = input("Plase enter a label to verify (or Q to quit):")
                            x = x.lower()
                            x = x.replace(" ","")
                            if x == "q" or x == "Q":
                                print("Stay Safe!")
                            else:
                                validation(x)

                else:
                    print("Invalid label - does not have a dash in the middle.")
                    x = input("Plase enter a label to verify (or Q to quit):")
                    x = x.lower()
                    x = x.replace(" ","")
                    if x == "q" or x == "Q":
                        print("Stay Safe!")
                    else:
                        validation(x)
            else:
                print("Invalid label - does not start with 3 letters.")
                x = input("Plase enter a label to verify (or Q to quit):")
                x = x.lower()
                x = x.replace(" ","")
                if x == "q" or x == "Q":
                    print("Stay Safe!")
                else:
                    validation(x)
    if len(x)<7:
        print("Invalid label - too short.")
        x = input("Plase enter a label to verify (or Q to quit):")
        x = x.lower()
        x = x.replace(" ","")
        if x == "q" or x == "Q":
            print("Stay Safe!")
        else:
            validation(x)

    if len(x)>7:
       print("Invalid label - too long.")
       x = input("Plase enter a label to verify (or Q to quit):")
       x = x.lower()
       x = x.replace(" ","")
       if x == "q" or x == "Q":
            print("Stay Safe!")
       else:
            validation(x) 

    #if x[3] == "-":
        #return True
    #else:
        #print("Invalid label - does not have a dash in the middle.")
        #validation()

    #for j in x[4:7]:
        #if j in digits:
            #return True
    #else:
            #print("Invalid label - does not end with 3 digits.")
            #validation()
    #else:
        #print("Invalid label - too short.")
        #validation()
        
#This function runs everything
def main():
    print("Welcome to the label verifier script!")
    print("Valid labels are of the form:")
    print("      <letter><letter><letter> - <digit><digit><digit> (spaces are allowed)")
    x = input("Plase enter a label to verify (or Q to quit):")
    x = x.lower()
    x = x.replace(" ","")
    if x == "q" or x == "Q":
        print("Stay Safe!")
    else:
        validation(x)
#This line executes everything.
main()
