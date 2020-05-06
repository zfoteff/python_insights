#!/usr/bin/env python3

"""
    Program uses socket module to find first availible port and creates
    a connection with the port 
"""

import sys
import socket
from contextlib import closing


PORT_RANGE_START    = int(sys.argv[1])
PORT_RANGE_END      = int(sys.argv[2])
HOST                = sys.argv[3]


"""
    Pre:    port exists for host ip
    Post:   0 is returned if the port is closed, otherwise the open port
            is returned
"""
def connect_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        result = s.connect_ex((host, port))

        if result == 0:
            # connection found
            print ("Found connection at port "+str(port))
            return port

        else:
            return 0

def main():
    counter = PORT_RANGE_START
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    print ("------------------------------------------------------")
    print ('\nAttempting to connect to host: '+str(HOST)+" ...\n\n")

    # -- Start of connection attempt loop
    while counter < PORT_RANGE_END:
        result = connect_socket(HOST, counter)

        if result == 0:
            # continue searching for open ports until loop ends
            counter += 1
            continue

        else:
            # connect s to the open port
            s.connect((HOST, result))
            print('Connected\n')
            print ("------------------------------------------------------\n")
            sys.exit()
    # -- End of connection attempt loop

    print("Unable to find connection.\nTerminating program\n")
    print ("------------------------------------------------------\n")

if __name__ == '__main__':
    main()
