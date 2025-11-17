import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    """
    Scrape a website and extract useful information.
    
    Args:
        url (str): The website URL to scrape
    
    Returns:
        dict: Dictionary containing extracted information
    """
    try:
        # Fetch the webpage
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract information
        data = {
            'url': url,
            'title': soup.title.string if soup.title else 'No title found',
            'headings': [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])],
            'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')[:5]],
            'links': [urljoin(url, a.get('href', '')) for a in soup.find_all('a')[:10]],
            'images': [urljoin(url, img.get('src', '')) for img in soup.find_all('img')[:5]]
        }
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def display_results(data):
    """Display scraped data in a readable format."""
    if not data:
        return
    
    print(f"\n{'='*50}")
    print(f"Website: {data['url']}")
    print(f"Title: {data['title']}")
    print(f"\nHeadings: {len(data['headings'])} found")
    for heading in data['headings'][:5]:
        print(f"  - {heading}")
    print(f"\nLinks: {len(data['links'])} found")
    for link in data['links'][:5]:
        print(f"  - {link}")
    print(f"{'='*50}\n")

def main():
    print("Welcome to the Web Scraper!")
    url = input("Enter a website URL: ").strip()
    
    if not url:
        print("No URL provided.")
        return
    
    # Add http:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print("Scraping website...")
    data = scrape_website(url)
    display_results(data)

if __name__ == "__main__":
    main()