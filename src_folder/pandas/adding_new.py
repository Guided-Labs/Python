## Adding a New Column

import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print(f"DataFrame with Salary Column:\n{df}")