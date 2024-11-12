## Checking if a File Exists

import os

def check_file_exists(filename):
    """Check if a file exists."""
    if os.path.isfile(filename):
        print(f"{filename} exists.")
    else:
        print(f"{filename} does not exist.")

check_file_exists('example.txt')