import zipfile

def hints_based_attack(zip_path: str, hints_dict: dict):
    """"
    I'm not sure sure what the arguments would be for this functions
    Maybe we could take in a dictionary, where the keys would be the type of hint
    Like names, dates, words, numbers, etc, and the values would obviously be the hitns themselves
    
    It would return the password if it's found, otherwise, it would return None
    
    """
