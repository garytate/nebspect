## Nebspect :: Logging Module
## Maintained by Gary (me@garytate.co.uk)

import os

def getLogByDate(date, dir):
    log_file = dir + ("/" + date)
    return log_file

def getLogArray(dir):
    logArray = []
    for filename in os.listdir(dir):
        logArray.append(filename)
    return logArray

def getLogArrayOutput(dir):
    logArray = []
    print("\n" + "*"*30 + "\n")
    for filename in os.listdir(dir):
        print("Loaded: " + filename)
        logArray.append(filename)
    return logArray
