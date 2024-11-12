## Writing to a File

def write_to_file(filename, data):
    """Write data to a file."""
    with open(filename, 'w') as file:
        file.write(data)
        print(f'Data written to {filename}')

write_to_file('example.txt', 'Hello, this is a test file!')