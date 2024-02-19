import csv
import shutil

def sum_second_column(csv_file, has_header=True):
    total = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        if has_header:
            next(reader)  # Skip the header row
        for row in reader:
            total += float(row[1])
    return total

# Usage example
csv_file = 'xx.csv'
result = sum_second_column(csv_file, has_header=False)
print(f"The sum of the second column in {csv_file} is: {result}")  # Added closing parenthesis
source_file = '/home/pgmabv/pyproblems/cop1.py'
destination_file = '/home/pgmabv/pyproblems/cop1_copy.py'

shutil.copyfile(source_file, destination_file)
import pandas as pd

def sum_all_numeric_columns(csv_file, has_header=True):
    df = pd.read_csv(csv_file, header=None if not has_header else 'infer')
    total = df.select_dtypes(include='number').sum().sum()
    return total

# Usage example
csv_file = 'xx.csv'
result = sum_all_numeric_columns(csv_file, has_header=False)
print(f"The sum of all numeric columns in {csv_file} is: {result}")