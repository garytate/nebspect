## Nebspect :: Logging Module
## Maintained by Gary (me@garytate.co.uk)

import os

def getLogByDate(date):
    return []

def getLogArray(dir):
    logArray = []
    for filename in os.listdir(dir):
        logArray.append(filename)
    return logArray
