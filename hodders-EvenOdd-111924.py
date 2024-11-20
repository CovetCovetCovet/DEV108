#!/usr/bin/env python3

"""
*********************************************************************    
*    Course:     DEV 108
*    Instructor: Phil Duncan
*    Term:       Fall 2024
*
*    Programmer: Sara Hodder
*    Assignment: DEV108 Coding Exercise: Even / Odd
*    
*    Description:   
* 
*    Revision    Date               Release Comment 
*    --------    ----------         -------------------------------------------- 
*    1.0         11/19/24           Initial submission
*    1
* 
"""

import time
import random

def is_even(n):
    return n % 2 == 0

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def collect_name():
    player_name = input("Enter your name:\t")
    print(f"Welcome {player_name}!")

    return player_name


def play_game(player_name):
    numlist = (1, 2, 3, 4)
    game = 0
    win = 0
    lose = 0
    game_outcome = []

    player_guess = input("Do you choose even or odd?")

    countdown(3)
    
    choice_1 = random(numlist)
    choice_2 = random(numlist)
    sum = choice_1 + choice_2

    even = is_even(sum) == True
    odd = is_even(sum) == False

    if even and player_guess.lower() == "even":
        print(f"{player_name}, you chose {player_guess}, the sum was {sum}, which is an even number, you Win!")
        win += 1
        game += 1
        game_outcome.append(game, win, player_guess)
    elif odd and player_guess.lower() == "odd":
        print(f"{player_name}, you chose {player_guess}, the sum was {sum}, which is an odd number, you Win!")
        win += 1
        game += 1
    elif even and player_guess.lower() == "odd":
        print(f"{player_name}, you chose {player_guess}, the sum was {sum}, which is an odd number, you Lose!")
        lose += 1
        game += 1
    elif odd and player_guess.lower() == "even":
        print(f"{player_name}, you chose {player_guess}, the sum was {sum}, which is an even number, you Lose!")
        lose += 1
        game += 1
    else:
        pass

        return sum


# Game uses Lists to store the Even Odd determination in correlation to game session number (first game, second game, etc. of game session).  HINT: Remember Lists can store Lists.
# Game compares stored player choice of Even Odd determination
# If determination matches player choice announce game outcome as required (A above. Required Game Session Result Display  modified for win)
# If determination is not a match for player choice announce game outcome as required (A above. Required Game Session Result Display )
# Store game outcome in correlation to game session number (first game, second game, etc. of game session).  HINT: Remember Lists can store Lists.


def main():
    again = "Y"
    while again.upper() == "N":
        print()
        print(input("Press any key to end program..."))
        print()
        break
    else:
        collect_name()
        play_game()

    print()
    again = input("Would you like to play again? y/n\t")
    print()


if __name__ == "__main__":
    main()