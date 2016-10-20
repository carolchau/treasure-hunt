from random import *
from math import *
import random
import time

def treasureHunt():
    print("Ahoy, matey! Welcome to the Treasure Hunt!")
    
    # Declare variables
    distance = 0
    foundTreasure = False
    stepAmount = 0
    
    # Explorer's coordinates
    x, y = 15, 15
    myLocation = (x, y)
    
    # Treasure's coordinates
    x1 = random.choice(range(1, 31))
    y1 = random.choice(range(1, 31))
    treasureLocation = (x1, y1)
    
    if (myLocation == treasureLocation):
        print (
            "\nOh, you lucky dingleberry." 
            "\nYou found the treasure and you didn't even have to move a leg." 
            "\nThe chance of that happening is ~ 0.1%." 
            "\nWell we can't let you keep the treasure." 
            "\nAfter all, it is the journey that matters." 
            "\nAnd we wouldn't wnat you to miss out on the journey." 
            "\nLet the actual Treasure Hunt begin!")
        while (treasureLocation == myLocation):
            x1 = random.choice(range(1, 31))
            y1 = random.choice(range(1, 31))
            treasureLocation = (x1, y1)
            
    
    # Loop to find the treasure
    while (foundTreasure == False):
        if (myLocation != treasureLocation):
            print ("\nYour current location is: ", myLocation)
            direction = str.lower(input("Please enter a direction (n, s, e, w), or x to exit: "))
            
            # Check for direction
            if (direction == 'n' or direction == 'north'):
                y = y + 1
                direction = 'north.'
            elif (direction == 's' or direction == 'south'):
                y = y - 1
                direction = 'south.'
            elif (direction == 'e' or direction == 'east'):
                x = x + 1
                direction = 'east.'
            elif (direction == 'w' or direction == 'west'):
                x = x - 1
                direction = 'west.'
            elif (direction == 'X' or direction == 'x'):
                print("Aww, giving up already? So be it. \nBye!")
                return
            else:
                print ("Hey, what are you, drunk?!")
                print (direction, "is not a valid direction.")
                print ("Try Again.")
                continue
                
            myLocation = (x, y)
            print ("Alright Explorer, you went", direction)
            print ("Your location is now: ", myLocation)
            distance = sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
            print ("The distance you are from the booty is: ", distance)
            stepAmount += 1
        else:
            print ("\nCongrats, ya found da bootay!!! ")
            print ("And it only took you", stepAmount, "steps!")
            foundTreasure = True                     
                  
treasureHunt()
