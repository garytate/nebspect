## Nebspect Version 0.0.1
## Maintained by Gary (me@garytate.co.uk)
## Version 0.0.1 published 08/10/19

## Imports
import sys
import os
from lib import directory

## Initiating

main_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = directory.getChildDirectory(main_folder, "\logs")
char_folder = directory.getChildDirectory(main_folder, "\characters")

print(main_folder, log_folder, char_folder)
input()