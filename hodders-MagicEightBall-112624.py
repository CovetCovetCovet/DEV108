#!/usr/bin/env python3

"""
********************************************************************************    
*    Course:     DEV 108
*    Instructor: Phil Duncan
*    Term:       Fall 2024
*
*    Programmer: Sara Hodder
*    Assignment: DEV108 Magic Eight Ball
*    
*    Description:   
* 
*    Revision    Date               Release Comment 
*    --------    ----------         -------------------------------------------- 
*    1.0         11/26/24           Initial submission
*    1
* 
"""

import random


def collect_name():
    print("Threads of Fate: The Witch's Prophecy")
    player_name = input("\nWho am I speaking with? ")
    print(f"Welcome, {player_name}, to the realm of the unknown. The spirits "
          "are listening...")

    return player_name


def play_game(questions):
    answers = ("The stars align in your favor", "The spirits whisper yes", 
               "Magic is on your side, and fate smiles upon you", 
               "The crystal ball glows with a clear yes", 
               "The cursed runes spell doom - no, the answer is not in your "
               "favor", "The answer lies in the void — a forbidding no", 
               "The cauldron bubbles with uncertainty", 
               "The fates are clouded; wait for the next full moon")

    question = input("\nAsk your question, yes or no, and we shall see what "
                     "fate reveals. ")
    
    response = random.choice(answers)
    print(f"{response}.")
    questions.append([question, response])

    return questions

def count_len(questions):
    count = len(questions)

    return count


def recap_games(player_name, count, questions):

    print(f"{player_name}, {count} questions you have spun into the cauldron, "
          f"and {count} answers have bubbled forth...")

    for item in questions:
        print(f"{item[0]} - {item[1]}.")


def main():
    again = "y"
    questions = []
    player_name = collect_name()
    while again.lower() == "y":
        play_game(questions)

        again = input("\nWill you stir the cauldron once more with a question, "
                      "or let the embers smolder in silence? (y/n)  ")

    print()
    count = count_len(questions)
    recap_games(player_name, count, questions)
    print("\nMay the moon guide your path, the stars light your way, and the "
          "magic within you always stay. Farewell, until our paths cross again!")
    print()
    

if __name__ == "__main__":
    main()