## Reading CSV Files

import csv

def read_csv_file(filename):
    """Read a CSV file."""
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

read_csv_file('sample.csv')
