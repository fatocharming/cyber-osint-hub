import requests

def fetch_http_headers(url):
    """
    Fetches HTTP headers from a given URL and returns them in a readable format.
    
    Parameters:
    url (str): The target URL to fetch headers from.
    
    Returns:
    dict: A dictionary containing HTTP headers.
    """
    try:
        response = requests.get(url)
        # Return the headers as a dictionary
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes the HTTP headers for common security-related headers.
    
    Parameters:
    headers (dict): HTTP headers to analyze.
    
    Returns:
    None: Prints out the analysis results.
    """
    security_headers = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'X-XSS-Protection',
        'Referrer-Policy'
    ]
    
    print("\n--- HTTP Header Analysis ---")
    for header in security_headers:
        value = headers.get(header, 'Not Present')
        print(f"{header}: {value}")

def main():
    """
    Main function to execute the script.
    Prompts user for a URL and fetches header information.
    
    Returns:
    None
    """
    url = input("Enter the URL to analyze (including http:// or https://): ")
    headers = fetch_http_headers(url)
    
    if headers:
        print("\nFetched HTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```