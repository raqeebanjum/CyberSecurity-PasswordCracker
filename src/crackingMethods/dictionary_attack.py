"""
Dictionary Attack Implementation for Password Cracker

### Overview:
This script attempts to crack the password of a password-protected ZIP file using a dictionary attack.
It reads passwords from a predefined dictionary file and attempts to extract the contents of the ZIP file.

### Features:
- Reads a list of common passwords from a dictionary file.
- Attempts to unlock the ZIP file using each password.
- Tracks and displays progress for each password attempt.
- Stops immediately if a correct password is found.

### Future Enhancements:
- Implement a variation generator (e.g., replace 'e' with '3', 'o' with '0', etc.).
- Add logging functionality to track unsuccessful attempts.
- Improve efficiency by using multi-threading or multiprocessing.

"""

import zipfile

def dictionary_attack(zip_path, dict_path):
    """
    Attempts to crack a password-protected ZIP file using a dictionary attack.
    
    :param zip_path: Path to the password-protected ZIP file.
    :param dict_path: Path to the dictionary file containing common passwords.
    :return: The cracked password if found, otherwise None.
    """
def dictionary_attack(zip_path, dict_path):
    """
    Attempts to crack a password-protected ZIP file using a dictionary attack.
    
    :param zip_path: Path to the password-protected ZIP file.
    :param dict_path: Path to the dictionary file containing common passwords.
    :return: The cracked password if found, otherwise None.
    """
    try:
        # Open the ZIP file in read mode
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            
            # Open the dictionary file and read passwords line by line
            with open(dict_path, 'r', encoding='utf-8') as dict_file:
                
                # Iterate through each password in the dictionary
                for password in dict_file:
                    try:
                        password = password.strip()  # Remove any leading/trailing whitespace
                        
                        # Attempt to extract the ZIP file using the current password
                        zip_file.extractall(pwd=password.encode('utf-8'))
                        print(f"[SUCCESS] Password found: {password}")
                        return password  # Stop if password is found
                    except KeyboardInterrupt:
                        print("\n[INFO] Interrupted by user. Stopping dictionary attack.")
                        return None
                    except:
                        # If extraction fails, the password is incorrect
                        print(f"[FAILED] Trying: {password}")

    except FileNotFoundError:
        print("[ERROR] ZIP file or dictionary file not found. Check the file paths.")
    except zipfile.BadZipFile:
        print("[ERROR] Invalid ZIP file. Make sure the file is a valid archive.")
    
    print("[INFO] Password not found in dictionary.")
    return None  # Return None if password was not found

# Example Usage (Modify paths accordingly before running)
if __name__ == "__main__":
    zip_path = "protected.zip"  # Replace with actual ZIP file path
    dict_path = "common_passwords.txt"  # Replace with actual dictionary file path
    
    result = dictionary_attack(zip_path, dict_path)
    if result:
        print("Cracking successful!")
    else:
        print("Password not found.")
