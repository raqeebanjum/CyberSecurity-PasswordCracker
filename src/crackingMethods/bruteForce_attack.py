import pyzipper
import itertools
import string
import threading
from concurrent.futures import ThreadPoolExecutor
import io

def try_password(zip_bytes, password, found_event, result_holder):
    """
    Attempts to extract ZIP with a given password.
    Exits early if another thread finds the password.
    """
    if found_event.is_set():
        return

    try:
        zip_stream = io.BytesIO(zip_bytes)
        with pyzipper.AESZipFile(zip_stream, 'r') as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
            found_event.set()
            result_holder.append(password)
    except:
        pass  # Ignore failed attempts


def brute_force_attack(zip_path: str, max_length=5, max_threads=8):
    """
    Attempts to brute-force the password for a ZIP file using parallel threads.

    """
    # Read the ZIP file once into memory
    with open(zip_path, 'rb') as f:
        zip_bytes = f.read()

    characters = string.ascii_lowercase + string.digits
    found_event = threading.Event()
    result_holder = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for length in range(1, max_length + 1):
            if found_event.is_set():
                break
            print(f"[INFO] Trying passwords of length {length}...")

            for attempt in itertools.product(characters, repeat=length):
                if found_event.is_set():
                    break

                password = ''.join(attempt)
                executor.submit(try_password, zip_bytes, password, found_event, result_holder)

    if result_holder:
        print(f"[SUCCESS] Password found: {result_holder[0]}")
        return result_holder[0]
    else:
        print("[INFO] Password not found with brute force.")
        return None