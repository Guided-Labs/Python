##  Filtering Rows

import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(f"Filtered DataFrame:\n{filtered_df}")