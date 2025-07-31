import socket
import requests

def get_ip_info(ip):
    """
    Fetches public information about the given IP address using ipinfo.io API.
    Returns a dictionary with the IP information.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response as a dictionary
    except requests.RequestException as e:
        print(f"Error fetching IP info: {e}")
        return None

def port_scanner(target, ports):
    """
    Scans the specified ports on the target host.
    Prints the status of each port (open/closed).
    """
    print(f"Scanning {target} for open ports...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout for the connection attempt
            result = sock.connect_ex((target, port))  # Try to connect to the port
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")  # Get IP from user
    ports_to_scan = [22, 80, 443, 8080]  # Common ports to scan
    ip_info = get_ip_info(target_ip)  # Fetch IP information

    if ip_info:
        print(f"IP Information: {ip_info}")  # Display IP info if successful

    port_scanner(target_ip, ports_to_scan)  # Perform port scan