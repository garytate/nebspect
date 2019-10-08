## Nebspect Version 0.0.1
## Maintained by Gary (me@garytate.co.uk)
## Version 0.0.1 published 08/10/19

## Imports
import sys
import directory

## Initiating

# Error Check ex01 - file not ran from main folder.
if (not directory.verifyDirectory()):
    print("FATAL ERROR ex01: Please run main.py directly from the folder.\nProgram shutting down.")
    sys.exit(0)

log_folder = directory.getLogFolder(directory.getDirectoryParent())
print(log_folder)
input()