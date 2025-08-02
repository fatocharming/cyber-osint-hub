import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_http_headers(url):
    """Fetches HTTP headers from the specified URL."""
    try:
        response = requests.head(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def get_meta_data(url):
    """Extracts metadata from the HTML of the specified URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title and description
        title = soup.title.string if soup.title else "N/A"
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else "N/A"
        
        return {
            'title': title,
            'description': description_content
        }
    except requests.RequestException as e:
        print(f"Error fetching metadata: {e}")
        return None

def analyze_url(url):
    """Analyzes a URL by fetching HTTP headers and metadata."""
    print(f"Analyzing URL: {url}")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please provide a complete URL, including the scheme (http/https).")
        return
    
    # Fetch and print HTTP headers
    headers = get_http_headers(url)
    if headers:
        print("\nHTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
    
    # Fetch and print metadata
    metadata = get_meta_data(url)
    if metadata:
        print("\nMetadata:")
        print(f"Title: {metadata['title']}")
        print(f"Description: {metadata['description']}")

if __name__ == "__main__":
    # Example usage
    url_to_analyze = input("Enter a URL to analyze (e.g., https://example.com): ")
    analyze_url(url_to_analyze)
```