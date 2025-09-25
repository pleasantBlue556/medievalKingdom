import json, os
from utils import config as c

saveDir = os.path.join("..", "savefiles")
saveDirAlt = "savefiles"
os.makedirs(saveDir, exist_ok=True)
saveNum = str(len(os.listdir(saveDir)))
currentSave: 0

# default save
defaultData = {
    "kingdom": {
        "name": "",
        "gold": 0,
    },
    "data": {
        "version": 1.0,
        "timesPlayed": 0,
        "stop smuggling!!!": True,
    },
}
defaultConfig = {
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
}


def save(saveData, slot=saveNum, msg=c.settings["saveMsg"]):
    if slot == "config":
        filePath = os.path.join(saveDir, f"conf.json")
        slotAlt = 'conf'
    else:
        filePath = os.path.join(saveDir, f"savefile{slot}.json")
        slotAlt = 'saveFile' + str(slot) + '.json'
    if os.path.exists(filePath):
        os.makedirs(os.path.join(saveDir, slotAlt), exist_ok=True)
    with open(filePath, "w") as f:
        json.dump(saveData, f, indent=4)
    if msg:
        print(c.settings['saveMsg'].format(saveNum=saveNum))


def saveDict(newDict, newData, saveData):
    saveData[newDict].update(newData)
    save(saveData, msg=False)
    print(f"saved {newDict}.")


def load(saveDirectory, saveNum, msg=c.settings["loadMsg"]):
    filePath = os.path.join(saveDirectory, f"savefile{saveNum}.json")
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            loadData = json.load(f)
            if msg:
                print(c.settings['loadMsg'].format(saveNum=saveNum))
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

#
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
