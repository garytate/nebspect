## Nebspect Version 0.0.1
## Maintained by Gary (me@garytate.co.uk)
## Version 0.0.1 published 08/10/19

## Imports
import os, sys
from lib import directory, characters, logging

## Initiating
os.system('cls')
print("Nebspect: Version 0.0.1 - Last updated 08/10/2019\n")

# Initaliase sub-directories
main_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = directory.getChildDirectory(main_folder, "/logs")
char_folder = directory.getChildDirectory(main_folder, "/characters")

# Loading all characters into memory
characters = characters.loadCharacters(char_folder)

# Loading all log file names into memory
logArray = logging.getLogArray(log_folder)
print(logArray)

for char in characters:
    print(char)
