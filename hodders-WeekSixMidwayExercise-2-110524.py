#!/usr/bin/env python3

"""
*********************************************************************    
*    Course:     DEV 108
*    Instructor: Phil Duncan
*    Term:       Fall 2024
*
*    Programmer: Sara Hodder
*    Assignment: DEV108 Week Six Midway Check In Exercise
*    
*    Description:   
* 
*    Revision    Date               Release Comment 
*    --------    ----------         -------------------------------------------- 
*    1.0         11/03/24           Initial submission
*    1
* 
"""

# Start Problem 1
print("******  PROBLEM 1 ******")


# Loop to assign price per piece at break points and calculate total earnings
while True:
    number_of_pieces = int(input("\nHow many pieces? Enter any whole number or "
                                 "-999 to quit: "))
    if number_of_pieces == -999:
        print()
        print("Goodbye!")
        break
    elif number_of_pieces <= 0:
        earnings = 0.00
        total_earnings = float(number_of_pieces * earnings)
    elif number_of_pieces >= 0 and number_of_pieces <= 500:
        earnings = 0.73
        total_earnings = float(number_of_pieces * earnings)
    elif number_of_pieces >= 500 and number_of_pieces <= 1000:
        earnings = 1.58
        total_earnings = float(number_of_pieces * earnings)
    elif number_of_pieces >= 1000:
        earnings = 2.15
        total_earnings = float(number_of_pieces * earnings)
    else:
        pass
    print(f"At {number_of_pieces:,.0f} pieces at ${earnings:,.2f} per piece, "
          f"you've earned ${total_earnings:,.2f}.")


input("\nPress any key to continue. . .")
# End of Problem 1


# Start Problem 2
print("\n******  PROBLEM 2 ******\n")


# Validation for number of days input
def validate_days():
    while True:
        number_of_days = float(input("Enter number of days:\t"))
        if number_of_days <= 0:
            print("Invalid number of days. Please re-enter.")
            print()
        elif number_of_days > 0:
            break

    return number_of_days

# Validation for number of miles input
def validate_miles():
    while True:
        number_of_miles = float(input("Enter number of miles:\t"))
        if number_of_miles <= 0:
            print("Invalid number of miles. Please re-enter.")
            print()
        elif number_of_miles > 0:
            break

    return number_of_miles

# Calculate costs
def calc_cost(number_of_days, number_of_miles):
    cost_per_day = 29.99
    cost_per_mile = 0.35
    rental_fee = 1.75

    duration_cost = float(cost_per_day * number_of_days)
    mileage_cost = float(cost_per_mile * number_of_miles)
    total_cost = float(duration_cost + mileage_cost + rental_fee)

    return (cost_per_day, cost_per_mile, rental_fee, duration_cost, 
            mileage_cost, total_cost)

# Print cost data for the user
def print_total(cost_per_day, number_of_days, duration_cost, cost_per_mile, 
                number_of_miles, mileage_cost, rental_fee, total_cost):

    print(f"\nCar rental at ${cost_per_day} per day for "
          f"{number_of_days:,.0f} days is ${duration_cost:,.2f}."
          f"\nMileage at ${cost_per_mile} per mile for "
          f"{number_of_miles:,.0f} miles is ${mileage_cost:,.2f}."
          f"\nTotal cost including a fee of ${rental_fee} is "
          f"${total_cost:,.2f}.")

# Function calls    
number_of_days = validate_days()
number_of_miles = validate_miles()
(cost_per_day, cost_per_mile, rental_fee, duration_cost, mileage_cost, 
 total_cost) = calc_cost(number_of_days, number_of_miles)
print_total(cost_per_day, number_of_days, duration_cost, cost_per_mile, 
            number_of_miles, mileage_cost, rental_fee, total_cost)


input("\nPress any key to continue. . .")
# End of Problem 2


# Start Problem 3
print("\n******  PROBLEM 3 ******\n")


# Input with match statement to check input and assign season
month = input("Enter a month number:\t")
match month:
    case "1":
        season = "Winter"
    case "2":
        season = "Winter"
    case "3":
        season = "Spring"
    case "4":
        season = "Spring"
    case "5":
        season = "Spring"
    case "6":
        season = "Summer"
    case "7":
        season = "Summer"
    case "8":
        season = "Summer"
    case "9":
        season = "Spring"
    case "10":
        season = "Spring"
    case "11":
        season = "Spring"
    case "12":
        season = "Winter"
    case month if month is not int:
        month = 0
        season = "no season"

# Print month and season
print(f"Month {month} is in {season}.")


input("\nPress any key to exit. . .")
# End of Problem 3


# Start Problem 4
print("\n******  PROBLEM 4 ******\n")


# Setting the float constant
MAX_INPUT = 3

# Convert float constant to a counter
counter = MAX_INPUT 

# User input
while counter > 0:
    if counter == 3:
        number_1 = input("Enter number 1:\t")
        counter -= 1
    elif counter == 2:
        number_2 = input("Enter number 2:\t")
        counter -= 1
    elif counter == 1:
        number_3 = input("Enter number 3:\t")
        counter -= 1
    else:
        pass

# Convert to float
number_1 = float(number_1)
number_2 = float(number_2)
number_3 = float(number_3)

# Calculations
sum = (number_1 + number_2 + number_3)
product = (number_1 * number_2 * number_3)
average = (sum / 3)

# Print calculations
print(f"\nSum = {sum:,.0f}"
      f"\nProduct = {product:,.0f}"
      f"\nAverage = {average:,.2f}")


input("\nPress any key to exit. . .")
# End of Problem 4

# Start Problem 5
print("\n******  PROBLEM 5 ******\n")


# Establish starting message length
message_length = 0

# Input & message length check
message = str(input("Enter your short message: "))
while True:
    message_length = len(message)
    if message_length >= 1 and message_length <= 80:
        print("Accepted")
        break
    elif message_length > 80:
        print("Rejected")
        break
    elif message_length <= 1:
        print("Rejected")
        break


input("\nPress any key to exit. . .")
# End of Problem 5


# Start Bonus Problem
print("\n******  Bonus PROBLEM ******\n")


# Ask for a cost
amount = float(input("Enter a purchase amount:\t"))

# Ternary conditional to verify input is within credit limit
print(f"${amount:,.2f} is approved" if amount <= 5000 else f"${amount:,.2f} is rejected")


input("\nPress any key to exit. . .")
# End of Bonus Problem