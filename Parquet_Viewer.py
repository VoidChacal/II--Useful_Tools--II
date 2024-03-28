import pandas as pd

pd.set_option('display.max_rows', 30)  # Be cautious with this
pd.set_option('display.max_columns', 6)  # And this

# Replace 'FILE_PATH' with the path to your actual Parquet file
df = pd.read_parquet(r'FILE_PATH')

# Display the DataFrame
print(df)

