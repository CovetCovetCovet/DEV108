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
*    --------     ----------        ------------------------------------------------------ 
*    1.0         
*    1
* 
"""

# Start Problem 1
print("******  PROBLEM 1 ******\n")

# I chose to add "earnings" to make it easier to read and modify if prices
# change in the future.
while True:
    number_of_pieces = int(input("How many pieces? Enter any whole number or "
                                 "-999 to quit: \t"))
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
    print(f"At {number_of_pieces} pieces at ${earnings:,.2f} per piece, you've "
          f"earned ${total_earnings:,.2f}.")
    print()


input("\nPress any key to continue. . .")
# End of Problem 1

# Start Problem 2
print("******  PROBLEM 2 ******")

# I created functions because it's easier for me to make loops that way.
def validate_days():
    while True:
        number_of_days = float(input("Enter number of days:\t"))
        if number_of_days <= 0:
            print("Invalid number of days. Please re-enter.")
            print()
        elif number_of_days > 0:
            break

    return number_of_days

def validate_miles():
    while True:
        number_of_miles = float(input("Enter number of miles:\t"))
        if number_of_miles <= 0:
            print("Invalid number of miles. Please re-enter.")
            print()
        elif number_of_miles > 0:
            break

    return number_of_miles


def calc_cost(number_of_days, number_of_miles):
    cost_per_day = 29.99
    cost_per_mile = 0.35
    rental_fee = 1.75

    duration_cost = float(cost_per_day * number_of_days)
    mileage_cost = float(cost_per_mile * number_of_miles)
    total_cost = float(duration_cost + mileage_cost + rental_fee)

    return cost_per_day, cost_per_mile, rental_fee, duration_cost, mileage_cost, total_cost

def print_total(cost_per_day, number_of_days, duration_cost, cost_per_mile, number_of_miles, mileage_cost, rental_fee, total_cost):

    print(f"Car rental at ${cost_per_day} per day for "
          f"{number_of_days:,.0f} days is ${duration_cost:,.2f}."
          f"\nMileage at ${cost_per_mile} per mile for "
          f"{number_of_miles:,.0f} miles is ${mileage_cost:,.2f}"
          f"\nTotal cost including a fee of ${rental_fee} is "
          f"${total_cost:,.2f}")
    
number_of_days = validate_days()
number_of_miles = validate_miles()
cost_per_day, cost_per_mile, rental_fee, duration_cost, mileage_cost, total_cost = calc_cost(number_of_days, number_of_miles)
print_total(cost_per_day, number_of_days, duration_cost, cost_per_mile, number_of_miles, mileage_cost, rental_fee, total_cost)


input("\nPress any key to continue. . .")
# End of Problem 2

# Start Problem 3
print("******  PROBLEM 3 ******")

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
print(f"Month {month} is in {season}.")
print()


input("\nPress any key to exit. . .")
# End of Problem 3

# Start Problem 4
print("******  PROBLEM 4 ******")



input("\nPress any key to exit. . .")
# End of Problem 4

# Start Problem 5
print("******  PROBLEM 5 ******")



input("\nPress any key to exit. . .")
# End of Problem 5


# Start Bonus Problem
print("******  Bonus PROBLEM ******")



input("\nPress any key to exit. . .")
# End of Bonus Problem
