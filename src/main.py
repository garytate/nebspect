## Nebspect Version 0.0.1
## Maintained by Gary (me@garytate.co.uk)
## Version 0.0.1 published 08/10/19

## Imports
import os, sys, time, re
from lib import directory, characters, logging

## Initiating
print("Nebspect: Version 0.0.1 - Last updated 08/10/2019\n")

# Initaliase sub-directories
main_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = directory.getChildDirectory(main_folder, "/logs")
char_folder = directory.getChildDirectory(main_folder, "/characters")

# Loading all characters into memory
characters = characters.loadCharacters(char_folder)

# Loading all log file names into memory
logArray = logging.getLogArray(log_folder)
for log in logArray:
    print("Loaded: " + log)

before = time.time()

for char in characters:
    charResults = 0
    charDaysActive = 0
    charIsActive = False
    char = re.sub(r'[^a-zA-Z]', "", char)
    for logfile in logArray:
        logs = logging.getLogByDate(logfile, log_folder)
        with open(logs, encoding="UTF-8") as l:
            for lines in l:
                lines = re.sub(r'[^a-zA-Z]', "", lines)
                if char in lines:
                    charResults += 1
                    charIsActive = True
            if charIsActive:
                charDaysActive += 1
        charIsActive = False
    print(char, str(charResults), str(charDaysActive))        

after = time.time()

print(after-before)
