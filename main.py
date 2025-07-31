import requests

def fetch_http_headers(url):
    """
    Fetches the HTTP headers from a specified URL.

    Args:
        url (str): The target URL to fetch headers from.

    Returns:
        dict: A dictionary of HTTP headers.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        # Ensure we get a successful response
        response.raise_for_status()
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes the fetched HTTP headers and extracts useful information.

    Args:
        headers (dict): The HTTP headers to analyze.

    Returns:
        dict: A dictionary with analysis results.
    """
    analysis = {
        'Content-Type': headers.get('Content-Type'),
        'Server': headers.get('Server'),
        'X-Powered-By': headers.get('X-Powered-By'),
        'Cache-Control': headers.get('Cache-Control'),
        'Strict-Transport-Security': headers.get('Strict-Transport-Security')
    }
    return analysis

def main():
    """
    Main function to input URL and display analyzed HTTP headers.
    """
    url = input("Enter the URL to analyze (e.g., https://example.com): ")
    headers = fetch_http_headers(url)
    
    if headers:
        print("\nFetched HTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        analysis = analyze_headers(headers)
        print("\nAnalyzed HTTP Headers:")
        for key, value in analysis.items():
            print(f"{key}: {value if value else 'Not available'}")

if __name__ == "__main__":
    main()
```