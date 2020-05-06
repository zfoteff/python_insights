#!/usr/bin/env python3
# Host Script

import socket

HOST = "147.222.165.1"
PORT = 6500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                conn.send(b"Error")
                break

            print (str(data))
            conn.send(b"Complete")

        print("Goodbye")

            
