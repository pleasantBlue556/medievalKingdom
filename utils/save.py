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
        "misc": "c",
    },
    "data": {
        "version": 1.0,
        "timesPlayed": 0,
        "stop smuggling!!!": True,
    },
}


def save(saveData, saveSlot=saveNum, msg=c.settings["saveMsg"]):
    filePath = os.path.join(saveDir, f"savefile{saveSlot}.json")
    with open(filePath, "w") as f:
        json.dump(saveData, f, indent=4)
    if msg:
        print(f"{msg}")


def saveDict(newDict, newData, saveData, msg=c.settings["loadMsg"]):
    saveData[newDict].update(newData)
    save(saveData, msg=False)
    print(f"saved {newDict}.")


def load(saveDirectory, saveSlot, msg=c.settings["loadMsg"]):
    filePath = os.path.join(saveDirectory, f"savefile{saveSlot}.json")
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            loadData = json.load(f)
            if msg:
                print(msg)
    else:
        print(f"save not found, check {filePath}.")
        loadData = defaultData.copy()

    merge(loadData, defaultData)
    return loadData


def merge(target, data):
    for key, value in data.items():
        if key not in target:
            target[key] = value
        elif isinstance(value, dict):
            merge(target[key], value)


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
