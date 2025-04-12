import os
from zipfile import ZipFile, BadZipFile
from config import *
from InquirerPy import inquirer


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
    choices = [
        {"name": "Dictionary Attack", "value": 1},
        {"name": "Brute Force Attack", "value": 2},
        {"name": "Hints Based Attack", "value": 3},
        {"name": "Exit", "value": 0},
    ]
    
    return inquirer.select(
        message="Select a password cracking method:",
        choices=choices,
    ).execute()

def get_user_input_hints_based_attack():
    """Collect user-provided hints for future hint-based attacks"""
    print("\nEnter any hints you think might be part of the password (names, dates, etc).")
    print("Type 'STOP' when you're done.\n")

    userHints = []
    count = 1

    try:
        while True:
            hint = input(f"Hint {count}: ").strip()
            if not hint:
                print("Hint cannot be empty. Try again.")
                continue
            if hint.upper() == "STOP":
                break
            userHints.append(hint)
            count += 1
    except KeyboardInterrupt:
        print("\n[INFO] Hint entry cancelled by user.")

    return userHints


def list_zip_files():
    """List all ZIP files with arrow-key selection"""
    zip_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.zip')]
    if not zip_files:
        print("No ZIP files found in the input folder.")
        return None

    choices = zip_files + ["Exit"]
    selected = inquirer.select(
        message="Choose a ZIP file to crack:",
        choices=choices,
    ).execute()

    return None if selected == "Exit" else selected