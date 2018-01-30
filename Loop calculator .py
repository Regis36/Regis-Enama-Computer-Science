
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
