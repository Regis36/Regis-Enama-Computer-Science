##Camel Game
import random 
#Print statements
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Sahara desert.")
print("The Natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.") 

#variables
done=False
miles_traveled= 0
thirst= 0
camel_tiredness= 0
Native_distance= -20
drinks_left= 4

#Main loop
while done==False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status Check.")
    print("Q. Quit.")
    user_choice= input("Enter your choice: ")
    if user_choice.upper() == "Q":
        done= True
        
    elif user_choice.upper()== "E":
        print("Miles traveled: 0")
        print("Drinks in canteen: 3")
        print("The natives are", Native_distance, "miles behind you.")
        
    elif user_choice.upper()=="D":
        camel_tiredness= 0
        print("The camel is happy")
        Native_distance= random.randint(7,15)
        print("The Natives are",Native_distance , "Miles away")
        
    elif user_choice.upper()== "C":
        miles_traveled= random.randint(10,21)
        print("You have traveled", miles_traveled , "miles")
        thirst= thirst+1
        print("Your thirst is", thirst)
        camel_tiredness= camel_tiredness +random.randint(1,4)
        print("Your camel's tiredness is", camel_tiredness)
        Native_distance= random.randint(7,15)
        print("The Natives are", Native_distance, "miles away")

    elif user_choice.upper()== "B":
        miles_traveled= random.randint(5,13)
        print("You have traveled", miles_traveled, "miles")
        thirst= thirst+1
        print("Your thirst is", thirst)
        camel_tiredness= camel_tiredness+1
        print("Your camel's tiredness is", camel_tiredness)
        Native_distance= random.randint(7,15)
        print("The Natives are", Native_distance, "miles away")

    elif user_choice.upper()=="A":
        drinks_left= drinks_left -1

    if thirst> 4 and thirst<6:
        print("You are thirsty")
    elif thirst> 6:
        print("You died of thirst")
        done=True

    if camel_tiredness in range(5,8):
        print("Your camel is getting tired")
    elif camel_tiredness> 8:
        print("Your camel is dead")
        done=True

    if Native_distance==miles_traveled:
        print("The Natives Caught up to you")
        done=True
    elif Native_distance <= 10:
        print("The Natives are getting close!")

    if miles_traveled== 200:
        print("Congratulations, you escaped the Natives with the camel")
        done=True
        
    
        
        
        
        
        
        
    
