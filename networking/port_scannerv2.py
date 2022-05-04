import socket
import time
import colorama
from threading import Thread, Lock
from queue import Queue

colorama.init()
socket.setdefaulttimeout(0.05)

MENU_STRING = "\tWhat would you like to scan?\n\t[1]\tCommon Ports\n\t[2]\tAll Registered Ports\n\t[3]\tSpecific Port\n\t[4]\tSpecific Range of Ports\n\t[5]\tEnter new IP Address\n\t[6]\tQuit\n: "


def check_port(ip, port_num) -> bool:
    """Attempts to connect to the host using the specified port. Returns true if a connection can be established with
    the port, False otherwise

    Args:
        ip (str): Host IP address to connect to
        port_num: Port number (physical or virtual) that a socket connection should be created on
    Returns:
        bool: Result of connection to the host. True if connection is established, false otherwise
    """

    sock = socket.socket()
    try:
        sock.connect((ip, port_num))
    except socket.error:
        print(colorama.Fore.RED + f"[-] Port {port_num}:\tClosed")
        return False

    print(colorama.Fore.GREEN + f"[+] Port {port_num}:\tOpen")
    return True


def check_port_range(ip, port_start, port_end) -> list:
    """Method checks a range of ports and returns an array of all open ports

    Args:
        ip (str): Host IP address
        port_start: Starting port for the sacn
        port_end: End port for the scan
    Return:
        list: List of all open ports in the range
    """
    open_ports = list()

    try:
        for port in range(port_start, port_end):
            if check_port(ip, port):
                open_ports.append(port)
    except KeyboardInterrupt:
        print(colorama.Fore.WHITE + "\tTerminating Scan ...\n")

    return open_ports


def main():
    host_ip = input("Enter IP addr. to scan: ")
    while True:
        print("-" * 45)
        try:
            # Prompt user with menu
            choice = int(input(MENU_STRING))
            while choice < 1 or choice > 6:
                choice = int(input("\tPlease select one of the numbered options above\n: "))
        except ValueError:
            choice = int(input("\tPlease select one of the numbered options above\n: "))

        if choice == 1:
            """
            Scan all common ports 0-1023 on the host
            """
            start = time.time()
            open_ports = check_port_range(host_ip, 0, 1024)
            t = (time.time() - start)
            print(colorama.Fore.WHITE + f"\tScanned 1024 ports in {t:.3f} seconds")
            print(f"\t{len(open_ports)} open ports: {open_ports}")

        elif choice == 2:
            """
            Scan all 49151 logical ports on the host
            """
            start = time.time()
            open_ports = check_port_range(host_ip, 0, 49151)
            t = (time.time() - start)
            print(colorama.Fore.WHITE + f"\tScanned 49152 ports in {t:.3f} seconds")
            print(f"\t{len(open_ports)} open ports: {open_ports}")

        elif choice == 3:
            """
            Scan specific port
            """
            try:
                port_choice = int(input("\tSelect a port to scan\n: "))
                while port_choice < 0 or port_choice >= 65535:
                    port_choice = int(input("\tSelect a port in the range [0, 65535]\n:"))

            except ValueError:
                # User enters a character other than an integer
                port_choice = int(input("\tPlease enter an integer in the range [0, 49151]\n:"))

            start = time.time()
            check_port(host_ip, port_choice)
            t = (time.time() - start)
            print(colorama.Fore.WHITE + f"\tScanned port {port_choice} in {t:.3f} seconds")

        elif choice == 4:
            """
            Scan range of ports
            """
            try:
                start_port = int(input("Starting port: "))
                while start_port < 0 or start_port > 49150:
                    #   Ensure 0 <= start < 49150
                    start_port = int(input("\tPlease select a port in the range [0, 49150]\n: "))

            except ValueError:
                #   User enters a character other than an integer
                start_port = int(input("\tPlease enter an integer in the range [0, 49151]\n: "))

            try:
                end_port = int(input("End port: "))
                while end_port <= start_port or end_port > 49151:
                    #   Ensure start <= end < 49151
                    end_port = int(input("\tPlease select a port in the range [start_port+1, 49151]\n: "))

            except ValueError:
                #   User enters a character other than an integer
                end_port = int(input("\tPlease enter an integer in the range [start_port+1, 49151]\n: "))

            start = time.time()
            check_port_range(host_ip, start_port, end_port + 1)
            t = (time.time() - start)
            print(colorama.Fore.WHITE + f"\tScanned from port {start_port} to port {end_port} in {t:.3f} seconds")

        elif choice == 5:
            host_ip = input("Enter an IP addr. to scan: ")

        elif choice == 6:
            break


if __name__ == '__main__':
    main()
