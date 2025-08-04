import requests

def fetch_http_headers(url):
    """
    Fetches the HTTP headers of a given URL and displays key information.
    
    Args:
        url (str): The target URL to fetch headers from.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.head(url)  # Perform a HEAD request to retrieve headers
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return {}

def analyze_headers(headers):
    """
    Analyzes and prints key HTTP header information.

    Args:
        headers (dict): The HTTP headers to analyze.
    """
    print("\n--- HTTP Headers Analysis ---")
    for header, value in headers.items():
        print(f"{header}: {value}")

    # Check for common security headers
    security_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Content-Type-Options']
    missing_headers = [h for h in security_headers if h not in headers]

    if missing_headers:
        print("\nWarning: Missing security headers:")
        for missing in missing_headers:
            print(f"- {missing}")

def main():
    """
    Main function to execute the OSINT tool.
    """
    target_url = input("Enter the URL to analyze (e.g., https://example.com): ")
    headers = fetch_http_headers(target_url)

    if headers:
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```