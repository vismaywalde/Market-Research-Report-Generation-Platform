import requests
from bs4 import BeautifulSoup

def get_market_data(url):
    # Make a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant data (you can modify the selector based on your target website's HTML structure)
        data = soup.find_all('div', class_='market-info')
        
        # Process the extracted data
        extracted_data = [item.get_text() for item in data]
        return extracted_data
    else:
        return None
