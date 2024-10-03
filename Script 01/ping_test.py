#!/usr/bin/env python3
import time
import os
import subprocess

SEP = "-" * 40

class bcolors: #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getDefaultGateway_Linux():
    p = subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)
    out = p.stdout.read().decode('utf-8').split()[2]
    return out

def testLocalConnectivity_Linux():
    gateway = getDefaultGateway_Linux()
    consoleResponse = os.system('ping -c 1 5' + gateway + ' > /dev/null') # -c 1 means only ping once


    if (consoleResponse == 0):
        print(bcolors.OKGREEN + "Local connectivity test successful." + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Local connectivity test failed." + bcolors.ENDC)

def testRemteConnectivity_Linux():
    url = "google.com"


def clearPrompt():
    print("Press Enter to continue...")
    input()
    prompt()

def prompt():
    print(SEP)
    print("Options:")
    print("1. Display default gateway")
    print("2. Test Local Connectivity")
    print("3. Test Remote Connectivity")
    print("4. Test DNS Resolution")

    choice = input("Please select an option (1-4) or enter Q/q to quit: ")
    print(SEP)
    # Validate input
    if choice == "1":
        print("Displaying default gateway...")
        print(SEP)

        print("Default gateway: " + getDefaultGateway_Linux())
        clearPrompt()
    elif choice == "2":
        print("Testing local connectivity...")
        print(SEP)
        testLocalConnectivity_Linux()
        time.sleep(0.1)
        clearPrompt()

    elif choice == "3":
        print("Testing remote connectivity... (pinging google.com)")
        print(SEP)



    elif choice == "Q" or choice == "q":
        print("Exiting program...")
        exit()
    if choice not in ["1", "2", "3", "4", "Q", "q"]:
        print(bcolors.FAIL + "Invalid choice. Please select a valid option." + bcolors.ENDC)

def main():
    print("Welcome to the ping tester!")
    while True:
        prompt()

if __name__ == "__main__":
    main()