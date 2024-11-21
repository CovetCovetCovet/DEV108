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


# Functional Requirement (Player point of view)
# App presents a welcome message and asks player for their name.
# App greets the player by name and asks for their yes or no question.
# Player enters their question in the app.
# App responds by randomly selecting one of the eight answers and displays it to the player.
# App asks player if they have another question.
# If the player answers yes they want to ask another question, repeat steps 2 through 5.
# Note: After the first question address the player by name without the greeting. They have already been greeted the first time in Step 2.
# If the player answers no they do not want to ask another question, display the following.
# Number of questions asked.
# A list of the questions asked and their corresponding answers.
# A cheery farewell message.
# User Experience. 
# Use the example below to base your player interaction.
# As long as the spirit of the interaction matches the example below, you are free to be as creative with your messages as you want.
# You may use the traditional Eight ball questions or make up your own set of questions.  Unleash your creativity and have fun!

# Compose a series of eight (8) responses that a fortune teller might answer to someone asking yes or no questions.  (Let your own creative impulses be your guide as to the answers you make.)

# Store the Answers in a Tuple.
# Use a randomizer to select one answer per question to display to the player.
# Store the player questions in a List.
# Use len() to determine the number of times the player asks a question.
# Use Ternary Operator for all binary decisions.  
# Use a post condition loop to repeat until the player chooses not to continue.
# When the player chooses not to continue:
# Present a listing of the questions and corresponding answers as shown in the Example UX.
# Present a cheery farewell message of your creation.
# All user input shall be case insensitive.
# Use only one print() statement for multi line output.
# Follow all PEP-8 standards.
# Grammar and spelling count.  Be attentive to the details.

# YES: 
# It is certain
# Yes definitely
# Outlook good
# Signs point to yes

# MAYBE: 
# Ask again later
# Cannot predict now

# NO: 
# Don't count on it
# Very doubtful