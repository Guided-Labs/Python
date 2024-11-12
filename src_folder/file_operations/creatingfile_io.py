## Creating a New File

def create_file(filename):
    """Create a new file."""
    with open(filename, 'w') as file:
        file.write('This is a new file.')
    print(f"{filename} has been created.")

# Create a new file
create_file('example.txt')