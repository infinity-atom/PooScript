from asyncio.windows_events import NULL
import sys
from time import sleep

def getArgs(index):
    return sys.argv[index]

def sendError(lineNo, text):
    print("\033[1;31;40m==========================================================")
    print("\033[1;31;40mAn error occured at line " + lineNo)
    print("\033[1;31;40m" + text)
    print("\033[1;31;40m==========================================================")
    print("\033[0;37;40m")

def sendDebug(title, text):
    print("\033[1;34;40m==========================================================")
    print("\033[1;37;40m" + title)
    print("\033[1;34;40m==========================================================")
    print("\033[1;34;40m" + text)
    print("\033[1;34;40m==========================================================")
    print("\033[0;37;40m")

# get file name

try:
    file = open(getArgs(1), "r").read()
except:
    sendError("0", "You need to specify a file.\nDoes the file exist? Is the file valid?")
    sys.exit(2)

lines = file.split("\n")

# interpret each line

print("\033[0;37;40m")

for line in lines:
    splitLine = line.split(":")

    if splitLine[0][:2] == "! " or splitLine[0] == "":
        continue

    if splitLine[0] == "send":
        print(line[5:])
    elif splitLine[0] == "wait":
        try:
            sleep(int(line[5:]))
        except:
            sendError(str(lines.index(line) + 1), "Could not find a valid number.")
            break
    elif splitLine[0] == "ask":
        try:
            askText = input(splitLine[1])
            if splitLine[2] == "send":
                print(askText)
            elif splitLine[2] == "void":
                continue
            else:
                sendError(str(lines.index(line) + 1), splitLine[2] + " is not a valid use argument.")
                break
        except:
            sendError(str(lines.index(line) + 1), "You have not specified a use argument.")
            break
    elif splitLine[0] == "debug":
        if line[6:] == "error":
            sendError(str(lines.index(line) + 1), "An error was triggered manually.")
            break
        elif line[6:] == "contents":
            sendDebug("debug:contents output", file)
        else:
            sendError(str(lines.index(line) + 1), line[6:] + " is not a valid argument.")
            break
    else:
        sendError(str(lines.index(line) + 1), splitLine[0] + " isn't a valid function")
        break