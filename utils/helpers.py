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

def highlight(rule, text='', color=cf.BLUE) -> str:
    endResult = ""
    for letter in text:
        if rule(letter):
            endResult += color + letter + cs.RESET_ALL
        else:
            endResult += letter
    return endResult