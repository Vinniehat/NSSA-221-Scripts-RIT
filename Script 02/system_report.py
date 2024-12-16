#!/usr/bin/env python3
# Vinnie Lauro - 10/04/2024

import socket
import os
import platform
from datetime import date
import sys
from sys import stdout

HOSTNAME = ""
class bColors: #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def displayHeader(headerName):
    print(bColors.HEADER + headerName + bColors.ENDC)

def displayDeviceInfo():
    displayHeader("Device Information")
    HOSTNAME = socket.gethostname()
    print("Hostname: " + HOSTNAME)
    print("Domain: " + socket.getfqdn())
    print()

def displayNetworkInfo():
    displayHeader("Network Information")
    print("IP Address: " + os.popen("ip addr show eth0 | grep inet | awk '{print $2}'").read().split("/")[0]) # https://askubuntu.com/questions/560412/how-to-display-ip-address-of-eth0-interface-using-a-shell-script
    print("Gateway: " + os.popen("ip route | grep default | awk '{print $3}'").read().strip())
    print("Network Mask: " + os.popen("ifconfig | grep -w 'inet' | awk '{print $4}' | head -1 ").read().strip())

    # For loop on each DNS server
    dnsServers = os.popen("cat /etc/resolv.conf | grep nameserver | awk '{print $2}'").read().split()

    for i in range(len(dnsServers)):
        print("DNS Server " + str(i+1) + ": " + dnsServers[i])
    
    print() # Blank line

def displayOSInfo():
    displayHeader("Operating System Information")
    print("Operating System: " + platform.system())
    print("OS Version: " + platform.version())
    print("Kernel Version: " + platform.release())
    print()

def displayStorageInfo():
    displayHeader("Storage Information")
    df_command = os .popen("df -h /").read().splitlines()[1:]
    # Headers: Filesystem Size Used Avail Use% Mounted on
    # Is split into a list of strings by each drive

    for i in range(len(df_command)): # For each drive
        row = df_command[i].split()
        print(bColors.OKBLUE + "---Drive " + str(i) + " --- " + bColors.ENDC)
        print("Drive Capacity: " + row[1])
        print("Used Space: " + row[2])
        print("Available Space: " + row[3])
    print()

def displayProcessorInfo():
    displayHeader("Processor Information")
    # print("CPU Model: " + (platform.processor() if platform.processor() != "" else "Unable to be determined"))
    print("CPU Model: " + os.popen("lscpu | grep 'Model name' | awk '{print $3}'").read().strip())
    print("Number of Processors: " + str(os.cpu_count()))
    print("Number of Threads: " + os.popen("nproc --all").read())
    print()

def displayMemoryInfo():
    displayHeader("Memory Information")

    free_command = os.popen("free -h").read().splitlines()[1].split()
    # Headers: Total RAM: used free shared buff/cache available
    # Is split into a list of strings by Mem and Swap

    print("Total RAM: " + free_command[1])
    print("Available RAM: " + free_command[6])
    print()

# main function


def main():
    current_user = os.popen("whoami").read().strip()
    log_file_path = f"/home/{current_user}/{socket.gethostname()}_system_report.log"
    sys.stdout = os.popen(f"tee {log_file_path}", "w") # https://stackoverflow.com/questions/26796592/print-on-console-and-text-file-simultaneously-python
    sys.stderr = sys.stdout

    os.system("clear")
    print(bColors.BOLD + bColors.OKGREEN + "System Report \t" + str(date.today()) + " " + bColors.ENDC + "\n")

    displayDeviceInfo()
    displayNetworkInfo()
    displayOSInfo()
    displayStorageInfo()
    displayProcessorInfo()
    displayMemoryInfo()

    stdout.close()

    print("Log file saved to: " + log_file_path + "!")

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()