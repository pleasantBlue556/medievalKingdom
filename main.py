import json, os, platform, sys
from colorama import init as coloramaInit, Fore as cf, Style as cs, Back as cb
from utils import config as conf
from utils import save as sv
from utils import helpers as h

# import curses as cr

userSys = platform.system()
userVer = platform.release()
# if distro.name():
#     userVer = distro.name()

# init os
if userSys == "Windows":
    coloramaInit(autoreset=True)

# ↑↓←→
currentCaret = 1
caret1 = conf.settings["caret"]
caret2 = "↓"
caret3 = "↓"
caret4 = "↓"

# file
saveFileList = []
saveFileListAlt = []
currentSaveAlt = ""
loadDataAlt = ""
currentSave = 0
breakOut = False
saveDirList = os.listdir(sv.saveDirAlt)

# shorter keybind var
w = conf.settings["up"]
a = conf.settings["left"]
s = conf.settings["down"]
d = conf.settings["right"]
z = conf.settings["select"]
x = conf.settings["cancel"]
c = conf.settings["misc"]
keybindList = [w, a, s, d, z, x, c]

# settings keywords
settingsKeywords = [
    "text",
    "text speed",
    "speed",
    "caret",
    "save",
    "save message",
    "load",
    "load message",
    "new day message",
    "day message",
    "end message",
    "end",
    "action message",
    "action",
    "act",
    "up",
    "left",
    "down",
    "right",
    "select",
    "cancel",
    "misc",
]

# settings var
nextP = False
prevP = False
page = 1
page3Extra = ""

# credits var
credPage = 1
# nextP and prevP carry on with credits page


def fileFunc():
    """runs whenever file is picked"""
    global currentSaveAlt, currentSave, loadDataAlt, breakOut
    h.clearAll()
    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [files]{cs.RESET_ALL}")

    # split .json off
    saveFileListAlt = os.listdir(sv.saveDirAlt)
    saveFileList = []
    for i in range(len(os.listdir(sv.saveDirAlt))):
        # REALLY weird looking but just cuts the .json off
        saveFileList.append(os.path.splitext(saveFileListAlt[i])[0])

    if len(os.listdir(sv.saveDirAlt)) == 0:
        print("use 'c' to start a new file.")
    else:
        # list prints
        for displayIndex, fileName in enumerate(sorted(os.listdir(sv.saveDirAlt))):
            filePath = os.path.join(sv.saveDirAlt, fileName)
            if fileName.endswith(".json"):
                # grab data from each save
                with open(filePath, "r") as f:
                    data = json.load(f)
                name = data.get("kingdom", None).get("name", "")
                gold = data.get("kingdom", None).get("gold", 0)

                # add mark
                if displayIndex == currentSave:
                    currentSaveAlt = "*"
                else:
                    currentSaveAlt = ""
                print(
                    f"{displayIndex}{currentSaveAlt}: {fileName} // "
                    f"'{name}', {gold} gold"
                )

    print("")
    choice = h.inputadv(f"[#] [{z}] [{x}] [{c}] [help]")
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
    if choice == "help":
        print(f"[{z}]: continue (*)\n" f"[{x}]: exit\n" f"[{c}]: new file\n")
        h.inputadv("[enter] to leave")
    elif choice == x:
        h.clearAll()
        return
    elif choiceInt:
        currentSave = choice
        loadDataAlt = sv.load(sv.saveDirAlt, currentSave)
        breakOut = True
        h.sleepadv(1)
        h.clearAll()
        return
    elif choice in [z, "*"]:
        loadDataAlt = sv.load(sv.saveDirAlt, currentSave)
        breakOut = True
        h.sleepadv(1)
        h.clearAll()
        return
    elif choice == c:
        print(os.listdir(sv.saveDirAlt))
        if not os.listdir(sv.saveDirAlt)[0]:
            sv.save(sv.defaultData, sv.saveNum)
        else:
            sv.save(sv.defaultData, sv.saveNum + 1)
        if not os.path.exists(os.path.join(sv.saveDirAlt, "conf.json")):
            sv.save(sv.defaultConfig, "config")
        h.sleepadv(1)
    else:
        print("did not understand.\n")
        h.sleepadv(1)
    return fileFunc()


