import os
from zipfile import ZipFile, BadZipFile
from src.config import *

file_path = os.path.join(INPUT_FOLDER, INPUT_FILE)

def check_zip_exists():
    """Check if input.zip exists in input folder"""
    # making sure that input.zip is actually in the input folder
    return os.path.isfile(file_path)
    #pass

def is_password_protected():
    """Verify if ZIP is password protected"""
    # Making sure that the zip file is actually protected
    try: 
        with ZipFile(file_path) as zip_file:
            for file_info in zip_file.infolist():
                if file_info.flag_bits & 0x1:
                    print("This file is indeed encrpyted!")
                    return True
            print("This file is NOT password protected.")
            return False
    except BadZipFile: 
        return CORRUPTED_ZIP

            
    pass

def validate_zip():
    """Run all validation checks"""
    if not check_zip_exists():
        return(FILE_NOT_FOUND)
    if not is_password_protected():
        return (NOT_PASSWORD_PROTECTED)    
    pass

def display_menu():
    """Display method selection menu"""
    print("\nSelect a password cracking method:  ")
    print("Method 1. Dictionary Attack")
    print("Method 2. Brute Force Attack")
    print("Method 3. Hints Based Attack")
    print("Exit Program.")

    pass

def get_user_choice():
    """Get and validate user's method choice"""
    while True: 
        userChoice = input("Enter 1 for Dictionary Attack, 2 for Brute Force Attack, 3 for Hints-Based Attack and 4 to exit the program.")
        if userChoice in ['1', '2', '3', '4']:
            return int(userChoice)
        print("Thats an invalid choice. Please Try Again.")
   # pass