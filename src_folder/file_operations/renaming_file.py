## Renaming a File

import os

def rename_file(old_name, new_name):
    """Rename a file."""
    os.rename(old_name, new_name)
    print(f"{old_name} has been renamed to {new_name}.")

rename_file('renamed_example.txt', 'a_example.txt')