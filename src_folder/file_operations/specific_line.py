## Reading Specific Lines from a File

def read_specific_lines(filename, start_line, end_line):
    """Read specific lines from a file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines[start_line:end_line]

specific_lines = read_specific_lines('example.txt', 0, 2)
print(specific_lines)