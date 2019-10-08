## Nebspect :: Characters Module
## Maintained by Gary (me@garytate.co.uk)

import os
from pathlib import Path

# @array [strings]
def loadCharacters(directory):
    characters = []
    char_file = directory + "\characters.txt"
    with open(char_file, "r") as chars:
        for char in chars:
            char = char.replace("\r", "").replace("\n", "")
            characters.append(char)
    return characters
