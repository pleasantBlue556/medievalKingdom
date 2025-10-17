import os
import platform
import time

from colorama import Style as cs, init as coloramaInit
from colorama_ex.ansi_ex_back import Back as cb, Back_EX as cbx, Back_Gray as cbg
from colorama_ex.ansi_ex_fore import Fore as cf, Fore_EX as cfx, Fore_Gray as cfg

userSys = platform.system()
if userSys == "Windows":
    coloramaInit(autoreset=True)


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


def resolveColor(name):
    mode, color = name.split(".")
    # print(mode, color)
    nameSpace = {
        "cf": cf,
        "cb": cb,
        "cs": cs,
        "cfx": cfx,
        "cbx": cbx,
        "cfg": cfg,
        "cbg": cbg,
    }
    # print(nameSpace[mode])
    return getattr(nameSpace[mode], color)


# def getColor(colorType, colorMode='f') -> str:
#     global blue, lightblue, black, black, white, gray, cyan, lightcyan, \
#         lightgreen, lightmagenta, pink, green, lightyellow, magenta, red,\
#         lightgray, yellow, purple, lightpurple, orange, lightorange
#     # fore
#     if colorMode == 'f':
#         blue = cf.BLUE
#         lightblue = cfx.MALIBUBLUE
#         black = cfg.BLACK
#         white = cfg.WHITE
#         gray = cfg.GRAY16
#         cyan = cfx.ROBINBLUE
#         green = cf.GREEN
#         lightcyan = cfx.BRIGHTTURQUISE
#         lightgreen = cfx.GREEN_EX
#         lightmagenta = cfx.PINKFLAMINGO
#         pink = cfx.RAZZLEDAZZLE
#         lightyellow = cfx.LASERLEMON
#         magenta = cfx.MAGENTA
#         red = cfx.RED
#         lightgray = cfg.GRAY20
#         yellow = cfx.YELLOW
#         purple = cfx.ELECTRICVIOLET
#         lightpurple = cfx.LIGHTELECTRICVIOLET
#         orange = cfx.ORANGEPEEL
#         lightorange = cfx.NEONCARROT
#     # back
#     elif colorMode == 'b':
#         blue = cb.BLUE
#         lightblue = cbx.MALIBUBLUE
#         black = cbg.BLACK
#         white = cbg.WHITE
#         gray = cbg.GRAY16
#         cyan = cbx.ROBINBLUE
#         green = cb.GREEN
#         lightcyan = cbx.BRIGHTTURQUISE
#         lightgreen = cbx.GREEN_EX
#         lightmagenta = cbx.PINKFLAMINGO
#         pink = cbx.RAZZLEDAZZLE
#         lightyellow = cbx.LASERLEMON
#         magenta = cbx.MAGENTA
#         red = cbx.RED
#         lightgray = cbg.GRAY20
#         yellow = cbx.YELLOW
#         purple = cbx.ELECTRICVIOLET
#         lightpurple = cbx.LIGHTELECTRICVIOLET
#         orange = (cbx
#                   .ORANGEPEEL)
#         lightorange = cbx.NEONCARROT
#     if colorType == 'blue':
#         return blue
#     elif colorType == "light blue":
#         return lightblue
#     elif colorType == "black":
#         return black
#     elif colorType == "white":
#         return white
#     elif colorType == "gray":
#         return gray
#     elif colorType == "cyan":
#         return cyan
#     elif colorType == "green":
#         return green
#     elif colorType == "light cyan":
#         return lightcyan
#     elif colorType == "light green":
#         return lightgreen
#     elif colorType == "light magenta":
#         return lightmagenta
#     elif colorType == "pink":
#         return pink
#     elif colorType == "light yellow":
#         return lightyellow
#     elif colorType == "magenta":
#         return magenta
#     elif colorType == "red":
#         return red
#     elif colorType == "light gray":
#         return lightgray
#     elif colorType == "yellow":
#         return yellow
#     elif colorType == "purple":
#         return purple
#     elif colorType == "light purple":
#         return lightpurple
#     elif colorType == "orange":
#         return orange
#     elif colorType == "light orange":
#         return lightorange
#     else:
#         return None


def highlight(mode="digit", text="", color=cf.BLUE) -> str:
    endResult = ""
    if mode == "digit":
        for letter in text:
            if letter.isdigit():
                endResult += color + letter + cs.RESET_ALL
            else:
                endResult += letter
        return endResult


# for i in range(10):
#     print(highlight('digit', f'savefile{i}'))
# sleepadv(2)

print(blue + "0000")
