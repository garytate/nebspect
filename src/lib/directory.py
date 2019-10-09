## Nebspect :: Directory Module
## Maintained by Gary (me@garytate.co.uk)

import os

# @return boolean
def verifyDirectory():
    return os.path.exists("main.py")

# @return string
def getChildDirectory(dir_parent, dir_child):
    return str(dir_parent) + dir_child