def settingsFunc():
    """recursive settings function, calls data from config and saves(?)"""
    global nextP, prevP, page, page3Extra, saveFileList, saveFileListAlt
    h.clearAll()
    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [settings]{cs.RESET_ALL}")
    if page == 1:
        nextP = True
        prevP = False
        page3Extra = ""
        print(
            "## page 1 - customization >>\n"
            f"1. text speed: {conf.settings['textSpeed']}\n"
            f"2. caret: '{conf.settings['caret']}'\n"
        )
    elif page == 2:
        nextP = True
        prevP = True
        page3Extra = ""
        print(
            "<< page 2 - messages >>\n"
            f"1. save message: {conf.settings['saveMsg']}\n"
            f"2. load message: {conf.settings['loadMsg']}\n"
            f"3. new day message: {conf.settings['newDayMsg']}\n"
            f"4. action message: {conf.settings['actionMsg']}\n"
        )
    elif page == 3:
        nextP = False
        prevP = True
        page3Extra = " only"
        print(
            "<< page 3 - keybinds ##\n"
            f"1. up: [{conf.settings['up']}]\n"
            f"2. left: [{conf.settings['left']}]\n"
            f"3. down: [{conf.settings['down']}]\n"
            f"4. right: [{conf.settings['right']}]\n"
            f"5. select: [{conf.settings['select']}]\n"
            f"6. cancel: [{conf.settings['cancel']}]\n"
            f"7. misc: [{conf.settings['misc']}]\n"
        )
    choice = h.inputadv(f"[<] [>] [#{page3Extra}] [{x}] [{c}] [help]").strip()
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
        # collapsable
    if choice == "help":
        print(
            f"[<]: previous page (also use {a})\n"
            f"[>]: next page (also use {d})\n"
            f"[<<]: first page\n"
            f"[>>]: last page\n"
            f"[{x}]: exit\n"
            f"[{c}]: save changes\n"
        )
        h.inputadv("[enter] to leave")
    elif choice in ["next", ">", d] and nextP:
        page += 1
    elif choice in ["prev", "previous", "<", a] and prevP:
        page -= 1
    elif choice == "<<":
        page = 1
    elif choice == ">>":
        page = 3
    elif choiceInt or choice in settingsKeywords:
        # pg 1. customization
        if page == 1:
            # text spd
            if choice in ["1", "text", "text speed", "speed"]:
                settingsChoice = h.inputadv(
                    "makes the text move faster or slower - default: 1\n"
                    "speed multipliers: [0] [0.25], [0.5], [1], [2], [3]\n"
                )
                if settingsChoice in ["0", "0.25", "1/4", "0.5", "1/2", "1", "2", "3"]:
                    if settingsChoice == "1/4":
                        settingsChoice = "0.25"
                    elif settingsChoice == "1/2":
                        settingsChoice = "0.5"
                    conf.settings["textSpeed"] = float(settingsChoice)
                    print(f"speed set to {conf.settings['textSpeed']}.\n")
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            # caret type
            elif choice in ["2", "caret"]:
                settingsChoice = h.inputadv(
                    "change the caret of every input statement - default: >\n"
                    "examples: ->, -, o\n"
                    "note: the newline and extra space after the caret are given automatically.\n"
                )
                conf.settings["caret"] = settingsChoice
                print(f"caret set to {conf.settings["caret"]}.\n")
                h.sleepadv(1)

        # pg 2. messages
        elif page == 2:
            # save message
            if choice in ["1", "save", "save message"]:
                settingsChoice = h.inputadv(
                    "edit the save message - default: 'file {saveNum} saved.'\n"
                    "[{saveNum}: save number] [blank: remove message]\n"
                )
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    conf.settings["saveMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    conf.settings["saveMsg"] = ""
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            # load message
            if choice in ["2", "load", "load message"]:
                settingsChoice = h.inputadv(
                    "edit the load message - default: 'file {saveNum} loaded.'\n"
                    "[{saveNum}: save number] [blank: remove message]\n"
                )
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    conf.settings["loadMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    conf.settings["loadMsg"] = ""
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            # new day message
            if choice in ["3", "new day message", "day message", "end message", "end"]:
                settingsChoice = h.inputadv(
                    "edits the 'day is ending' messages - default: 'the day is ending...'\n"
                    "[{day}: day number] [blank: remove messages]\n"
                )
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    conf.settings["newDayMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    conf.settings["newDayMsg"] = ""
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            # act message
            if choice in ["4", "action message", "action", "act"]:
                settingsChoice = h.inputadv(
                    "edits the action message - default: 'what is your action?'\n"
                    "[blank: remove messages]\n"
                )
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    conf.settings["actionMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    conf.settings["newDayMsg"] = ""
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

        # pg 3. keybinds
        elif page == 3:
            if choice in ["1", "up"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'up' - default: w\n"
                    f"can't use: {keybindList}\n"
                    "[:]"
                )
                if settingsChoice == ":":
                    return
                    # collapsable
                elif settingsChoice not in keybindList:
                    print(f"'up' set to '{settingsChoice}'.")
                    conf.settings["up"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            elif choice in ["2", "left"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'left' - default: a\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'left' set to '{settingsChoice}'.")
                    conf.settings["left"] = settingsChoice
                    h.sleepadv(1)
                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                else:
                    print("did not understand.")
                    h.sleepadv(1)
            elif choice in ["3", "down"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'down' - default: s\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'down' set to '{settingsChoice}'.")
                    conf.settings["down"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            elif choice in ["4", "right"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'right' - default: d\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'right' set to '{settingsChoice}'.")
                    conf.settings["right"] = settingsChoice
                    h.sleepadv(1)
                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                else:
                    print("did not understand.")
                    h.sleepadv(1)
            elif choice in ["5", "select"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'select' - default: z\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'select' set to '{settingsChoice}'.")
                    conf.settings["select"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)

                elif settingsChoice == ":":
                    return
                else:
                    print("did not understand.")
                    h.sleepadv(1)

            elif choice in ["6", "cancel"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'cancel' - default: x\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'cancel' set to '{settingsChoice}'.")
                    conf.settings["cancel"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)

                else:
                    print("did not understand.")
                    h.sleepadv(1)

            elif choice in ["7", "misc"]:
                settingsChoice = h.inputadv(
                    "edit keybind 'misc' - default: c\n"
                    f"can't use: {keybindList}\n"
                    f"[:]"
                )
                if settingsChoice == ":":
                    return
                elif settingsChoice not in keybindList:
                    print(f"'misc' set to '{settingsChoice}'.")
                    conf.settings["misc"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice in keybindList:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return
                else:
                    print("did not understand.")
                    h.sleepadv(1)

    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        print("that page is unavailable (unavailable pages are marked by #'s)")
        h.sleepadv(1.5)
    elif choice == x:
        h.clearAll()
        return
    elif choice == c:
        saveFileListAlt = os.listdir(sv.saveDirAlt)
        saveFileList = []
        # universal settings config
        sv.save(c.settings, "config")
        h.sleepadv(1)
    else:
        print("did not understand.")
        h.sleepadv(1)
    return settingsFunc()


def creditsFunc():
    global credPage, nextP, prevP
    h.clearAll()
    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [credits]{cs.RESET_ALL}")
    if credPage == 1:
        nextP = True
        prevP = False
        print("## page 1 - dev >>\n" "1: pleasantBlue\n")
    elif credPage == 2:
        nextP = True
        prevP = True
        print("<< page 2 - contributors >>\n" "...wip\n")
    elif credPage == 3:
        nextP = False
        prevP = True
        print("<< page 3 - special thanks ##\n" "...wip\n")
    choice = h.inputadv(f"[<] [>] [#] [{x}] [help]")
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
    if choice == "help":
        print(
            f"[<]: previous page (also use {a})\n"
            f"[>]: next page (also use {d})\n"
            f"[<<] first page\n"
            f"[>>] last page\n"
            f"[{x}]: exit\n"
            f"thanks to everyone on here!\n"
            f"i hope this list grows big someday :)\n"
        )
        h.inputadv("[enter] to leave")
    elif choice == "<<":
        credPage = 1
        return creditsFunc()
    elif choice == ">>":
        credPage = 3
        return creditsFunc()
    elif choice in ["next", ">", d] and nextP is not False:
        credPage += 1
        return creditsFunc()
    elif choice in ["prev", "previous", "<", a] and prevP is not False:
        credPage -= 1
        return creditsFunc()
    elif choice in [x]:
        h.clearAll()
        return
    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        print("that page is unavailable (unavailable pages are marked by #'s)")
        h.sleepadv(1.5)
        return creditsFunc()
    elif choiceInt:
        # pg 1. dev
        if page == 1:
            print(
                "hi! im the main dev of this game, but i dont like talking about myself very much...\n"
                "its kinda my first time coding (emphasis on 'kinda'), so... i try :)\n"
            )
            h.inputadv("[enter] to leave")
    else:
        print("did not understand.")
        h.sleepadv(1)
    return creditsFunc()


def quitFunc():
    h.clearAll()
    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [quit]{cs.RESET_ALL}")
    # sv.save()
    print("thanks for playing!")
    h.sleepadv(1)
    h.clearAll()
    sys.exit()


loadData = loadDataAlt
actionCount = 3


def gameLoop(actions=actionCount):
    for _ in range(actions):
        print(f"you have {actions} actions.")
        if loadDataAlt == sv.defaultData:
            command = h.inputadv('welcome to medievalKingdom! to start, type "help".')
        else:
            command = h.inputadv(f"{conf.settings['actionMsg']}")
        if command == "help":
            pass
        h.clearAll()
        actions -= 1


# start!
while True:
    h.clearAll()
    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [medievalKingdom]{cs.RESET_ALL}")
    print(
        f"{caret1} [files]\n"
        f"{caret2} [settings]\n"
        f"{caret3} [credits]\n"
        f"{caret4} [quit]"
    )
    choice = h.inputadv("")
    # up
    if choice == w:
        if currentCaret == 2:
            currentCaret -= 1
            caret2 = "↓"
            caret1 = conf.settings["caret"]
        elif currentCaret == 3:
            currentCaret -= 1
            caret3 = "↓"
            caret2 = conf.settings["caret"]
        elif currentCaret == 4:
            currentCaret -= 1
            caret4 = "↓"
            caret3 = conf.settings["caret"]
    # down
    elif choice == s:
        if currentCaret == 1:
            currentCaret += 1
            caret1 = "↑"
            caret2 = conf.settings["caret"]
        elif currentCaret == 2:
            currentCaret += 1
            caret2 = "↑"
            caret3 = conf.settings["caret"]
        elif currentCaret == 3:
            currentCaret += 1
            caret3 = "↑"
            caret4 = conf.settings["caret"]
    # select
    elif choice == z or not choice.strip():
        if currentCaret == 1:
            fileFunc()
        elif currentCaret == 2:
            settingsFunc()
        elif currentCaret == 3:
            creditsFunc()
        elif currentCaret == 4:
            quitFunc()
    # quit
    elif choice == x:
        quitFunc()
        # collapsable
    if breakOut:
        gameLoop()
        break
