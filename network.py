import socket
import subprocess
import platform


def check_internet():
    """
    Checks if the internet is available.
    """
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


def get_local_ip():
    """
    Returns the local IP address.
    """
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception:
        return "Unable to determine IP address"


def get_hostname():
    """
    Returns the system hostname.
    """
    return socket.gethostname()


def dns_lookup(domain):
    """
    Resolves a domain name to an IP address.
    """
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "Domain not found"


def ping_host(host):
    """
    Pings a host and returns the result.
    """
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr

    except Exception as e:
        return str(e)


if __name__ == "__main__":

    print("===== NETWORK DIAGNOSTICS =====")

    print("\nHostname:")
    print(get_hostname())

    print("\nLocal IP:")
    print(get_local_ip())

    print("\nInternet Connection:")
    if check_internet():
        print("Connected")
    else:
        print("Not Connected")

    domain = input("\nEnter a domain for DNS lookup (example: google.com): ")

    print("\nResolved IP:")
    print(dns_lookup(domain))

    host = input("\nEnter host to ping: ")

    print("\nPing Result:")
    print(ping_host(host))