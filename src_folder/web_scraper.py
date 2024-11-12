import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    """Scrape the webpage and extract data."""
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the webpage content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract and return the webpage's title as an example
            title = soup.title.string
            return f"Webpage Title: {title}"
        else:
            return f"Failed to retrieve data. HTTP Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"


url = "https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/?ref=lbp"
print(scrape_webpage(url))