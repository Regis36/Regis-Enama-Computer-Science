import random
##Soccer game
'''
get the ball into the net and score within 10 moves while staying away from the defenders
'''
#Instructions 
print("Welcome to Soccer") 
Name= (input("please enter your team name: "))
print("Hello", Name, "You have stolen the ball from the other team and have to make your way through the field")
print("The opponent wants the ball back and are chasing you down!")
print("Get the ball into the net while keeping it away from the other team in 10 moves either by passing or beating the defender with a skill move")
print("Good luck")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#variables
meters_traveled= 0
defender_distance= 3
skill_moves_left= 5
passes_left=3
tiredness= 0
moves_left= 10
score=0

#Main Loop
while done == True:
    Dribble_fullspeed= random.randrange(5,21)
    defender_behind= random.randint(1,10)
    print("A. Dribble moderate speed")
    print("B. Dribble full speed")
    print("C. Skill move")
    print("D. Pass the ball")
    print("E. Status check")
    print("F. Quit")
    print("")
    user_choice= input("Please enter your choice: ")

    if user_choice== "F" or user_input=="f":
        print(int(score))
        done= False
        
        

    
    
    



