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
    savedAlready = False
    if slot == "config":
        filePath = os.path.join(saveDir, f"conf.json")
        slotAlt = "conf"
    else:
        filePath = os.path.join(saveDir, f"savefile{slot}.json")
        slotAlt = "saveFile" + str(slot) + ".json"
    if not os.path.exists(filePath):
        # create path if it doesnt already exist
        if slotAlt == 'conf':
            with open(filePath, 'w') as configFile:
                json.dump(configFile, defaultConfig)
                savedAlready = True
        else:
            with open(filePath, 'w') as saveFile:
                json.dump(saveFile, defaultData)
                savedAlready = True
    if not savedAlready:
        # yu7y8ghji9l,;09plty[0n ] byik'/6oltb7ynph, 'bvf[n-mg5b
        with open(filePath, "w") as saveFile:
            json.dump(saveData, saveFile, indent=4)
    if msg:
        # saveNum = slot number
        print(c.settings["saveMsg"].format(saveNum=slot))
    elif msg and slot == 'config':
        # saveNum = 'conf'
        print(c.settings['saveMsg'].format(saveNum=slotAlt))

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



# choice = input("save/load")
# if choice == "save":
#     slot = input("slot num?")
#     if slot == 'config':
#         save(defaultConfig, slot)
#     else:
#         save(defaultData, slot)
#
# elif choice == "load":
#     slot = input("slot num?")
#     saveData = load(saveDir, slot)
#     print(saveData)


# im so snart
