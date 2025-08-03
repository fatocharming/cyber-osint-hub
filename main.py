import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches and displays the HTTP headers of a given URL.
    
    Parameters:
    url (str): The URL from which to fetch the HTTP headers.
    
    Returns:
    dict: The HTTP headers returned by the server.
    """
    try:
        response = requests.get(url)
        # Return headers if request is successful
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes and prints key HTTP header information.
    
    Parameters:
    headers (dict): The HTTP headers to analyze.
    """
    if headers:
        print("HTTP Header Analysis:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        # Check for security-related headers
        security_headers = ['Content-Security-Policy', 'X-Frame-Options', 
                            'X-XSS-Protection', 'Strict-Transport-Security']
        print("\nSecurity Headers:")
        for header in security_headers:
            print(f"{header}: {headers.get(header, 'Not Present')}")

def main():
    """
    Main function to run the OSINT HTTP header analysis.
    """
    url = input("Enter the URL to analyze (e.g., http://example.com): ")
    parsed_url = urlparse(url)
    
    # Ensure the URL is well-formed
    if not parsed_url.scheme:
        url = 'http://' + url  # Default to HTTP if no scheme provided

    headers = get_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()
```