import socket
import sys

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = int(sys.argv[2]) if len(sys.argv) > 2 else 3000

with socket.socket() as sock:
    sock.settimeout(1)
    result = sock.connect_ex((host, port))

print("open" if result == 0 else "closed")
