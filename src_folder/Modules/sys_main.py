## Sys Module

import sys

def get_python_version():
    """Get the version of Python being used."""
    return sys.version

python_version = get_python_version()
print(f"Python version: {python_version}")
