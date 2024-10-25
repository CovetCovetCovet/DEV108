#!/usr/bin/env python3

"""
*********************************************************************    
*    Course:     DEV 108
*    Instructor: Phil Duncan
*    Term:       Fall 2024
*
*    Programmer: 
*    Assignment: DEV108 Week Five Check In Exercise Part 1
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
print("******  PROBLEM 1 ******")
print()
sales_total = 0
while True:
    sale = input("Enter a decimal number or 'Done' to quit:\t")
    if sale.lower() == "done":
        break
    try:
        sale = float(sale)
        sales_total += sale
    except ValueError:
        print("Invalid input.")

if sales_total <= 0:
    total_com = sales_total * 0
    com_rate = "0%"
elif sales_total >= 0.01 and sales_total <= 499.99:
    total_com = sales_total * 0.05
    com_rate = "5%"
elif sales_total >= 500 and sales_total <= 999.99:
    total_com = sales_total * 0.1
    com_rate = "10%"
elif sales_total <= 1000:
    total_com = sales_total * 0.15
    com_rate = "15%"

total_earnings = sales_total + float(total_com)
    
print("**********************************************************************"
      f"\nYour sales total is ${sales_total:,.2f}. Your commission rate is {com_rate}."
      f"\nYour total commission is ${total_com:,.2f}."
      f"\nYour total earnings are ${total_earnings:,.2f}."
      "\n**********************************************************************")


input("\nPress any key to continue. . .")
# End of Problem 1

# Start Problem 2
print("******  PROBLEM 2 ******")
print()

another = "Y"
while another.upper() == "Y":
    planetary_body = int(input("Enter the position of a planetary body:\t\t"))
    match planetary_body:
        case "1":
            print(f"The object at position {planetary_body} is an inner planet.")
        case "2":
            print(f"The object at position {planetary_body} is an inner planet.")
        case "3":
            print(f"The object at position {planetary_body} is an inner planet.")
        case "4":
            print(f"The object at position {planetary_body} is an inner planet.")
        case "5":
            print(f"The object at position {planetary_body} is an outer planet.")
        case "6":
            print(f"The object at position {planetary_body} is an outer planet.")
        case "7":
            print(f"The object at position {planetary_body} is an outer planet.")
        case "8":
            print(f"The object at position {planetary_body} is an outer planet.")
        case "9":
            print(f"The object at position {planetary_body} is not a planet anymore.")
        case planetary_body if planetary_body >= 10:
            print(f"The object at position {planetary_body} is beyond Neptune, so not a planet.")
        case planetary_body if planetary_body <= 0:
            print(f"The object at position {planetary_body} is invalid.")
    another = input("Would you like to enter the position of another planetary body? (y/n)\t")

input("\nPress any key to continue. . .")
# End of Problem 2

# Start Problem 3
print("******  PROBLEM 3 ******")
print()

current_length = 0

string_entry = str(input("Enter a string:\t"))
while True:
    new_length = len(string_entry)
    if new_length > current_length:
        string_entry = str(input(f"That string is {len(string_entry)}. Good. Now enter a longer string:\t"))
    elif new_length <= current_length:
        print("Sadly, that was not longer than the previous string.")
        current_length = 0
        break

    current_length = new_length


input("\nPress any key to exit. . .")
# End of Problem 3