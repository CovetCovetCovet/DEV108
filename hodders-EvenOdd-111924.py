#!/usr/bin/env python3

"""
********************************************************************************    
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
    player_name = input("Enter your name: ")
    print(f"Welcome {player_name}!")

    return player_name


def play_game(player_name):
    numlist = (1, 2, 3, 4)
    game = 0
    wins = game_outcome_guess.count("win")
    losses = game_outcome_guess.count("lose")
    game_outcome_guess = []

    print()
    guess = input("Do you choose even or odd?")
    print()

    countdown(3)
    
    num_1 = random(numlist)
    num_2 = random(numlist)
    sum = num_1 + num_2

    is_even(sum)

    if is_even == True:
        result = "even"
    else:
        result = "odd"

    if result == guess.lower():
        game += 1
        outcome = "win"
    else:
        game += 1
        outcome = "lose"

    game_outcome_guess.append([game, outcome, guess])

    print(f"{player_name}, you chose {guess}, the sum was {sum}, which is an {result} number, you {outcome}!"
          f"\nThat's {wins} wins and {losses} losses!")


    return sum, game_outcome_guess, game, wins, losses, outcome, guess


def recap_games(player_name, game_outcome_guess, game, wins, losses):
    win_rate = wins / game

    print(f"{player_name}, you played {game} games and won {wins}"
          f"\nThat is a {win_rate}% win rate!")

    for item in game_outcome_guess:
        print(item)

# Game 1 you won selecting Even, Game 2 you lost selecting Odd, Game 3 you won selecting Odd, Game 4 you won selecting Odd, Game 5 you lost selecting Even, Game 6 you lost selecting Odd, Game 7 you won selecting Even.
# Congratulations, you are a Grand Champion!

def main():
    again = "Y"
    while again.upper() == "N":
        print()
        recap_games()
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