#!/usr/bin/env python3

"""
********************************************************************************    
*    Course:     DEV 108
*    Instructor: Phil Duncan
*    Term:       Fall 2024
*
*    Programmer: Sara Hodder
*    Assignment: DEV108 I/O
*    
*    Description:   
* 
*    Revision    Date               Release Comment 
*    --------    ----------         -------------------------------------------- 
*    1.0         12/12/24           Initial submission
*    1
* 
"""


import csv

FILENAME = "trips.csv"

def write_trip(mpg_list):
    with open(FILENAME, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(mpg_list)


def read_trip(mpg_list):
    with open(FILENAME, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            mpg_list.append(row)
    
    return mpg_list


def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    mpg_list = [['Distance', 'Gallons', 'MPG']]

    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        mpg_list.append([miles_driven, gallons_used, mpg])
        
        more = input("More entries? (y or n): ")
    
    write_trip(mpg_list)
    read_trip(mpg_list)
    
    print("Bye")

if __name__ == "__main__":
    main()

