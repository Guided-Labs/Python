## Using requests Library

import requests

def fetch_webpage(url):
    """Fetch and return the content of a webpage."""
    response = requests.get(url)
    return response.text

url = "https://www.example.com"
content = fetch_webpage(url)
print(content[:200])  # Print first 200 characters of the webpage content



## Using matplotlib Library

# import matplotlib.pyplot as plt

# def plot_graph():
#     """Plot a simple line graph."""
#     x = [1, 2, 3, 4, 5]
#     y = [2, 3, 5, 7, 11]
#     plt.plot(x, y)
#     plt.title('Simple Line Graph')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.show()

# plot_graph()



##  Using pandas Library

# import pandas as pd

# def create_dataframe():
#     """Create and return a pandas DataFrame."""
#     data = {
#         'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']
#     }
#     df = pd.DataFrame(data)
#     return df

# df = create_dataframe()
# print(df)