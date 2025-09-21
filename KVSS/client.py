import socket
import sys

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected. Type commands (PUT/GET/DEL/STATS). Ctrl+C to quit.")
    for line in sys.stdin:
        s.sendall(line.encode())
        resp = s.recv(1024).decode()
        print(resp.strip())
