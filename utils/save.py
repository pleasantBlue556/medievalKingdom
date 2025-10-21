import json
import os

from utils import config as c

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
    },
    "data": {
        "version": 1.0,
        "timesPlayed": 0,
        "stop smuggling!!!": True,
    },
}
defaultConfig = c.settings


# yu7y8ghji9l,;09plty[0n ] byik'/6oltb7ynph, 'bvf[n-mg5b
def save(saveData, slot, msg=c.settings["saveMsg"]):
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
    if msg and slot == "config":
        print(c.settings["saveMsg"].format(saveNum="config"))
    elif msg:
        print(c.settings["saveMsg"].format(saveNum=slot))


def saveDict(newDict, newData, saveData, saveNum):
    saveData[newDict].update(newData)
    save(saveData, saveNum, msg=False)


def load(saveDirectory="savefiles", saveNum=None, msg=c.settings["loadMsg"]):
    if saveNum != "config":
        filePath = os.path.join(saveDirectory, f"savefile{saveNum}.json")
    elif saveNum == 'config':
        filePath = os.path.join(saveDirectory, 'conf.json')
    else:
        print(f'did not have saveNum: {saveNum}.')
        return None
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            loadData = json.load(f)
            if msg:
                print(c.settings["loadMsg"].format(saveNum=saveNum))
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
