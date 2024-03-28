import pandas as pd

pd.set_option('display.max_rows', 30) # <--- ('', None) To see all rows
pd.set_option('display.max_columns', 30) # <--- ('', None) To see all columns

# Replace 'FILE_PATH' with the path to your actual CSV file
file_path = r'FILE_PATH'

# Read the CSV file
df = pd.read_csv(file_path)

# Print the content
print(df)
