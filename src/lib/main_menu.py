from pip._vendor.colorama import Fore, Back, Style
from lib import logging

def displayMenu(logs, chars, fLogs, fChars):
    """ Files Loaded: xy, Characters Loads: xy
        [1] Load Characters
        [2] Load Log Files
        [3] Check Activity
        [4] Exit
    """
    print("\n" + "*"*30 + "\n")
    print(Fore.WHITE + "Files Loaded: " + Fore.GREEN + str(len(logging.getLogArray(fLogs))) + Fore.WHITE + " Characters Loaded: " + Fore.GREEN + str(len(chars)) + "\n")
    print(Fore.BLUE + "[1] " + Fore.WHITE + "Load Characters")
    print(Fore.BLUE + "[2] " + Fore.WHITE + "Load Log Files")
    print(Fore.BLUE + "[3] " + Fore.WHITE + "Check Activity")
    print(Fore.BLUE + "[4] " + Fore.WHITE + "Exit Program")
