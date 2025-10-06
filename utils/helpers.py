import time, os, platform
from utils import config as c
from colorama import init as coloramaInit, Fore as cf, Back as cb, Style as cs

userSys = platform.system()
if userSys == "Windows":
    coloramaInit(autoreset=True)


# adv = advanced
def inputadv(msg="", caret=c.settings["caret"]):
    inp = input(f"{msg}\n{caret} ").lower()
    return inp


def sleepadv(length=1, speed=c.settings["textSpeed"]):
    time.sleep(length * speed)


def clearAll():
    if platform.system() == "Windows":
        os.system("cls")  # prints a box with an x in terminal but works in cmd
    elif platform.system() == "Linux":
        os.system("clear")


# doesnt work
# def huh(msg="dnu", sleepTime=1, returnArea=False):
#     if msg == "min":
#         print("please enter a higher number.")
#     elif msg == "max":
#         print("please enter a lower number.")
#     elif msg == "dnu":
#         print("did not understand.")
#     else:
#         print(msg)
#     sleepadv(sleepTime)
#     if returnArea:
#         return returnArea
#     elif not returnArea:
#         return

# looks too chaotic
# def printadv(text):
#     textAlt = ''
#     for letter in text:
#         textAlt += letter
#         print(textAlt)
#         sleepadv(0.02)
#         clearAll()

def resolveColor(mode, name):
    mode, color = name.split('.')
    nameSpace = {'cf': cf, 'cb': cb, 'cs': cs}
    return getattr(nameSpace[mode], color)

def getColor(colorType) -> str:
    colorType.upper()
    if colorType == "BLUE":
        return "blue"
    elif colorType == "LIGHTBLUE_EX":
        return "light blue"
    elif colorType == "BLACK":
        return "black"
    elif colorType == "LIGHTWHITE_EX":
        return "white"
    elif colorType == "LIGHTBLACK_EX":
        return "gray"
    elif colorType == "CYAN":
        return "cyan"
    elif colorType == "GREEN":
        return "green"
    elif colorType == "LIGHTCYAN_EX":
        return "light cyan"
    elif colorType == "LIGHTGREEN_EX":
        return "light green"
    elif colorType == "LIGHTMAGENTA_EX":
        return "light magenta"
    elif colorType == "LIGHTRED_EX":
        return "pink"
    elif colorType == "LIGHTYELLOW_EX":
        return "light yellow"
    elif colorType == "MAGENTA":
        return "magenta"
    elif colorType == "RED":
        return "red"
    elif colorType == "WHITE":
        return "light gray"
    elif colorType == "YELLOW":
        return "yellow"
    else:
        return None


def getColorAlt(colorType) -> str:
    colorType.lower()
    if colorType == "blue":
        return "BLUE" # use resolveColor later
    elif colorType == "light blue":
        return "LIGHTBLUE_EX"
    elif colorType == "black":
        return "BLACK"
    elif colorType == "white":
        return "LIGHTWHITE_EX"
    elif colorType == "gray":
        return "LIGHTBLACK_EX"
    elif colorType == "cyan":
        return "CYAN"
    elif colorType == "green":
        return "GREEN"
    elif colorType == "light cyan":
        return "LIGHTCYAN_EX"
    elif colorType == "light green":
        return "LIGHTGREEN_EX"
    elif colorType == "light magenta":
        return "LIGHTMAGENTA_EX"
    elif colorType == "pink":
        return "LIGHTRED_EX"
    elif colorType == "light yellow":
        return "LIGHTYELLOW_EX"
    elif colorType == "magenta":
        return "MAGENTA"
    elif colorType == "red":
        return "RED"
    elif colorType == "light gray":
        return "WHITE"
    elif colorType == "yellow":
        return "YELLOW"
    else:
        return None


def highlight(mode="digit", text="", color=cf.BLUE) -> str:
    endResult = ""
    if mode == "digit":
        for letter in text:
            if letter.isdigit():
                endResult += color + letter + cs.RESET_ALL
            else:
                endResult += letter
        return endResult


# debug
# for i in range(10):
#     print(highlight('digit', f'savefile{i}'))
# sleepadv(2)
