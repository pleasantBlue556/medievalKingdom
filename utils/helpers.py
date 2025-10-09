import os
import platform
import time

from colorama import Style as cs, init as coloramaInit
from colorama_ex.ansi_ex_back import Back as cb, Back_EX as cbx, Back_Gray as cbg
from colorama_ex.ansi_ex_fore import Fore as cf, Fore_EX as cfx, Fore_Gray as cfg

from utils import config as c

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


def resolveColor(name):
    mode, color = name.split(".")
    nameSpace = {"cf": cf, "cb": cb, "cs": cs, "cfx": cfx, "cbx": cbx, "cfg": cfg, "cbg": cbg}
    return getattr(nameSpace[mode], color)


#
# def getColorAlt(_colorType) -> str:
#     str(_colorType.upper())
#     print(_colorType)
#     n, colorType = _colorType.split(".")
#     if colorType == "BLUE":
#         return "blue"
#     elif colorType == "LIGHTBLUE_EX":
#         return "light blue"
#     elif colorType == "BLACK":
#         return "black"
#     elif colorType == "LIGHTWHITE_EX":
#         return "white"
#     elif colorType == "LIGHTBLACK_EX":
#         return "gray"
#     elif colorType == "CYAN":
#         return "cyan"
#     elif colorType == "GREEN":
#         return "green"
#     elif colorType == "LIGHTCYAN_EX":
#         return "light cyan"
#     elif colorType == "LIGHTGREEN_EX":
#         return "light green"
#     elif colorType == "LIGHTMAGENTA_EX":
#         return "light magenta"
#     elif colorType == "LIGHTRED_EX":
#         return "pink"
#     elif colorType == "LIGHTYELLOW_EX":
#         return "light yellow"
#     elif colorType == "MAGENTA":
#         return "magenta"
#     elif colorType == "RED":
#         return "red"
#     elif colorType == "WHITE":
#         return "light gray"
#     elif colorType == "YELLOW":
#         return "yellow"
#     else:
#         return None
#

def getColor(colorType) -> str:
    colorType.lower()
    if colorType == "blue":
        return cf.BLUE
    elif colorType == "light blue":
        return cfx.MALIBUBLUE
    elif colorType == "black":
        return cfg.BLACK
    elif colorType == "white":
        return cfg.WHITE
    elif colorType == "gray":
        return cfg.GRAY16
    elif colorType == "cyan":
        return cfx.ROBINBLUE
    elif colorType == "green":
        return cf.GREEN
    elif colorType == "light cyan":
        return cfx.TURQUISE
    elif colorType == "light green":
        return cfx.GREEN_EX
    elif colorType == "light magenta":
        return cfx.PINKFLAMINGO
    elif colorType == "pink":
        return cfx.RAZZLEDAZZLE
    elif colorType == "light yellow":
        return cfx.LASERLEMON
    elif colorType == "magenta":
        return cfx.MAGENTA
    elif colorType == "red":
        return cfx.RED
    elif colorType == "light gray":
        return cfg.GRAY20
    elif colorType == "yellow":
        return cfx.YELLOW
    elif colorType == "purple":
        return cfx.ELECTRICVIOLET
    elif colorType == "light purple":
        return cfx.LIGHTELECTRICVIOLET
    elif colorType == "orange":
        return cfx.ORANGEPEEL
    elif colorType == "light orange":
        return cfx.NEONCARROT
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
