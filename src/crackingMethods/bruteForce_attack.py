import pyzipper
import itertools
import string
import io

def try_password(zip_bytes, password):
    """
    Attempts to extract ZIP with a given password.
    Returns True if successful, False otherwise.
    """
    try:
        zip_stream = io.BytesIO(zip_bytes)
        with pyzipper.AESZipFile(zip_stream, 'r') as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
            return True
    except:
        return False

def brute_force_attack(zip_path: str, max_length=5):
    """
    Attempts to brute-force the password for a ZIP file using a single thread
    """
    # Read the ZIP file once into memory
    with open(zip_path, 'rb') as f:
        zip_bytes = f.read()

    characters = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        print(f"[INFO] Trying passwords of length {length}...")

        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            if try_password(zip_bytes, password):
                print(f"[SUCCESS] Password found: {password}")
                return password

    print("[INFO] Password not found with brute force.")
    return None