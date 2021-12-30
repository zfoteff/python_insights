import socket
import time
import colorama
from contextlib import closing

colorama.init()

socket.setdefaulttimeout(0.005)

def check_port(ip, port_num):
    results = []
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            result = s.connect_ex((ip, port_num))

            if result == 0:
                #   Connection found
                print (colorama.Fore.GREEN+f"[+] Port {port_num}: \tOpen")
                results.append(port_num)

            else:
                #   No Connection found
                print (colorama.Fore.RED+f"[-] Port {port_num}: \tClosed")

    except socket.error:
        print ("\tUnable to connect to server. Terminating ...")
        return

def check_port_range(ip, port_start, port_end):
    try:
        for port in range(port_start, port_end):
            check_port(ip, port)

    except KeyboardInterrupt:
        print (colorama.Fore.WHITE+"\tTerminating Scan ...\n")
        return

def main ():
    hostIP = input("Enter IP Addr. to Scan: ")
    while True:
        print ("-"*45)
        try:
            # Prompts user with three choices of scans and the option to quit
            choice = int(input("\tWhat would you like to scan?"
                +"\n\t[1]\tCommon Ports"
                +"\n\t[2]\tAll Registered Ports"
                +"\n\t[3]\tSpecific Port"
                +"\n\t[4]\tSpecific Range of Ports"
				+"\n\t[5]\tEnter new IP Address"
                +"\n\t[6]\tQuit\n: "))

            #   User input checking with try loop and while loop
            while choice < 1 or choice > 6:
                choice = int(input("\tPlease select one of the numbered options above\n: "))

        except ValueError:
            #   User enters a character other than an integer
            choice = int(input("\tPlease select one of the numbered options above\n: "))


        if choice == 1:
            #   Scan all common ports 0-1023 on the host
            start = time.time()
            check_port_range(hostIP, 0, 1024)
            t = (time.time() - start)
            print(colorama.Fore.WHITE+"\tScanned 1024 ports in %.3f seconds"%(t))

        elif choice == 2:
            #   Scan all 49151 registered logical ports on the host
            start = time.time()
            check_port_range(hostIP, 0, 49151)
            t = (time.time() - start)
            print(colorama.Fore.WHITE+"\tScanned 49152 ports in %.3f seconds"%(t))

        elif choice == 3:
            #   Scan specific port
            try:
                port_choice = int(input("\tSelect a port to scan\n: "))

                while port_choice < 0 or port_choice >= 65535:
                    port_choice = int(input("\tSelect a port in the range [0, 65535]\n:"))

            except ValueError:
                # User enters a character other than an integer
                port_choice = int(input("\tPlease enter an integer in the range [0, 49151]\n:"))

            start = time.time()
            check_port(hostIP, port_choice)
            t = (time.time() - start)
            print (colorama.Fore.WHITE+"\tScanned port %d in %.5f seconds"%(port_choice, t))

        elif choice == 4:
            #   Scan user defined range of options
            try:
                start_port = int(input("Starting port: "))

                #   Ensure 0 <= start < 49150
                while start_port < 0 or start_port > 49150:
                    start_port = int(input("\tPlease select a port in the range [0, 49150]\n: "))
            except ValueError:
                #   User enters a character other than an integer
                start_port = int(input("\tPlease enter an integer in the range [0, 49151]\n: "))

            try:
                end_port = int(input("End port: "))

                #   Ensure start <= end < 49151
                while end_port <= start_port or end_port > 49151:
                    end_port = int(input("\tPlease select a port in the range [start_port+1, 49151]\n: "))
            except ValueError:
                #   User enters a character other than an integer
                end_port = int(input("\tPlease enter an integer in the range [start_port+1, 49151]\n: "))

            start = time.time()
            check_port_range(hostIP, start_port, end_port+1)
            t = (time.time() - start)
            print(colorama.Fore.WHITE+"\tScanned %d ports in %.3f seconds"%((end_port - start_port), t))

        elif choice == 5:
            hostIP = input("Enter an IP Addr. to scan: ")

        elif choice == 6:
            #   Exit the program
            break

main()
