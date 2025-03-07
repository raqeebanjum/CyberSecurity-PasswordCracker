import zipfile

def brute_force_attack(zip_path: str):
    
    #Danny and Branson
    #researching best way. 
    # the method has to be able to generate every possible combination of characters based on this variable
    # I set it to 4 for now for easy testing, but we can increase it later
    max_length = 5

    """
        Should return the password if it's found, otherwise, it'll return none
        
    """


import itertools
import string

def brute_force_attack(zip_path: str, max_length=5):
    """
    Attempts to brute-force the password for a ZIP file by trying every 
    possible combination of lowercase letters and digits up to max_length.
    
    :param zip_path: Path to the ZIP file.
    :param max_length: Maximum password length to attempt.
    :return: True if the password is found, otherwise False.
    """

    # Define the set of characters to use in the brute-force attack
    characters = string.ascii_lowercase + string.digits  # 'abcdefghijklmnopqrstuvwxyz0123456789'

    # Open the ZIP file for extraction attempts
    with zipfile.ZipFile(zip_path, 'r') as zip_file:

        # Try passwords of increasing lengths from 1 to max_length
        for length in range(1, max_length + 1):

            # Generate all possible character combinations of the current length
            for attempt in itertools.product(characters, repeat=length):
                password = ''.join(attempt)  # Convert tuple to string

                try:
                    # Try extracting the ZIP file with the current password
                    zip_file.extractall(pwd=password.encode())
                    
                    # If extraction is successful, print the password and return True
                    print(f"Password found: {password}")
                    return True

                except (RuntimeError, zipfile.BadZipFile):
                    # If extraction fails, continue to the next attempt
                    continue

    # Return False if no password was found
    return False

    