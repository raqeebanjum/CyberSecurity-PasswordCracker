import zipfile
import zlib

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
    characters = string.ascii_lowercase + string.digits

    # Open the ZIP file for extraction attempts
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        # Get the first file in the archive to test passwords
        test_file = zip_file.namelist()[0]

        # Try passwords of increasing lengths from 1 to max_length
        for length in range(1, max_length + 1):
            print(f"Trying passwords of length {length}...")

            # Generate all possible character combinations of the current length
            for attempt in itertools.product(characters, repeat=length):
                password = ''.join(attempt)  # Convert tuple to string

                try:
                    # Try reading the first file with the current password
                    zip_file.open(test_file, pwd=password.encode('utf-8'))
                    
                    # If successful, try extracting to verify the password
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"Password found: {password}")
                    return True

                except (RuntimeError, zipfile.BadZipFile, zlib.error):
                    # If extraction fails, continue to the next attempt
                    continue

        # Return False if no password was found
        return False

    