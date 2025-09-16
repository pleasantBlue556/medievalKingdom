import json, os
from utils import config as c

saveDir = os.path.join("..", "savefiles")
os.makedirs(saveDir, exist_ok=True)
saveNum = len(os.listdir(saveDir))

# default save
defaultData = {
    "name": "",
    "gold": 100,
    "value": 5,
}

def save(data, saveSlot=saveNum):
    filePath = os.path.join(saveDir, f"savefile{saveSlot}.json")
    with open(filePath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{c.settings[f"saveMsg"]}")

def load(saveSlot):
    filePath = os.path.join(saveDir, f"savefile{saveSlot}.json")
    if not os.path.exists(filePath):
        print("save not found?")
        return None
    with open(filePath, "r") as f:
        data = json.load(f)
        print(f"{c.settings[f"loadMsg"]}")
        return data

# DEBUG
# choice = input("save/load")
# if choice == "save":
#     slot = int(input("slot num?"))
#     save(defaultData, slot)
#
# elif choice == "load":
#     choice = int(input("slot num?"))
#     saveData = load(choice)
#     print(saveData)

# im so snart