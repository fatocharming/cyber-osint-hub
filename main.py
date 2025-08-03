import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches the HTTP headers from the specified URL.
    
    Args:
        url (str): The target URL to analyze.
    
    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {}

def analyze_headers(headers):
    """
    Analyzes and prints important HTTP header information.
    
    Args:
        headers (dict): The HTTP headers to analyze.
    """
    print("HTTP Header Analysis:")
    for header, value in headers.items():
        print(f"{header}: {value}")

    # Check for security-related headers
    security_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Content-Type-Options', 'X-Frame-Options']
    print("\nSecurity Headers:")
    for header in security_headers:
        if header in headers:
            print(f"{header} is present: {headers[header]}")
        else:
            print(f"{header} is missing!")

def main():
    """
    Main function to execute the OSINT script for HTTP headers.
    """
    target_url = input("Enter a URL to analyze (e.g., http://example.com): ")
    parsed_url = urlparse(target_url)

    # Ensure the URL has a scheme
    if not parsed_url.scheme:
        print("Please include the scheme (http or https) in the URL.")
        return

    headers = get_http_headers(target_url)
    if headers:
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```