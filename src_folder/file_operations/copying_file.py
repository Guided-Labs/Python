## Copying a File

import shutil

def copy_file(source, destination):
    """Copy a file from source to destination."""
    shutil.copy(source, destination)
    print(f"{source} has been copied to {destination}.")

copy_file('renamed_example.txt', 'copy_of_example.txt')