#!/usr/bin/env python3
# Description: Will parse through the syslog file and output any failed password attempts greater than 10.
# By: Vinnie Lauro
# Date: 11/22/2024

import os
import re
from datetime import datetime
from operator import contains

from colorama import just_fix_windows_console, Fore, Back, Style
from geoip import geolite2

just_fix_windows_console()

SYSLOG_PATH = "./syslog.log"


def main():
    os.system("clear")
    print("Attacker report - " + str(datetime.now().strftime("%m/%d/%Y %H:%M:%S")))

    with open(SYSLOG_PATH, "r") as syslog:
        # Read syslog file

        ip_list = {}

        for line in syslog:
            try:
                if "Failed password" not in line:
                    continue
                # Apr 15 00:00:07 spark sshd[7798]: Failed password for root from 218.25.208.92 port 20924 ssh2

                # line = line.split("Failed password for ")[1]
                # line = line.split(" from ")[1]
                #
                # # line should look like: "[IP] port [PORT] ssh2"
                #
                # ip = line.split()[0]

                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]

                if ip not in ip_list:
                    ip_list[ip] = 1
                else:
                    ip_list[ip] += 1
            except Exception as e:
                raise e

        # sort table from least to most (https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        ip_list = dict(sorted(ip_list.items(), key=lambda item: item[1]))
        print(ip_list)
        # Make table header
        print(f'{Fore.CYAN}COUNT\t\tIP ADDRESS\t\tCOUNTRY{Fore.RESET}')
        print("-------------------------------------")
        for ip in ip_list:
            # Print the result
            try:
                ipLookup = geolite2.lookup(ip)
                print(str(ip_list[ip]) + "\t\t" + ip + "\t\t" + ipLookup.country)
            except Exception as e:
                print(f'{Fore.RED}Error: {str(e)} - IP: {ip} - Continuing...{Fore.RESET}')
                if contains(str(e), "no attribute 'country'" ):
                    print(f'{Fore.YELLOW}Assigning type "NONE" to IP: {ip}...{Fore.RESET}', end="") # Still handle unknown countries
                    if ip_list[ip] >= 10:
                        print(f'{str(ip_list[ip])}\t\t{ip}\t\tNONE{Fore.RESET}')
                    else:
                        print(f'{Fore.YELLOW} - IP less than 10, not displaying...{Fore.RESET}')
                continue

        print("-------------------------------------")




if __name__ == "__main__":
    main()
