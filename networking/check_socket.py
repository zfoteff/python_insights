#!/usr/bin/env python3
"""
Program takes command line arguments to create range of ports to check
and record an ip address. Program then checks each port of the target
ip and returns whether or not the port is open
"""
import sys
import socket
from contextlib import closing

"""
    pre:  host ip exists and port exists for host
    post: returns a string that tells user whether port is open
"""
def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        result = s.connect_ex((host, port))
        if result == 0:
            print ("Port "+str(port)+" is open")
        else:
            print (str(port)+" closed, returned: "+str(result))

def main():
    ip = sys.argv[1]
    port_range_start = int(sys.argv[2])
    port_range_end = int(sys.argv[3])
    counter = port_range_start

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    #--- Start of check loop
    while counter < port_range_end:
        check_socket(sys.argv[1], counter)
        counter += 1
    #--- End of check loop

if __name__ == '__main__':
    main()
