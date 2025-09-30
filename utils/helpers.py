import time, os, platform
from utils import config as c
from colorama import init as coloramaInit, Fore as cf, Style as cs

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

def getColor(colorType, mode="cf.") -> str:
    colorType.lower()
    if colorType == mode + "BLUE":
        print(colorType, mode + "BLUE")
        return "blue"
    elif colorType == mode + "LIGHTBLUE_EX":
        return "light blue"
    elif colorType == mode + "BLACK":
        return "black"
    elif colorType == mode + "LIGHTWHITE_EX":
        return "white"
    elif colorType == mode + "LIGHTBLACK_EX":
        return "gray"
    elif colorType == mode + "CYAN":
        return "cyan"
    elif colorType == mode + "GREEN":
        return "green"
    elif colorType == mode + "LIGHTCYAN_EX":
        return "light cyan"
    elif colorType == mode + "LIGHTGREEN_EX":
        return "light green"
    elif colorType == mode + "LIGHTMAGENTA_EX":
        return "light magenta"
    elif colorType == mode + "LIGHTRED_EX":
        return "pink"
    elif colorType == mode + "LIGHTYELLOW_EX":
        return "light yellow"
    elif colorType == mode + "MAGENTA":
        return "magenta"
    elif colorType == mode + "RED":
        return "red"
    elif colorType == mode + "WHITE":
        return "light gray"
    elif colorType == mode + "YELLOW":
        return "yellow"
    else:
        return None


def getColorAlt(colorType, mode="cf.") -> str:
    colorType.lower()
    if colorType == "blue":
        return mode + "BLUE"
    elif colorType == "light blue":
        return mode + "LIGHTBLUE_EX"
    elif colorType == "black":
        return mode + "BLACK"
    elif colorType == "white":
        return mode + "LIGHTWHITE_EX"
    elif colorType == "gray":
        return mode + "LIGHTBLACK_EX"
    elif colorType == "cyan":
        return mode + "CYAN"
    elif colorType == "green":
        return mode + "GREEN"
    elif colorType == "light cyan":
        return mode + "LIGHTCYAN_EX"
    elif colorType == "light green":
        return mode + "LIGHTGREEN_EX"
    elif colorType == "light magenta":
        return mode + "LIGHTMAGENTA_EX"
    elif colorType == "pink":
        return mode + "LIGHTRED_EX"
    elif colorType == "light yellow":
        return mode + "LIGHTYELLOW_EX"
    elif colorType == "magenta":
        return mode + "MAGENTA"
    elif colorType == "red":
        return mode + "RED"
    elif colorType == "light gray":
        return mode + "WHITE"
    elif colorType == "yellow":
        return mode + "YELLOW"
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
