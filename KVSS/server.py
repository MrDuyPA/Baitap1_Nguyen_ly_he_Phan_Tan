import socket
import datetime

HOST = "0.0.0.0"
PORT = 12345

store = {}  # KV storage

def log(message):
    with open("server.log", "a") as f:
        f.write(f"{datetime.datetime.now()} {message}\n")

def handle_request(req):
    parts = req.strip().split()

    if not parts:
        return "400 BAD_REQUEST"

    cmd = parts[0].upper()

    if cmd == "PUT":
        if len(parts) < 3:
            return "400 BAD_REQUEST Missing key or value"
        key, value = parts[1], " ".join(parts[2:])
        created = key not in store
        store[key] = value
        return "201 CREATED" if created else "200 OK Updated"

    elif cmd == "GET":
        if len(parts) < 2:
            return "400 BAD_REQUEST Missing key"
        key = parts[1]
        if key in store:
            return f"200 OK {store[key]}"
        return "404 NOT_FOUND"

    elif cmd == "DEL":
        if len(parts) < 2:
            return "400 BAD_REQUEST Missing key"
        key = parts[1]
        if key in store:
            del store[key]
            return "204 NO_CONTENT"
        return "404 NOT_FOUND"

    elif cmd == "STATS":
        return f"200 OK count={len(store)}"

    else:
        return "400 BAD_REQUEST Unknown command"

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server running on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    req = data.decode()
                    log(f"REQ {addr}: {req.strip()}")
                    resp = handle_request(req)
                    log(f"RESP {addr}: {resp}")
                    conn.sendall(resp.encode() + b"\n")

if __name__ == "__main__":
    run_server()
