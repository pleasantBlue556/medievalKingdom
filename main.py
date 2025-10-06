import json, os, platform, sys
from colorama import init as coloramaInit, Fore as cf, Style as cs, Back as cb
from utils import save as sv, helpers as h

try:
    with open(os.path.join("savefiles", "conf.json"), "r") as _confData:
        confData = json.load(_confData)
except FileNotFoundError:
    sv.save(sv.defaultConfig, 'config', msg=False)
    with open(os.path.join("savefiles", "conf.json"), "r") as _confData:
        confData = json.load(_confData)

userSys = platform.system()
userVer = platform.release()
# if distro.name():
#     userVer = distro.name()

# init os
if userSys == "Windows":
    coloramaInit(autoreset=True)

__name__ = "__main__"

# ↑↓←→
currentCaret = 1
confData["caret"] = (
    confData["caretFore"] + confData["caretBack"] + confData["caret"] + cs.RESET_ALL
)
caret1 = confData["caret"]
caret2 = "↓"
caret3 = "↓"
caret4 = "↓"

# shorter keybind var
w = confData["up"]
a = confData["left"]
s = confData["down"]
d = confData["right"]
z = confData["select"]
x = confData["cancel"]
c = confData["misc"]
keybindList = [w, a, s, d, z, x, c]

