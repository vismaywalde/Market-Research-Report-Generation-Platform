# marketresearch/data_fetcher.py

import requests
from bs4 import BeautifulSoup
from config import SERP_API_KEY  # Import your SerpApi key from the config file

def get_market_data_from_search(query):
    params = {
        "q": query,  # User's query
        "api_key": SERP_API_KEY,
        "engine": "google",  # Using Google search engine
    }
    
    # Make a request to SerpApi directly
    response = requests.get("https://serpapi.com/search", params=params)

    if response.status_code == 200:
        results = response.json()  # Get JSON response
        # Extract links to the top 5 results
        links = [result['link'] for result in results.get('organic_results', [])[:5]]

        # Scrape each link for market data
        market_data = []
        for link in links:
            scraped_data = scrape_page(link)
            if scraped_data:
                market_data.append(scraped_data)
        
        return market_data
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return []

def scrape_page(url):
    """Scrape content from a single page."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract relevant data (modify this based on the site's structure)
            paragraphs = soup.find_all('p')
            page_content = ' '.join([p.get_text() for p in paragraphs])
            return page_content
        else:
            return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
