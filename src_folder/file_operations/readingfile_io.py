## Reading from a File

def read_from_file(filename):
    """Read data from a file."""
    with open(filename, 'r') as file:
        return file.read()

data = read_from_file('example.txt')
print(data)