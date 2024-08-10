#------------------------------------------------
# Program name – project1_7-11-Doubles_NayleneRondon.py
# Written by – Naylene Rondon
# Date – Began: 2/6/17
# Description of the program:
#Simulate playing 7-11 game. Player wins if the sum equals
# 7 or 11 or if the dice are equal in value.
#------------------------------------------------
import random  #Import random function

#Start

#Input & Variables
userName = input("Hey. What's your name? ")
go = "yes"
counter = int(0)
won = int(0)

#Loop
while(go != "no"):
    
    #Random Variables
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)


    #Process
    add = die1 + die2

    #Keep user informed
    print("\nDie 1 is: " + str(die1)  + ". Die 2 is: " + str(die2)+ ".")
    print("They add to: " + str(add))

    #Decision 1
    if(add == 7):
        print("\nCongrats, " + userName + ". You won. It adds to a seven.")
        won = won + 1
        
    elif(add == 11):
        print("\nCongrats, " + userName + ". You won. It adds to an eleven.")
        won = won + 1
        
    elif(die1 == die2):
        print("\nCongrats, " + userName + ". You won. It's a double.")
        won = won + 1
        
    else:
        print("\nToo bad, " + userName + ". Try again.")


    counter = counter + 1
    go = input("\nDo you want to play again? (yes/no) ") #Continues or Breaks Loop
    print("------------------------------------------------------")

#Displays at Quits
print("\nYou played " + str(counter) + " time(s).")
print("You won " + str(won) + " time(s).")
