# Name: Yueheng Yuan
# Date: 01/22/2025

import csv

# Specify the path to the CSV file
file_path = "data/Iris.csv"

try:
    # Open the target CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        
        # Read and print each row in the CSV
        for row in reader:
            print(row)

except FileNotFoundError:
    print(f"Error: The csv file '{file_path}' was not found.")
except Exception as e:
    print(f"Error: {e}")
