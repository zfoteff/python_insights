#!/usr/bin/env python3
# Client Script

import socket

HOST = "147.222.165.1"
PORT = 6500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect_ex((HOST, PORT))

    data = input(": ")
    data = bytes(data, 'utf-8')
    while data is not "quit":
        s.sendall(data)
        print(str(s.recv(1024)))
        data = input(": ")
        data = bytes(data, 'utf-8')
        
