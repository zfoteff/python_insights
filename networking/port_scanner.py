#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
from contextlib import closing

socket.setdefaulttimeout(.001)
remoteServerIP = input("Enter IP Addr to Scan: ")

print("-"*45)
print("\tPlease Wait... Scanning ")
print("-"*45)

start = datetime.now()

try:
    for port in range (1, 1023):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            result = s.connect_ex((remoteServerIP, port))

            if result == 0:
                # connection found
                print ("[+] Port %d: \tOpen"%(port))

            else:
                # No connection found
                print ("[-] Port %d: \tClosed"%(port))

except KeyboardInterrupt:
    print ("\n\tTerminating Scan ...")
    sys.exit()

except socket.error:
    print("\n\tCould not connect to server. Terminating ...")
    sys.exit()

end = datetime.now()
t = (end - start)
t = t.seconds
print ("Scan completed in %d seconds"%(t))
