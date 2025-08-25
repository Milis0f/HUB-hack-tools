import sys
import socket
from typing import List

COMMON_SUBDOMAINS: List[str] = [
    "www",
    "mail",
    "ftp",
    "test",
    "dev",
    "api",
]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python subfinder.py <domain>")
        return
    domain = sys.argv[1].strip()
    print(f"Checking subdomains for {domain}...")
    found = []
    for sub in COMMON_SUBDOMAINS:
        full = f"{sub}.{domain}"
        try:
            socket.gethostbyname(full)
            print(full)
            found.append(full)
        except socket.gaierror:
            continue
    if not found:
        print("No subdomains found")

if __name__ == "__main__":
    main()
