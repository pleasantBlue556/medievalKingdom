import time, os, platform
from utils import config as c

# adv = advanced
def inputadv(msg="", caret=c.settings["caret"]):
    inp = input(f"{msg}\n{caret} ").lower()
    return inp
def sleepadv(length=1, speed=c.settings["textSpeed"]):
    time.sleep(length*speed)
def clearAll():
    if platform.system() == "Windows":
        os.system("cls") # prints a box with an x in terminal but works in cmd
    elif platform.system() == "Linux":
        os.system("clear")
def huh(msg, sleepTime, returnArea):
    if msg == "min":
        print("please enter a higher number.")
    elif msg == "max":
        print("please enter a lower number.")
    elif msg == "dnu":
        print("did not understand.")
    else:
        print(msg)
    sleepadv(sleepTime)
    return returnArea