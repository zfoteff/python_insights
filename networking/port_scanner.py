#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
from contextlib import closing

remoteServerIP = input("Enter IP Addr to Scan: ")

print("-"*45)
print("\tPlease Wait... Scanning ")
print("-"*45)

start = datetime.now()

try:
    for port in range (1, 1027):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            result = s.connect_ex((remoteServerIP, port))

            if result == 0:
                # connection found
                print ("[+] Port %d:\tOpen"%(port))

            else:
                # No connection found
                print ("[-] Port %d:\tClosed"%(port))

except KeyboardInterrupt:
    print ("\n\tTerminating Scan ...")
    sys.exit()

except socket.error:
    print("\n\tCould not connect to server. Terminating ...")
    sys.exit()

end = datetime.now()
t = float(end - start)
print ("Scan completed in %.3f seconds"%(t))
