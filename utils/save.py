import json, os
from utils import config as c

os.makedirs('savefiles', exist_ok=True)
saveNumAlt = 0
currentSave = 0

def initSaveNum(saveNum=saveNumAlt):
    for i in range(len(os.listdir('savefiles'))):
        if os.listdir('savefiles')[i] != 'conf.json':
            saveNum += 1
    return saveNum

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
    "saveMsg": f"file {initSaveNum()} saved.",
    "loadMsg": f"file {initSaveNum()} loaded.",
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


# yu7y8ghji9l,;09plty[0n ] byik'/6oltb7ynph, 'bvf[n-mg5b
def save(saveData, slot=initSaveNum(), msg=c.settings["saveMsg"]):

    # define filepath
    if slot == "config":
        slotAlt = "conf.json"
    else:
        slotAlt = "savefile" + str(slot) + ".json"
    filePath = os.path.join('savefiles', slotAlt)

    # write
    with open(filePath, "w") as savefile:
        json.dump(saveData, savefile, indent=4)

    # msg logic
    if msg and slot == "config":
        print(c.settings["saveMsg"].format(saveNum="config"))
    elif msg:
        print(c.settings["saveMsg"].format(saveNum=slot))


def saveDict(newDict, newData, saveData):
    saveData[newDict].update(newData)
    save(saveData, msg=False)


def load(saveDirectory='savefiles', saveNum=initSaveNum(), msg=c.settings["loadMsg"]):
    filePath = os.path.join(saveDirectory, f"savefile{saveNum}.json")
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            loadData = json.load(f)
            if msg:
                print(c.settings["loadMsg"].format(saveNum=saveNum))
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


choice = input("save/load")
if choice == "save":
    slot = input("slot num?")
    if slot == 'config':
        save(defaultConfig, slot)
    else:
        save(defaultData, slot)

elif choice == "load":
    slot = input("slot num?")
    saveData = load('savefiles', slot)
    print(saveData)


# im so snart
