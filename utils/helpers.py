import time, os, platform

settings = {
    # page 1
    "textSpeed": 1,
    "caret": ">",

    # page 2
    "actionMsg": "what is your action? ",
    "saveMsg": "file {saveNum} saved.",
    "loadMsg": "file {saveNum} loaded.",
    "newDayMsg": "the day is ending...",

    # page 3
    "up": "w",
    "left": "a",
    "down": "s",
    "right": "d",
    "select": "z",
    "cancel": "x",
    "misc": "c"
}

# adv = advanced
def inputadv(msg="", caret=settings["caret"]):
    inp = input(f"{msg}\n{caret} ").lower()
    return inp
def sleepadv(length=1, speed=settings["textSpeed"]):
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