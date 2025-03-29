import os
from zipfile import ZipFile, BadZipFile
from src.config import *

def is_password_protected(file_path):
    """Verify if ZIP is password protected"""
    # Making sure that the zip file is actually protected
    try: 
        with ZipFile(file_path) as zip_file:
            for file_info in zip_file.infolist():
                if file_info.flag_bits & 0x1:
                    return True
            return False
    except BadZipFile: 
        return CORRUPTED_ZIP

def validate_zip(file_path):
    """Run validation check for password protection only, since we know that the zip will always exist"""
    if not is_password_protected(file_path):
        return NOT_PASSWORD_PROTECTED

def display_menu():
    """Display method selection menu"""
    print("\nSelect a password cracking method:")
    print("1. Dictionary Attack")
    print("2. Brute Force Attack")
    print("3. Hints Based Attack")
    print("0. Exit")

def get_user_choice():
    """Get and validate user's method choice"""
    while True:
        userChoice = input("Enter your choice (1-4): ")
        if userChoice in {'0', '1', '2', '3'}:
            return int(userChoice)
        print("Invalid choice. Try again.")

def get_user_input_hints_based_attack():
    """Collect user-provided hints for future hint-based attacks"""
    userHints = {}
    count = 1
    
    while True:
        hint = input(f"Hint {count}: ").strip()
        if hint.upper() == "STOP":
            break
        userHints[count] = hint
        count += 1

    return userHints

def list_zip_files():
    """List all ZIP files in the input folder and let user select one"""
    zip_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.zip')]
    if not zip_files:
        print("No ZIP files found in the input folder.")
        return None
    
    print("\nAvailable ZIP files:")
    for idx, file in enumerate(zip_files, 1):
        print(f"{idx}. {file}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the ZIP file you want to crack (or 0 to exit): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(zip_files):
                return zip_files[choice - 1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")