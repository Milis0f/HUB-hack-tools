import sys
import socket
from typing import List

def scan_ports(host: str, start: int, end: int) -> List[int]:
    open_ports = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python portscan.py <host> <start_port> <end_port>")
        return
    host = sys.argv[1]
    try:
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    except ValueError:
        print("Ports must be integers")
        return
    if start < 0 or end < 0 or start > end:
        print("Invalid port range")
        return
    print(f"Scanning {host} from port {start} to {end}...")
    open_ports = scan_ports(host, start, end)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found")

if __name__ == "__main__":
    main()
