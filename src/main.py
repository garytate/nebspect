## Nebspect Version 0.0.1
## Maintained by Gary (me@garytate.co.uk)
## Version 0.0.1 published 08/10/19

## Imports
import os, sys, time, re
from lib import directory, characters, logging, main_menu, getch, writing
from pip._vendor.colorama import init, Fore

## Initiating
init() # colorama
print("Nebspect: Version 0.0.1 - Last updated 08/10/2019\n")
active = True

# Initaliase sub-directories
main_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = directory.getChildDirectory(main_folder, "/logs")
char_folder = directory.getChildDirectory(main_folder, "/characters")
output_folder = directory.getChildDirectory(main_folder, "/results")

logging.getLogArrayOutput(log_folder)

# Main loop
while active:
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu.displayMenu(logging.getLogArray(log_folder), characters.loadCharacters(char_folder), log_folder, char_folder)
    try:
        choice = raw_input("> ")
    except:
        choice = input("> ")

    print(choice)
    if choice == '1': characters.loadCharactersOutput(char_folder)
    elif choice == '2': logging.getLogArrayOutput(log_folder)
    elif choice == '3': writing.getActivity(characters.loadCharacters(char_folder), logging.getLogArray(log_folder), log_folder, char_folder, output_folder), #WIP
    elif choice == '4': active = not active
    else: print(Fore.RED + "\nIncorrect option.")
    print(Fore.RESET + "\nPress enter to continue...")
    input()

print("")
