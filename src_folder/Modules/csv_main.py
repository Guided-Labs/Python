## CSV Module

import csv

def create_sample_csv(file_name):
    """Create a sample CSV file for testing."""
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 30, "New York"])
        writer.writerow(["Bob", 25, "Los Angeles"])
        writer.writerow(["Charlie", 35, "Chicago"])


def read_csv(file_name):
    """Read and print contents of a CSV file."""
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

create_sample_csv('sample.csv')

read_csv('sample.csv')