# settings keywords
settingsKeywords = [
    "text",
    "text speed",
    "speed",
    "caret",
    "caret color",
    "color",
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
# nextP and prevP carry

# file
saveFileList = []
_saveFileList = []
_currentSave = ""
loadDataAlt = ""
currentSave = 0
filePage = 1
saveListCap = confData["saveListCap"]
fileRangeMin = 0
if len(sv.saveDirList) < saveListCap:
    fileRangeMax = len(sv.saveDirList)
else:
    fileRangeMax = saveListCap

filePageNum = 0
for _ in range(filePageNum // saveListCap):
    filePageNum += 1
breakOut = False


def fileFunc():
    """runs whenever file is picked"""
    global _currentSave, currentSave, loadDataAlt, breakOut, fileRangeMin, fileRangeMax, filePage, saveListCap
    if len(sv.saveDirList) > saveListCap:
        nextP = True
    elif filePage == filePageNum:
        nextP = False
    else:
        nextP = False

    if len(sv.saveDirList) < saveListCap:
        prevP = True
    elif filePage == 1:
        prevP = False
    else:
        prevP = False
    h.clearAll()

    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [files]{cs.RESET_ALL}")

    # next/prev page
    statement = ""
    if prevP:
        statement += "<<"
    else:
        statement += "##"
    statement += f" page {filePage} ({fileRangeMin}-{fileRangeMax}) "
    if nextP:
        statement += ">>"
    else:
        statement += "##"
    print(statement)

    # split .json off
    _saveFileList = os.listdir("savefiles")
    saveFileList = []
    for i in range(len(_saveFileList)):
        # REALLY weird looking but just cuts the .json off
        saveFileList.append(os.path.splitext(_saveFileList[i])[0])

    if len(saveFileList) == 0:
        print("use 'c' to start a new file.")
    else:
        # list prints
        files = [
            f
            for f in sorted(os.listdir("savefiles"))
            if f.endswith(".json") and f.startswith("savefile")
        ]
        for displayIndex, fileName in enumerate(files):
            if displayIndex in range(fileRangeMin, fileRangeMax):
                filePath = os.path.join("savefiles", fileName)

                with open(filePath, "r") as f:
                    data = json.load(f)
                name = data.get("kingdom", None).get("name", "")
                gold = data.get("kingdom", None).get("gold", 0)

                # add mark
                if displayIndex == currentSave:
                    _currentSave = "*"
                else:
                    _currentSave = ""
                print(
                    f"{displayIndex}{_currentSave}: {fileName} // "
                    f"'{name}', {gold} gold"
                )

    print("")
    choice = h.inputadv(f"[#] [{z}] [{x}] [{c}] [help]")
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
        # collapsable
    if choice == "help":
        f"[<]: previous page (also use {a})\n"
        f"[>]: next page (also use {d})\n"
        f"[<<]: first page\n"
        f"[>>]: last page\n"
        f"[{z}]: continue\n"
        f"[{x}]: exit\n"
        f"[{c}]: new file\n"
        h.inputadv("[enter] to leave")
    elif choice == x:
        h.clearAll()
        return
    elif choiceInt:
        currentSave = choice
        loadDataAlt = sv.load("savefiles", currentSave)
        breakOut = True
        h.sleepadv(1)
        h.clearAll()
        return
    elif choice in [z, "*"] or not choice:
        loadDataAlt = sv.load("savefiles", currentSave)
        breakOut = True
        h.sleepadv(1)
        h.clearAll()
        return
    elif choice == c:
        if "conf.json" not in _saveFileList:
            sv.save(sv.defaultConfig, "conf")
        sv.save(sv.defaultData, sv.saveNum)
        currentSave = sv.saveNum
        h.sleepadv(1)
    elif choice in [a, "prev", "previous", "<"] and prevP:
        fileRangeMin -= saveListCap
        fileRangeMax -= saveListCap
    elif choice in [d, "next", ">"] and nextP:
        fileRangeMin += saveListCap
        fileRangeMax += saveListCap
    elif choice == "<<":
        filePage = 1
    elif choice == ">>":
        while True:
            filePage += 1
            if not nextP:
                break
    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        print("that page is unavailable (unavailable pages are marked by #'s)")
        h.sleepadv(1.5)
    else:
        print("did not understand.\n")
        h.sleepadv(1)
    return fileFunc()


def settingsFunc():
    """recursive settings function, calls data from config and saves(?)"""
    global nextP, prevP, page, page3Extra, saveFileList, _saveFileList
    h.clearAll()

    print(confData)

    print(f"{cb.LIGHTWHITE_EX}{cf.BLACK}// [settings]{cs.RESET_ALL}")
    if page == 1:
        nextP = True
        prevP = False
        page3Extra = ""
        print(
            "## page 1 - customization >>\n"
            f"1. text speed: {confData['textSpeed']}\n"
            f"2. caret: '{confData['caretColorless']}'\n"
            f"3. caret color: {h.getColor(confData['caretFore'])}, "
            f"{h.getColor(confData['caretBack'])}"
        )
    elif page == 2:
        nextP = True
        prevP = True
        page3Extra = ""
        print(
            "<< page 2 - messages >>\n"
            f"1. save message: {confData['saveMsg']}\n"
            f"2. load message: {confData['loadMsg']}\n"
            f"3. new day message: {confData['newDayMsg']}\n"
            f"4. action message: {confData['actionMsg']}\n"
        )
    elif page == 3:
        nextP = False
        prevP = True
        page3Extra = " only"  # added to choice input (numbers only!)
        print(
            "<< page 3 - keybinds ##\n"
            f"1. up: [{confData['up']}]\n"
            f"2. left: [{confData['left']}]\n"
            f"3. down: [{confData['down']}]\n"
            f"4. right: [{confData['right']}]\n"
            f"5. select: [{confData['select']}]\n"
            f"6. cancel: [{confData['cancel']}]\n"
            f"7. misc: [{confData['misc']}]\n"
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
                    confData["textSpeed"] = float(settingsChoice)
                    print(f"speed set to {confData['textSpeed']}.\n")
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
                confData["caret"] = settingsChoice
                confData["colorlessCaret"] = settingsChoice
                print(f"caret set to {confData['caret']}.\n")
                h.sleepadv(1)

            # caret color
            elif choice in ["3", "caret color", "color"]:
                foregroundChoice = h.inputadv(
                    "changes the front and back of the caret - default: white, black\n"
                    "examples: 'light blue, magenta' means light blue caret on magenta background.\n\n"
                    "foreground:"
                )
                if h.getColorAlt(foregroundChoice) is not None:
                    confData["caretFore"] = h.resolveColor('cf', h.getColorAlt(foregroundChoice))
                    print(f'caret forecolor set to {confData["caretFore"]}.\n')
                    h.sleepadv(1)

                    backgroundChoice = h.inputadv("background:")
                    if h.getColorAlt(backgroundChoice) is not None:
                        confData["caretBack"] = h.resolveColor('cb', h.getColorAlt(backgroundChoice))
                        print(f'caret backcolor set to {confData["caretBack"]}.\n')
                        h.sleepadv(1)
                    else:
                        print(
                            "try a different color.\n"
                            "colors: "
                            "[red] [blue] [green] [yellow] [cyan] [magenta] [white] [black]\n"
                            '+[light]\n'
                        )
                        h.inputadv("[enter] to leave")
                else:
                    print(
                        "try a different color.\n"
                        "colors: "
                        "[red] [blue] [green] [yellow] [cyan] [magenta] [white] [black]\n"
                        'add "light" before color to make it brighter!\n'
                    )
                    h.inputadv("[enter] to leave")

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
                    confData["saveMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    confData["saveMsg"] = ""
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
                    confData["loadMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    confData["loadMsg"] = ""
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
                    confData["newDayMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    confData["newDayMsg"] = ""
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
                    confData["actionMsg"] = settingsChoice
                    h.sleepadv(1)

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    confData["newDayMsg"] = ""
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
                    confData["up"] = settingsChoice
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
                    confData["left"] = settingsChoice
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
                    confData["down"] = settingsChoice
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
                    confData["right"] = settingsChoice
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
                    confData["select"] = settingsChoice
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
                    confData["cancel"] = settingsChoice
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
                    confData["misc"] = settingsChoice
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
        # universal settings config
        sv.save(confData, "config")
        h.sleepadv(1)
    else:
        print("did not understand.")
        h.sleepadv(1)
    sv.save(confData, "config")
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
    # cr.initscr()
    # cr.curs_set(2)  # block cursor

    for _ in range(actions):
        print(f"you have {actions} actions.")
        if loadDataAlt == sv.defaultData:
            command = h.inputadv('welcome to medievalKingdom! to start, type "help".')
        else:
            command = h.inputadv(f"{confData['actionMsg']}")
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
            caret1 = confData["caret"]
        elif currentCaret == 3:
            currentCaret -= 1
            caret3 = "↓"
            caret2 = confData["caret"]
        elif currentCaret == 4:
            currentCaret -= 1
            caret4 = "↓"
            caret3 = confData["caret"]
    # down
    elif choice == s:
        if currentCaret == 1:
            currentCaret += 1
            caret1 = "↑"
            caret2 = confData["caret"]
        elif currentCaret == 2:
            currentCaret += 1
            caret2 = "↑"
            caret3 = confData["caret"]
        elif currentCaret == 3:
            currentCaret += 1
            caret3 = "↑"
            caret4 = confData["caret"]
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
    if currentCaret == 1:
        caret1 = (
            confData["caretFore"]
            + confData["caretBack"]
            + confData["caret"]
            + cs.RESET_ALL
        )
    elif currentCaret == 2:
        caret2 = (
            confData["caretFore"]
            + confData["caretBack"]
            + confData["caret"]
            + cs.RESET_ALL
        )
    elif currentCaret == 3:
        caret3 = (
            confData["caretFore"]
            + confData["caretBack"]
            + confData["caret"]
            + cs.RESET_ALL
        )
    elif currentCaret == 4:
        caret4 = (
            confData["caretFore"]
            + confData["caretBack"]
            + confData["caret"]
            + cs.RESET_ALL
        )

# notes:
# sz36, cascadia semibold -> 23*94
