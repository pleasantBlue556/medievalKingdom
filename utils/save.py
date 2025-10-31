import json
import os

os.makedirs("savefiles", exist_ok=True)
saveDirList = os.listdir("savefiles")
# init sdlf
saveDirListFiltered = []
for i in range(len(saveDirList)):
    if saveDirList[i].endswith(".json") and saveDirList[i].startswith("savefile"):
        saveDirListFiltered.append(saveDirList[i])


currentSave = 0


# default save
defaultData = {
    "kingdom": {
        "name": "",
        "gold": 0,
        "day": 0,
    },
    "data": {
        "version": 1.0,
        "timesPlayed": 0,
        "stop smuggling!!!": True,
    },
}
defaultConfig = settings = {
    # page 1
    "textSpeed": 1,
    "caretColorless": ">",
    "caret": ">",
    "caretFore": '\x1b[38;5;255m',
    "caretBack": '\x1b[38;5;232m',
    "saveListCap": 4,
    # page 2
    "saveMsg": "file {saveNum} saved.",
    "loadMsg": "file {saveNum} loaded.",
    "newDayMsg": "the day is ending...",
    "actionMsg": "what is your action?",
    # page 3
    "up": "w",
    "left": "a",
    "down": "s",
    "right": "d",
    "select": "z",
    "cancel": "x",
    "misc": "c",
}


# yu7y8ghji9l,;09plty[0n ] byik'/6oltb7ynph, 'bvf[n-mg5b       # ???
def save(saveData, slot, msg=defaultConfig["saveMsg"]):
    # define filepath
    if slot in ["config", "conf"]:
        _slot = "conf.json"
    else:
        _slot = "savefile" + str(slot) + ".json"
    filePath = os.path.join("savefiles", _slot)

    # write
    try:
        with open(filePath, "w") as savefile:
            json.dump(saveData, savefile, indent=4)
    except FileNotFoundError:
        print(f"could not find {filePath}.")

    # msg logic
    if msg and slot == "conf":
        print(msg.format(savenum="config"))
    elif msg:
        print(msg.format(savenum=slot))


def saveDict(newDict, newData, saveData, saveNum):
    saveData[newDict].update(newData)
    save(saveData, saveNum, msg=False)


def load(saveDirectory="savefiles", slot=None, msg=defaultConfig["loadMsg"]):
    if slot not in ["conf", "config"]:
        filePath = os.path.join(saveDirectory, f"savefile{slot}.json")
    elif slot in ["conf", "config"]:
        filePath = os.path.join(saveDirectory, "conf.json")
    else:
        print(f"did not have saveNum: {slot}.")
        return None
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            loadData = json.load(f)
            if msg:
                print(msg.format(savenum=slot))
    else:
        print(f"save not found, check {filePath}.")
        return None

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
#     slot = input("slot num?")
#     if slot == "config":
#         save(defaultConfig, slot)
#     else:
#         save(defaultData, slot)
#
# elif choice == "load":
#     slot = input("slot num?")
#     saveData = load("savefiles", slot)
#     print(saveData)
#
#
# im so snart
