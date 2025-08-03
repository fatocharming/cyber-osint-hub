import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetches HTTP headers for a given URL.

    Args:
        url (str): The URL to fetch headers from.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers to extract relevant information.

    Args:
        headers (dict): A dictionary of HTTP headers.

    Returns:
        None: Prints out analysis results.
    """
    if not headers:
        print("No headers to analyze.")
        return

    print("Analyzing HTTP Headers:")
    print(f"Server: {headers.get('Server', 'Not Provided')}")
    print(f"Content-Type: {headers.get('Content-Type', 'Not Provided')}")
    print(f"Content-Length: {headers.get('Content-Length', 'Not Provided')} bytes")
    print(f"Cache-Control: {headers.get('Cache-Control', 'Not Provided')}")
    print(f"X-Content-Type-Options: {headers.get('X-Content-Type-Options', 'Not Provided')}")

def main():
    """
    Main function to execute the OSINT HTTP header analysis script.
    
    Asks the user for a URL and fetches its HTTP headers.
    """
    url = input("Enter the URL to analyze (e.g., https://example.com): ")
    parsed_url = urlparse(url)
    
    # Ensure the URL is properly formatted
    if not parsed_url.scheme:
        print("Invalid URL. Please include the scheme (e.g., http:// or https://)")
        return

    headers = fetch_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()