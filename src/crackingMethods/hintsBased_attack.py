"""
Piloted by Big Daddy Danny Ya Hearrrdddddd
    ****Speakers Notes****
    Hey guys! It's yourrrr boy Danny here bringing you a new and improved hints-based attack! This 
    is going to be my best attempt at this, as this is my very first time coding a project of this 
    nature! A first time for everything right?!?!? Hahaha glad we're having fun here! I haven't coded 
    in python in a while, so if my syntax is a little janky, then dont tell me because you'll hurt 
    my feelings! Haha lets get to work!


# Overview
    This is a hints-based method that attempts to crack a password using "hints" given from the user. 
    The idea is that a user will be prompted by the system to enter some basic information. The basic 
    information given by the user will then be used to generate possible passwords, in hopes of gaining 
    access. 

# NOTES
    As of 03/28/25, user input not yet implemented, hardcoded data will be used as hints for testing 
    purposes.
    As of now, possible hints will include, but not limited to: 


"""

import zipfile
import itertools

def hints_based_attack(zip_path: str, hints_dict: dict):
   """
   For now, gonna hardcode hints to pass into the method until we have user-input.
   Going to base it on [name, birth year, favorite color, favorite sport]
   """

   #example hints
   hints = ['sam', '2000', 'blue', 'football']

def generate_guesses(hints):
    guesses = set()

    # Add individual hints
    for hint in hints:
        guesses.add(hint)

    # Add 2-hint combos ---> order matters in this 
    for combo in itertools.permutations(hints, 2):
        guesses.add(''.join(combo))

    return list(guesses)
