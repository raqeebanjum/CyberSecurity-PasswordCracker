import zipfile

def brute_force_attack(zip_path: str):
    
    
    # the method has to be able to generate every possible combination of characters based on this variable
    # I set it to 4 for now for easy testing, but we can increase it later
    max_length = 5
    """
        Should return the password if it's found, otherwise, it'll return none
        
    """
    