import re, io, os, time
from lib import logging, characters
from pip._vendor.colorama import Fore, Back, Style

def getActivity(chars, logs, fLogs, fChars, fOutput):
    filename = time.time()
    print("\n" + "*"*30 + "\n")
    _setup = True
    while(_setup):
        output = str(input("Output to text file? [Y/N]: "))
        if (output.lower() == "y"):
            _writeoutput = True
            _setup = False
        elif (output.lower() == "n"):
            _writeoutput = False
            _setup = False
        else:
            print(Fore.RED + "\nIncorrect value.\n" + Fore.RESET)

    if (_writeoutput):
        if not os.path.exists(fOutput):
            print("Creating output directory.")
            os.makedirs(fOutput)

    fName = input("File name: ")
    for char in chars:
        charResults = 0
        charDaysActive = 0
        charIsActive = False
        charreg = re.sub(r'[^a-zA-Z]', "", char)
        for logfile in logs:
            log = logging.getLogByDate(logfile, fLogs)
            with io.open(log, encoding="utf-8") as l:
                for lines in l:
                    lines = re.sub(r'[^a-zA-Z]', "", lines)
                    if charreg in lines:
                        charResults += 1
                        charIsActive = True
                if charIsActive:
                    charDaysActive += 1
            charIsActive = False
        print("%s: %s | %s" % (char, charResults, charDaysActive))
    
    return 0
