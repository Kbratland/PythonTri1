from pyperclip import *

def titleCase():
    returnString = ""
    noCap = ['a', 'and', 'as', 'at', 'but', 'by', 'down', 'for', 'from', 'if', 'in', 'into', 'like', 'near', 'nor',
             'of', 'off', 'on', 'once', 'onto', 'or', 'over', 'past', 'so', 'than', 'that', 'to', 'upon', 'when', 'with', 'Yet']
    stringList = []
    stringList += paste().lower().split()
    for lp in range(0, len(stringList)):
        if (lp == 0 or lp == len(stringList)-1):
            stringList[lp] = stringList[lp].capitalize()
        else:
            if not stringList[lp] in noCap:
                stringList[lp] = stringList[lp].capitalize()
        returnString += stringList[lp] + " "
    return returnString

print(titleCase())
copy(titleCase())