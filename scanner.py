import pyfiglet
import sys
import socket
from datetime import datetime

# Banner
ascii_banner = pyfiglet.figlet_format("PORT SCAN PROJECT")
print(ascii_banner)

# Argument check
if len(sys.argv) != 2:
    print("Invalid amount of Argument")
    print("Usage: python scanner.py <target>")
    sys.exit()

# Resolve target
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

# Scan info
print("_" * 60)
print("Scanning Target IP:", target)
print("Scanning started at:", str(datetime.now()))
print("_" * 60)

# Port scanning
try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] TCP Port {port} is open")

        s.close()

except KeyboardInterrupt:
    print("\nExiting Port Scan Project!")
    sys.exit()

except socket.error:
    print("\nServer not responding!")
    sys.exit()
