import os
from src.utils import validate_zip, display_menu, get_user_choice, list_zip_files
from src.config import *
from src.crackingMethods.dictionary_attack import dictionary_attack
from src.crackingMethods.bruteForce_attack import brute_force_attack
from src.crackingMethods.hintsBased_attack import hints_based_attack

def main():
    # letting the user pick a zip file, from all the zips in the input folder
    selected_file = list_zip_files()
    if not selected_file:
        print("No file selected. Exiting...")
        return

    # Zip file path(inside the input folder)
    zip_path = os.path.join(INPUT_FOLDER, selected_file)

    # validation to make sure it's password protected
    validation_result = validate_zip(zip_path)
    if validation_result:
        print(validation_result)
        return

    # loop that'll first display their options and then ask for the user choice for method of attack
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:  # Dictionary Attack
            dict_path = os.path.join('src', 'crackingMethods', 'wordLists', 'list1.txt')
            result = dictionary_attack(zip_path, dict_path)
            if result:
                print("Password cracking successful!")
                break
        
        elif choice == 2:  # Brute Force Attack
            result = brute_force_attack(zip_path)
            if result:
                print("Password cracking successful!")
                break
        
        elif choice == 3:  # Hints Based Attack
            result = hints_based_attack(zip_path)
            if result:
                print("Password cracking successful!")
                break
        
        elif choice == 0:  # Exit
            print("Exiting program...")
            break
        
        print("Password not found.")


if __name__ == "__main__":
    main()