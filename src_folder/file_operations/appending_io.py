## Appending to a File

def append_to_file(filename, data):
    """Append data to a file."""
    with open(filename, 'a') as file:
        file.write(data)
        print(f"Data appended to {filename}")

append_to_file('example.txt', '\nThis line has been appended.')