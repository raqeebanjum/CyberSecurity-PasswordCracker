"""
Dictionary Attack Implementation for Password Cracker (pyzipper-based, no failed prints)

### Overview:
This script attempts to crack the password of a password-protected ZIP file using a dictionary attack.
It reads passwords from a predefined dictionary file and attempts to extract the contents of the ZIP file.

### Features:
- Reads a list of common passwords from a dictionary file.
- Attempts to unlock the ZIP file using each password.
- Stops immediately if a correct password is found.

"""

import pyzipper

def dictionary_attack(zip_path, dict_path):
    """
    Attempts to crack a password-protected ZIP file using a dictionary attack.

    :param zip_path: Path to the password-protected ZIP file.
    :param dict_path: Path to the dictionary file containing common passwords.
    :return: The cracked password if found, otherwise None.
    """
    try:
        # Open the ZIP file in read mode
        with pyzipper.AESZipFile(zip_path, 'r') as zip_file:

            # Open the dictionary file and read passwords line by line
            with open(dict_path, 'r', encoding='utf-8') as dict_file:

                # Iterate through each password in the dictionary
                for password in dict_file:
                    try:
                        password = password.strip()

                        # Attempt to extract the ZIP file using the current password
                        zip_file.extractall(pwd=password.encode('utf-8'))
                        print(f"[SUCCESS] Password found: {password}")
                        return password

                    except KeyboardInterrupt:
                        print("\n[INFO] Interrupted by user. Stopping dictionary attack.")
                        return None
                    except:
                        pass  # Fail silently to avoid spam

    except FileNotFoundError:
        print("[ERROR] ZIP file or dictionary file not found. Check the file paths.")
    except pyzipper.BadZipFile:
        print("[ERROR] Invalid ZIP file. Make sure the file is a valid archive.")

    print("[INFO] Password not found in dictionary.")
    return None