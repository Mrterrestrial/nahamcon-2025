#!/usr/bin/env python3
import socket

def main():
    host = "challenge.nahamcon.com"
    port = 32208
    with socket.create_connection((host, port)) as s:
        while True:
            # Receive data from the server
            data = s.recv(4096)
            if not data:
                break
            text = data.decode(errors="ignore")
            print(text, end="")

            # If we spot the flag in the output, stop
            if "flag{" in text.lower():
                break

            # Otherwise, send a newline to get the next chunk
            s.sendall(b"\n")

if __name__ == "__main__":
    main()
