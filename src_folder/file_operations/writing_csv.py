## Writing CSV Files

import csv

def write_csv_file(filename, data):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        print(f'Data written to {filename}')

data_to_write = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]
write_csv_file('output.csv', data_to_write)