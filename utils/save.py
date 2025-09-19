import json, os
from utils import config as c

saveDir = os.path.join("..", "savefiles")
saveDirAlt = "savefiles"
os.makedirs(saveDir, exist_ok=True)
saveNum = len(os.listdir(saveDir))
currentSave: 0

# default save
defaultData = {
    "kingdom": {
        "name": "",
        "gold": 0,
    },
    "config": {
        "textSpeed": 1,
        "caret": ">",
        # page 2
        "actionMsg": "what is your action? ",
        "saveMsg": f"file {saveNum} saved.",
        "loadMsg": f"file {saveNum} loaded.",
        "newDayMsg": "the day is ending...",
        # page 3
        "up": "w",
        "left": "a",
        "down": "s",
        "right": "d",
        "select": "z",
        "cancel": "x",
        "misc": "c"
    },
    "data": {
        "version": 1.0,
        "timesPlayed": 0,
    },

    "i see you smuggling in here...": True,
}

def save(data, saveSlot=saveNum):
    filePath = os.path.join(saveDir, f"savefile{saveSlot}.json")
    with open(filePath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{c.settings[f"saveMsg"]}")

def load(saveDirectory, saveSlot):
    filePath = os.path.join(saveDirectory, f"savefile{saveSlot}.json")
    if not os.path.exists(filePath):
        print(f"save not found, check {filePath}.")
        return None
    with open(filePath, "r") as f:
        data = json.load(f)
        print(f"{c.settings[f"loadMsg"]}")
        return data

# choice = input("save/load")
# if choice == "save":
#     slot = int(input("slot num?"))
#     save(defaultData, slot)
#
# elif choice == "load":
#     choice = int(input("slot num?"))
#     saveData = load(saveDir, choice)
#     print(saveData)

# im so snart