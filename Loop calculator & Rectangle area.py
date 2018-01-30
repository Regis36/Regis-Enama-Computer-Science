'''
##This program will calculate the amount of miles per gallon used by cars
while True:
    print("This program will calculate the amount of miles per gallon used by cars")
    miles_driven = float(input(" Please enter the amount of miles driven :"))
    gallon_used = float(input("Enter the gallons used : "))
    miles_per_Gallon = miles_driven/gallon_used
    print("Your miles per gallon is", miles_per_Gallon)
    user_input= input("would you like to perform a new calculation? Y/N")
    if user_input== "Y" or user_input== "y":
        continue
    else:
        break
'''

##Calculate the area of a rectangle and allow the user to calculate as many operations they want and exit
while True:
    print("This program will calculate the area of a rectangle")
    Length= float(input("Enter the value of the length :"))
    Width= float(input("Enter the value of the width:"))
    Area_of_a_rectangle= Length*Width
    print("The area of the rectangle is", Area_of_a_rectangle)
    user_input= input("would you like to find the area of a rectangle with new dimmensions? Yes/No")
    if user_input== "Yes":
        continue
    else:
        break
              
