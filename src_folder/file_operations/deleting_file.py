## Deleting a File

import os
def delete_file(filename):
    """Delete a file if it exists."""
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")

delete_file('new_file.txt')