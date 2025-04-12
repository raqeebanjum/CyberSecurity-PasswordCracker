"""
# Overview
    This is a hints-based method that attempts to crack a password using "hints" given from the user. 
    The idea is that a user will be prompted by the system to enter some basic information. The basic 
    information given by the user will then be used to generate possible passwords, in hopes of gaining 
    access. 

# NOTES
    03/29/25 - hints_based_attack now calls get_user_input_hints_based_attack() to have the user input
    their own hints. It continues and then stops once user specifies. generate_guesses() needs to be 
    further modified to generate more than just ordered-paired guesses
"""

import pyzipper
import itertools
from utils import get_user_input_hints_based_attack


def hints_based_attack(zip_path: str):
    hints = get_user_input_hints_based_attack()
    guesses = generate_guesses(hints)

    with pyzipper.AESZipFile(zip_path, 'r') as zip_file:
        for password in guesses:
            try:
                zip_file.extractall(pwd=password.encode('utf-8'))
                print(f"[SUCCESS] Password found: {password}")
                return password
            except:
                pass  # Silent fail
        return None


def generate_guesses(hints): 
    guesses = set()

    # Add individual hints
    for hint in hints:
        guesses.add(hint)

    # Add 2-hint combos ---> order matters
    for combo in itertools.permutations(hints, 2): 
        guesses.add(''.join(combo))

    return list(guesses)