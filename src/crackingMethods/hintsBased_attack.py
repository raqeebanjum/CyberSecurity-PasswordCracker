"""
# Overview
    This is a hints-based method that attempts to crack a password using "hints" given from the user. 
    The idea is that a user will be prompted by the system to enter some basic information. The basic 
    information given by the user will then be used to generate possible passwords, in hopes of gaining 
    access. 

# NOTES
    04/08/25 - generate_guesses now provides all the possible permutations, and now will add in a dash
    '-' or underscore '_' for more possibilities. Also plays around with capitalization. 

"""

import zipfile
import itertools
from src.utils import get_user_input_hints_based_attack


def hints_based_attack(zip_path: str):
   hints = get_user_input_hints_based_attack()
   guesses = generate_guesses(hints)

   # ripped logic from dictionary_attack
   # instead of reading from a file, loop through the list of guesses
   with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for password in guesses:
            try:
                zip_file.extractall(pwd=password.encode('utf-8'))
                print(f"[SUCCESS] Password found: {password}")
                return password
            except:
                print(f"[FAILED] Trying: {password}")
        return None


# generates guesses to test with hardcoded information
def generate_guesses(hints): 
    guesses = set()

    # Add individual hints
    for hint in hints:
        guesses.add(hint)

    """
        So this itertools.permutations tool I found online - it'll actually generate all
        the ordered pairs we could have using the values in hints. So like ['sam', 'football']
        would become 'samfootball' as a potential password guess. Not sure if it works yet.
    """
    for r in range(2, len(hints) + 1):
        for combo in itertools.permutations(hints, r):
            base = ''.join(combo)
            guesses.add(base)

            guesses.add('_'.join(combo)) # With underscores
            guesses.add('-'.join(combo)) # With dashes
            guesses.add(''.join([word.capitalize() for word in combo])) # Capitalized style

    # should return all single hints + the permutations of paired hints
    return list(guesses)
    
