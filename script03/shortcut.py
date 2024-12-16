# !/usr/bin/env python3
# Developed by Vinnie Lauro - 11/01/2024
import os
import time

USER_HOME_DIRECTORY = os.path.expanduser("~")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    try:
        # clear terminal
        os.system('clear')
        print("Welcome to the Symbolic Linker!")
        print()
        print("Current Directory: ", os.getcwd())
        print()
        print(bcolors.OKBLUE + "Press 1 to create a symbolic link in your home directory" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Press 2 to remove a symbolic link in your home directory" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Press 3 to display all symbolic links" + bcolors.ENDC)
        print()
        print(bcolors.OKCYAN + "Type (1-3) to select an option or type Q/q to quit: " + bcolors.ENDC)

        option = input() # get input

        if option == "1": # add
            os.system('clear')
            print(bcolors.OKCYAN + "Please type the name of the file: " + bcolors.ENDC)
            file = input()

            # check if file exists
            if os.path.exists(file):
                # create file in home directory
                os.symlink(os.path.abspath(file), os.path.join(USER_HOME_DIRECTORY + '/' + file))
                print(bcolors.OKGREEN + "Symbolic link created!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "File does not exist!" + bcolors.ENDC)


        elif option == "2": # del
            os.system('clear')
            print(bcolors.OKCYAN + "Please type the name of the file: " + bcolors.ENDC)
            file = input()
            # check if link exists
            link_path = os.path.join(USER_HOME_DIRECTORY + '/' + file)
            if os.path.islink(link_path): # check if file is a link
                # unlink file in home directory
                os.unlink(link_path)
                print(bcolors.OKGREEN + "Symbolic link removed!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "File does not exist!" + bcolors.ENDC)

        elif option == "3": # list all symbolic links
            os.system('clear')
            print(bcolors.OKGREEN + "Symbolic links in your home directory: " + bcolors.ENDC)
            os.system('ls -l ~ | grep ^l')

        elif option == "Q" or option == "q": # quit
            print(bcolors.OKBLUE + "Goodbye!" + bcolors.ENDC)
            print()
            time.sleep(1)
            os.system('clear')
            exit(0)

        else: # fallback if the user types an invalid option
            print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)
            print()
        wait = input(bcolors.OKBLUE + "\nPress enter to continue..." + bcolors.ENDC)

    except Exception as e: # catch any exceptions that may occur
        print(bcolors.FAIL + "Whoops! Something went wrong! Please try again." + bcolors.ENDC)
        print(bcolors.FAIL + "Error: ", str(e)+ bcolors.ENDC)
        print()
        wait = input(bcolors.OKBLUE + "\nPress enter to continue..." + bcolors.ENDC)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
