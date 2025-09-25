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


def huh(msg="dnu", sleepTime=1, returnArea=False):
    if msg == "min":
        print("please enter a higher number.")
    elif msg == "max":
        print("please enter a lower number.")
    elif msg == "dnu":
        print("did not understand.")
    else:
        print(msg)
    sleepadv(sleepTime)
    if returnArea:
        return returnArea
    elif not returnArea:
        return


# looks too chaotic
# def printadv(text):
#     textAlt = ''
#     for letter in text:
#         textAlt += letter
#         print(textAlt)
#         sleepadv(0.02)
#         clearAll()

def getColor(colorType) -> str:
    if colorType == 'cf.BLUE':
        return 'blue'
    elif colorType == 'cf.LIGHTBLUE_EX':
        return 'light blue'
    elif colorType == 'cf.BLACK':
        return 'black'
    elif colorType == 'cf.LIGHTWHITE_EX':
        return 'light gray'
    elif colorType == 'cf.LIGHTBLACK_EX':
        return 'gray'
    elif colorType == 'cf.CYAN':
        return 'cyan'
    elif colorType == 'cf.GREEN':
        return 'green'
    elif colorType == 'cf.LIGHTCYAN_EX':
        return 'light cyan'
    elif colorType == 'cf.LIGHTGREEN_EX':
        return 'light green'
    elif colorType == 'cf.LIGHTMAGENTA_EX':
        return 'light magenta'
    elif colorType == 'cf.LIGHTRED_EX':
        return 'pink'
    elif colorType == 'cf.LIGHTYELLOW_EX':
        return 'light yellow'
    elif colorType == 'cf.MAGENTA':
        return 'magenta'
    elif colorType == 'cf.RED':
        return 'red'
    elif colorType == 'cf.WHITE':
        return 'white'
    elif colorType == 'cf.YELLOW':
        return 'yellow'

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
