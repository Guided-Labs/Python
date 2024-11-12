## OS Module

import os

def list_directory_files(path):
    """List all files in the given directory."""
    return os.listdir(path)

directory_files = list_directory_files(os.getcwd())
print(f"Files in the current directory: {directory_files}")