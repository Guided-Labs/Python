## Requests Module

import requests

def fetch_webpage_content(url):
    """Fetch and return the content of a webpage."""
    response = requests.get(url)
    return response.text

content = fetch_webpage_content('https://w3schools.com/python/demopage.htm')
print(content)