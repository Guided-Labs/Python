## Using Else Block

def read_file(file_name):
    """Read and return content from a file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: File not found."
    else:
        return content

print(read_file("example.txt")) 
print(read_file("non_existing_file.txt"))