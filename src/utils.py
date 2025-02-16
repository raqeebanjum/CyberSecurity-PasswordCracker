import os
from zipfile import ZipFile, BadZipFile
from src.config import *

def check_zip_exists():
    print("This one should see if input.zip actually exists")
    

def is_password_protected():
    print("This should see if zip input.zip is actually protected")
    print("there isnt' a reason to try to crack it if it's not even password protected")
    
def validate_zip():
    print("Combine the previous checks, to make it easy to call in main")