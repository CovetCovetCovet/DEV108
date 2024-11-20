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


def play_game(player_name, game_outcome_guess, game, wins, losses):
    numlist = (1, 2, 3, 4)

    print()
    guess = input("Do you choose even or odd? ")
    print()

    countdown(3)
    
    num_1 = random.choice(numlist)
    num_2 = random.choice(numlist)
    sum = num_1 + num_2

    
    if is_even(sum) == True:
        result = "even"
    else:
        result = "odd"

    if result == guess.lower():
        game += 1
        wins += 1
        outcome = "win"
    else:
        game += 1
        losses += 1
        outcome = "lose"

    game_outcome_guess.append([game, outcome, guess])


    print(f"{player_name}, you chose {guess}, the sum was {sum}, which is an {result} number, you {outcome}!"
          f"\nThat's {wins} wins and {losses} losses!")

    return game_outcome_guess, game, wins, losses


def recap_games(player_name, game_outcome_guess, game, wins):
    win_rate = float((wins / game) * 100)

    print(f"{player_name}, you played {game} games and won {wins}."
          f"\nThat is a {win_rate:.0f}% win rate!")

    for item in game_outcome_guess:
        print(f"Game {item[0]} you {item[1]} selecting {item[2]}.")

    if win_rate >= 50:
        print("\nCongratulations, you are a Grand Champion!")
    else:
        print("\nRelaunch the game to try again to become a Grand Champion.")

def reset_game(game, wins, losses, game_outcome_guess):
    game = 0
    wins = 0
    losses = 0
    game_outcome_guess = []

    return game, wins, losses, game_outcome_guess


def main():
    again = "y"
    player_name = collect_name()
    game = 0
    wins = 0
    losses = 0
    game_outcome_guess = []
    while again.lower() == "y":
        game_outcome_guess, game, wins, losses = play_game(player_name, game_outcome_guess, game, wins, losses)

        print()
        again = input("Would you like to play again? y/n  ")
        print()

    print()
    recap_games(player_name, game_outcome_guess, game, wins)
    print()
    game, wins, losses, game_outcome_guess = reset_game(game, wins, losses, game_outcome_guess)
    

if __name__ == "__main__":
    main()