import json, os, platform, sys, time, copy, unicurses as ucrs

if platform.system() == "Windows":
    try:
        import curses as crs
    except ImportError:
        # install windows port
        import subprocess

        subprocess.check_call(["pip", "install", "windows-curses"])
        import curses as crs
else:
    import curses as crs
# since all is imported as crs should work...?
_posX = 0  # starts at 0 on start, per printadv: _posX++    used for addstr
stdscr = crs.initscr()

from colorama import Style as cs, init as coloramaInit
from colorama_ex.ansi_ex_back import Back as cb, Back_EX as cbx, Back_Gray as cbg
from colorama_ex.ansi_ex_fore import Fore as cf, Fore_EX as cfx, Fore_Gray as cfg

cfxList = list(cfx.__dict__.items())
cfList = list(cf.__dict__.items())
cfgList = list(cfg.__dict__.items())
cbxList = list(cbx.__dict__.items())
cbList = list(cb.__dict__.items())
cbgList = list(cbg.__dict__.items())
spacingGray = cfg.GRAY12
# option one---[1] <--spacingGray for -
# option two---[2]
# option three-[3]

from utils import save as sv

# from utils import helpers as h

# INIT VARIABLES

try:
    confData = sv.load(slot="conf", msg=False)
    # with open(os.path.join("savefiles", "conf.json"), "r") as _confData:
    #     confData = json.load(_confData)
except FileNotFoundError:
    sv.save(sv.defaultConfig, "config", msg=False)
    confData = sv.load(slot="conf", msg=False)
    # with open(os.path.join("savefiles", "conf.json"), "r") as _confData:
    #     confData = json.load(_confData)


# adv = advanced
def printadv(msg="", posX=int(_posX), posY=0):
    global _posX
    _posX += 1  # increases by one
    stdscr.addstr(msg, posX, posY)


def inputadv(msg="", caret=confData["caret"], posY=0):
    crs.curs_set(2)
    stdscr.clear()
    if caret:
        printadv(f"{msg}\n{confData['caretFore']}{confData['caretBack']}{confData['caret']}{cs.RESET_ALL} ", posY=posY)
    else:
        printadv(f"{msg}\n{cs.RESET_ALL} ", posY=posY)
    ch = stdscr.getch()
    while True:
        if ch in [10, 13]: #10 is \n or enter and 13 is \r
            break
        elif ch in [crs.KEY_BACKSPACE, 127, 8]:
            if len()

    crs.curs_set(0)
    return str(inp.lower()) # just in case


def sleepadv(length=1, speed=confData["textSpeed"]):
    time.sleep(length * speed)


def clearAll():
    if platform.system() == "Windows":
        os.system("cls")  # prints a box with an x in terminal but works in cmd
    elif platform.system() == "Linux":
        os.system("clear")
    _posX = 0


def huh(error, returnArea=None, method=None, msg=""):
    if error is None:
        _msg = ""
    elif error == "max":
        _msg = "value is too high."
    elif error == "min":
        _msg = "value is too low."
    elif error == "typeStr":
        _msg = "needed type 'string'."
    elif error == "typeInt":
        _msg = "needed type 'int'."
    elif error == "typeFloat":
        _msg = "needed type 'float'."
    elif error == "range":
        _msg = "out of range."
    elif error == "dnu":
        _msg = "did not understand."
    else:
        _msg = "got bad variable"

    # var 'msg' is an addon message, default ''
    # space is necessary so doesnt have to be manually added eveywheree
    printadv(_msg + " " + msg)

    if method is None:  # default
        sleepadv(1)
    elif method == "input":  # for longer independent readings
        inputadv("[enter] to leave")

    if returnArea is not None:
        return returnArea


# fore
fCol = {
    "blue": cf.BLUE,
    "light blue": cfx.MALIBUBLUE,
    "black": cfg.GRAY2,
    "true black": cfg.BLACK,
    "white": cfg.WHITE,
    "gray": cfg.GRAY16,
    "cyan": cfx.ROBINBLUE,
    "green": cf.GREEN,
    "light cyan": cfx.BRIGHTTURQUISE,
    "light green": cfx.GREEN_EX,
    "light magenta": cfx.PINKFLAMINGO,
    "pink": cfx.RAZZLEDAZZLE,
    "light yellow": cfx.LASERLEMON,
    "magenta": cfx.MAGENTA,
    "red": cfx.RED,
    "light gray": cfg.GRAY20,
    "yellow": cfx.YELLOW,
    "purple": cfx.ELECTRICVIOLET,
    "light purple": cfx.ELECTRICVIOLETLIGHT_EX,
    "orange": cfx.ORANGEPEEL,
    "light orange": cfx.NEONCARROT,
    "none": cs.RESET_ALL,
}
# back
bCol = {
    "blue": cb.BLUE,
    "light blue": cbx.MALIBUBLUE,
    "black": cbg.GRAY2,
    "true black": cbg.BLACK,
    "white": cbg.WHITE,
    "gray": cbg.GRAY16,
    "cyan": cbx.ROBINBLUE,
    "green": cb.GREEN,
    "light cyan": cbx.BRIGHTTURQUISE,
    "light green": cbx.GREEN_EX,
    "light magenta": cbx.PINKFLAMINGO,
    "pink": cbx.RAZZLEDAZZLE,
    "light yellow": cbx.LASERLEMON,
    "magenta": cbx.MAGENTA,
    "red": cbx.RED,
    "light gray": cbg.GRAY20,
    "yellow": cbx.YELLOW,
    "purple": cbx.ELECTRICVIOLET,
    "light purple": cbx.ELECTRICVIOLETLIGHT_EX,
    "orange": cbx.ORANGEPEEL,
    "light orange": cbx.NEONCARROT,
    "none": cs.RESET_ALL,
}

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
caret1 = (
    confData["caretFore"] + confData["caretBack"] + confData["caret"] + cs.RESET_ALL
)
caret2 = "↓"
caret3 = "↓"
caret4 = "↓"

# shorter keybind var, dynamic
w = confData["up"]
a = confData["left"]
s = confData["down"]
d = confData["right"]
z = confData["select"]
x = confData["cancel"]
c = confData["misc"]
_keybindList = [w, a, s, d, z, x, c]

# settings keywords (long)
settingsKeywords = [
    "text",
    "text speed",
    "speed",
    "caret",
    "caret color",
    "color",
    "save cap",
    "save list cap",
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
settingsPage = 1
page3Extra = ""
rebound = False
currentConfData = ""

# credits var
credPage = 1

# file
saveFileList = []
_saveFileList = []
_currentSave = ""
_loadData = ""
saveNeeded = cs.RESET_ALL  # on default, does not affect color
currentSave = 0
filePage = 1
fileRangeMin = 0
saveNum = len(sv.saveDirListFiltered)
if saveNum < confData["saveListCap"]:
    fileRangeMax = len(sv.saveDirListFiltered)
else:
    fileRangeMax = confData["saveListCap"]
breakOut = False


def fileFunc():
    """runs whenever file is picked"""
    global _currentSave, currentSave, _loadData, breakOut, fileRangeMin, fileRangeMax, filePage, prevP, nextP
    clearAll()
    # printadv(sv.saveDirListFiltered)
    printadv(f"{cbg.WHITE}{cfg.BLACK}// [files]{cs.RESET_ALL}")

    # nextprevp logic
    if filePage == 1:
        nextP = True
        prevP = False
    if type(filePage / confData["saveListCap"]) is not int:
        nextP = False
        prevP = True
    if type(filePage / confData["saveListCap"]) is not int and filePage == 1:
        nextP = False
        prevP = False
    else:
        nextP = True
        prevP = True

    # next/prev page
    statement = ""
    if prevP:
        statement += "<<"
    else:
        statement += "##"
    statement += f" page {filePage} ({fileRangeMin}-{fileRangeMax - 1}) "
    if nextP:
        statement += ">>"
    else:
        statement += "##"
    printadv(statement)

    # split .json off
    _saveFileList = os.listdir("savefiles")
    saveFileList = []
    for i in range(len(_saveFileList) % confData["saveListCap"]):
        if _saveFileList[i].startswith("savefile"):
            # REALLY weird looking but just cuts the .json off
            saveFileList.append(os.path.splitext(_saveFileList[i])[0])

    if len(sv.saveDirListFiltered) == 0:
        printadv("use 'c' to start a new file.")
    else:
        # list printadvs
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
                if data.get("kingdom", ""):
                    name = data.get("kingdom", "").get("name", "")
                    gold = data.get("kingdom", "").get("gold", 0)
                else:
                    name = ""
                    gold = 0

                # add mark
                if displayIndex == currentSave:
                    _currentSave = "*"
                    printadv(
                        f"{displayIndex}{_currentSave}: {fileName}{spacingGray}-{cs.RESET_ALL}"
                        f"'{name}', {gold} gold"
                    )
                else:
                    _currentSave = ""
                    printadv(
                        f"{displayIndex}{_currentSave}: {fileName}{spacingGray}--{cs.RESET_ALL}"
                        f"'{name}', {gold} gold"
                    )
                # either has 1 or 2 dashes to be lined up
                # 0*. savefile0-'abc'
                # 1. savefile1--'abc'

    printadv("")
    choice = inputadv(f"[#] [{z}] [{x}] [{c}] [help]")
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
        # collapsable
    if choice == "help":
        printadv(
            f"[<]: previous page (also use {a})\n"
            f"[>]: next page (also use {d})\n"
            f"[<<]: first page\n"
            f"[>>]: last page\n"
            f"[{z}]: continue\n"
            f"[{x}]: exit\n"
            f"[{c}]: new file\n"
        )

        inputadv("[enter] to leave")
    elif choice in [a, "prev", "previous", "<"] and prevP:
        fileRangeMin -= confData["saveListCap"]
        fileRangeMax -= confData["saveListCap"]
        filePage -= 1
    elif choice in [d, "next", ">"] and nextP:
        fileRangeMin += confData["saveListCap"]
        fileRangeMax += confData["saveListCap"]
        filePage += 1
    elif choice == "<<":
        filePage = 1
        # collapsable
    elif choice == ">>":
        while True:
            if not nextP:
                break
            filePage += 1
    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        printadv("that page is unavailable (unavailable pages are marked by #'s)")
        sleepadv(1.5)
    elif choice == x:
        clearAll()
        return None
    # load
    elif choiceInt:
        currentSave = choice
        _loadData = sv.load("savefiles", currentSave, confData["loadMsg"])
        _loadData["data"]["timesPlayed"] += 1
        breakOut = True

        sleepadv(1)
        clearAll()
        return
    elif choice in [z, "*"] or not choice:
        _loadData = sv.load("savefiles", currentSave, confData["loadMsg"])
        _loadData["data"]["timesPlayed"] += 1
        breakOut = True

        sleepadv(1)
        clearAll()
        return
    # new file
    elif choice == c:
        if "conf.json" not in _saveFileList:
            sv.save(sv.defaultConfig, "conf", msg=False)
        sv.save(sv.defaultData, saveNum, msg=confData["saveMsg"])
        currentSave = saveNum

        sleepadv(1)

    # goes here after command is processed
    return fileFunc()


def settingsFunc():
    # recursive settings function
    global nextP, prevP, settingsPage, page3Extra, saveFileList, _saveFileList, saveNeeded, rebound, currentConfData
    global w, a, s, d, z, x, c
    clearAll()

    # printadv(confData)
    # printadv('new-----------------current)
    # printadv(currentConfData)

    printadv(f"{cbg.WHITE}{cfg.BLACK}// [settings]{cs.RESET_ALL}")

    # printadv pages
    if settingsPage == 1:
        nextP = True
        prevP = False
        page3Extra = ""
        rebound = False

        caretColorlessPlaceholder = confData["caretColorless"]
        caretColoredPlaceholder = (
            confData["caretFore"]
            + confData["caretBack"]
            + confData["caretColorless"]
            + cs.RESET_ALL
        )
        if not confData["caretColorless"]:
            caretColorlessPlaceholder = "#"
            caretColoredPlaceholder = "#"

        printadv(
            "## page 1 - customization >>\n"
            f"1. text speed:{spacingGray}--{cs.RESET_ALL}{confData['textSpeed']}\n"
            f"2. caret{spacingGray}--------{cs.RESET_ALL}{caretColorlessPlaceholder}\n"
            f"3. caret color:{spacingGray}-{cs.RESET_ALL}{caretColoredPlaceholder}\n"
            f"4. save cap:{spacingGray}----{cs.RESET_ALL}{confData['saveListCap']}\n"
        )
        # gotta be a better way to do this spacing
    elif settingsPage == 2:
        nextP = True
        prevP = True
        page3Extra = ""

        saveMsgPlaceholder = confData["saveMsg"]
        loadMsgPlaceholder = confData["loadMsg"]
        newDayMsgPlaceholder = confData["newDayMsg"]
        actionMsgPlaceholder = confData["actionMsg"]
        if not confData["saveMsg"]:
            saveMsgPlaceholder = "#"
        if not confData["loadMsg"]:
            loadMsgPlaceholder = "#"
        if not confData["newDayMsg"]:
            newDayMsgPlaceholder = "#"
        if not confData["actionMsg"]:
            actionMsgPlaceholder = "#"

        printadv(
            "<< page 2 - messages >>\n"
            f"1. save message:{spacingGray}----{cs.RESET_ALL}{saveMsgPlaceholder}\n"
            f"2. load message:{spacingGray}----{cs.RESET_ALL}{loadMsgPlaceholder}\n"
            f"3. new day message:{spacingGray}-{cs.RESET_ALL}{newDayMsgPlaceholder}\n"
            f"4. action message:{spacingGray}--{cs.RESET_ALL}{actionMsgPlaceholder}\n"
        )
    elif settingsPage == 3:
        nextP = False
        prevP = True
        page3Extra = " only"  # added to choice input (numbers only!)
        rebound = True  # goes backwards
        printadv(
            "<< page 3 - keybinds ##\n"
            f"1. up:{spacingGray}-----{cs.RESET_ALL}[{confData['up']}]\n"
            f"2. left:{spacingGray}---{cs.RESET_ALL}[{confData['left']}]\n"
            f"3. down:{spacingGray}---{cs.RESET_ALL}[{confData['down']}]\n"
            f"4. right:{spacingGray}--{cs.RESET_ALL}[{confData['right']}]\n"
            f"5. select:{spacingGray}-{cs.RESET_ALL}[{confData['select']}]\n"
            f"6. cancel:{spacingGray}-{cs.RESET_ALL}[{confData['cancel']}]\n"
            f"7. misc:{spacingGray}---{cs.RESET_ALL}[{confData['misc']}]\n"
        )
    # choice with dynamic variables based on page
    choice = inputadv(
        f"[<] [>] [#{page3Extra}] [{x}] [{saveNeeded}{c}{cs.RESET_ALL}] [help]"
    ).strip()

    # see if choice is type(int)
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
        # collapsable
    if choice == "help":
        printadv(
            f"[<]: previous page (also use {a})\n"
            f"[>]: next page (also use {d})\n"
            f"[<<]: first page\n"
            f"[>>]: last page\n"
            f"[{x}]: exit\n"
            f"[{c}]: save changes\n"
        )
        inputadv("[enter] to leave")
    elif choice in ["next", ">", d] and nextP or not rebound and not choice.strip():
        settingsPage += 1
        # collapsable
    elif (
        choice in ["prev", "previous", "<", a]
        and prevP
        or rebound
        and not choice.strip()
    ):
        settingsPage -= 1
        # collapsable
    elif choice == "<<":
        settingsPage = 1
        # collapsable
    elif choice == ">>":
        settingsPage = 3
        # collapsable

    # HERE!!! if choice is an integer or in the settings keywords...
    elif choiceInt or choice in settingsKeywords:

        # pg 1. customization
        if settingsPage == 1:
            # text spd
            if choice in ["1", "text", "text speed", "speed"]:
                settingsChoice = inputadv(
                    "makes the text move faster or slower - default: 1\n"
                    "speed multipliers: [1/8-2] [;]"
                )
                try:
                    float(eval(settingsChoice))
                    choiceFloat = True
                except ValueError:
                    choiceFloat = False
                except SyntaxError:
                    choiceFloat = False

                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif choiceFloat and 1 / 8 <= float(eval(settingsChoice)) <= 2:
                    confData["textSpeed"] = float(eval(settingsChoice))
                    printadv(f"speed set to {confData['textSpeed']}.\n")
                    sleepadv(1)
                elif (
                    choiceFloat
                    and 1 / 8 > float(eval(settingsChoice))
                    or choiceFloat
                    and 2 < float(eval(settingsChoice))
                ):
                    huh("range", msg="min:0.125, max:2")
                else:
                    huh("typeFloat")

            # caret type
            elif choice in ["2", "caret"]:
                settingsChoice = inputadv(
                    "change the caret of every input statement - default: >\n"
                    "[-, ->, *...] [;]\n"
                )
                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                else:
                    confData["caret"] = settingsChoice
                    confData["caretColorless"] = settingsChoice
                    printadv(f"caret set to {confData['caret']}.\n")
                    sleepadv(1)

            # caret color
            elif choice in ["3", "caret color", "color"]:
                printadv(
                    "changes the front and back of the caret - default: none, none\n"
                    "[foreground, background] [;]\n"
                )
                for i in range(2):
                    foregroundChoice = ""
                    backgroundChoice = ""
                    if i == 0:
                        foregroundChoice = inputadv("foreground:").strip()
                    elif i == 1:
                        backgroundChoice = inputadv("background:").strip()

                    if foregroundChoice == ";" or backgroundChoice == ";":
                        saveNeeded = cs.RESET_ALL
                        break
                    elif foregroundChoice in fCol:
                        printadv(
                            f"set foreground to {fCol[foregroundChoice]}{foregroundChoice}{cs.RESET_ALL}.\n"
                        )
                        confData["caretFore"] = fCol[foregroundChoice]
                        sleepadv(1)
                    elif backgroundChoice in bCol:
                        printadv(
                            f"set background to {bCol[backgroundChoice]}{fCol['white']}{backgroundChoice}{cs.RESET_ALL}.\n"
                        )
                        confData["caretBack"] = bCol[backgroundChoice]
                        sleepadv(1)
                    else:
                        huh(
                            error="dnu",
                            returnArea=None,
                            method="input",
                            msg=" use colors:\n"
                            "[white] [black] / [red] [orange] [yellow] [green] [blue] [purple] +[light]",
                        )
                        break

            # savelistcap
            elif choice in ["4", "save cap", "save list cap"]:
                settingsChoice = inputadv(
                    "changes the amount of files per page in the files menu - default: 4\n"
                    "[1-10] [;]\n"
                )
                try:
                    int(settingsChoice)
                    choiceInt = True
                except ValueError:
                    choiceInt = False
                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif not choiceInt:
                    huh("typeStr", "")
                elif 1 <= int(settingsChoice) <= 10 and choiceInt:
                    confData["saveListCap"] = int(settingsChoice)
                    printadv(f"save list cap changed to {settingsChoice}.")
                    sleepadv(1)
                elif int(settingsChoice) > 10:
                    huh("range", "", msg="max:10")
                elif int(settingsChoice) < 1:
                    huh("range", "", msg="min:1")

        # pg 2. messages
        elif settingsPage == 2:
            # save message

            # on success, lowercase mssages to make it non case-sensitive
            # also lowercase variable names so .format() is compatible

            if choice in ["1", "save", "save message"]:
                settingsChoice = inputadv(
                    "edit the save message - default: 'file {saveNum} saved.'\n"
                    "[{saveNum}: save number] [blank: remove message] [;]\n"
                )

                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif not settingsChoice.strip():
                    printadv("messages removed.\n")
                    confData["saveMsg"] = ""
                    sleepadv(1)
                elif settingsChoice.strip():
                    # before defining...
                    try:
                        settingsChoice.format(
                            savenum=saveNum
                        )  # itll fail to define this if savenum is faulty
                    except KeyError:
                        printadv(
                            "check if you misspelled 'savenum'."
                        )  # maybe make this more descriptive?
                        sleepadv(1)
                        return
                    printadv(f"message added.\n")
                    confData["saveMsg"] = settingsChoice.lower()
                    sleepadv(1)

                else:
                    huh("dnu", "")

            # load message
            if choice in ["2", "load", "load message"]:
                settingsChoice = inputadv(
                    "edit the load message - default: 'file {saveNum} loaded.'\n"
                    "[{saveNum}: save number] [blank: remove message] [;]\n"
                )
                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif not settingsChoice.strip():
                    printadv("messages removed.\n")
                    confData["loadMsg"] = ""
                    sleepadv(1)
                elif settingsChoice.strip():
                    # before defining...
                    try:
                        settingsChoice.format(
                            savenum=saveNum
                        )  # itll fail to define this if day is faulty
                    except KeyError:
                        printadv(
                            "check if you misspelled 'day'."
                        )  # maybe make this more descriptive?
                        sleepadv(1)
                        return
                    printadv(f"message added.\n")
                    confData["loadMsg"] = settingsChoice.lower()
                    sleepadv(1)
                else:
                    huh("dnu", "")

            # new day message
            if choice in ["3", "new day message", "day message", "end message", "end"]:
                settingsChoice = inputadv(
                    "edits the 'day is ending' messages - default: 'the day is ending...'\n"
                    "[{day}: day number] [blank: remove messages] [;]\n"
                )
                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif not settingsChoice.strip():
                    printadv("messages removed.\n")
                    confData["newDayMsg"] = ""
                    sleepadv(1)
                elif settingsChoice.strip():
                    # before defining...
                    try:
                        settingsChoice.format(
                            day=_loadData["day"]
                        )  # itll fail to define this if savenum is faulty
                    except KeyError:
                        printadv(
                            "check if you misspelled 'day'."
                        )  # maybe make this more descriptive?
                        sleepadv(1)
                        return
                    printadv(f"message added.\n")
                    confData["newDayMsg"] = settingsChoice.lower()
                    sleepadv(1)
                else:
                    huh("dnu", "")

            # act message
            if choice in ["4", "action message", "action", "act"]:
                settingsChoice = inputadv(
                    "edits the action message - default: 'what is your action?'\n"
                    "[{act}: actions remaining] [blank: remove messages] [;]\n"
                )
                if settingsChoice.strip() == ";":
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif not settingsChoice.strip():
                    printadv("messages removed.\n")
                    confData["actionMsg"] = ""
                    sleepadv(1)
                elif settingsChoice.strip():
                    # before defining...
                    try:
                        settingsChoice.format(
                            act=actionCount
                        )  # itll fail to define this if act is faulty
                    except KeyError:
                        printadv("check if you misspelled 'act'.")
                        sleepadv(1)
                        return  # ends before message can be written
                    printadv(f"message added.\n")
                    confData["actionMsg"] = settingsChoice.lower()
                    sleepadv(1)

        # pg 3. keybinds
        elif settingsPage == 3:

            _keybindList = [w, a, s, d, z, x, c]
            keybindList = ""
            for i in range(len(_keybindList)):
                keybindList += _keybindList[i]
            # rebuilds keybindlist without additional ''''' everywhere
            # ['hi', 'guys', 'my', 'name', 'is', 'snapple']

            if choice in ["1", "up"]:
                settingsChoice = inputadv(
                    "edit keybind 'up' - default: w\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == w:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'up' set to '{settingsChoice}'.")
                    confData["up"] = settingsChoice
                    w = settingsChoice
                    sleepadv(1)
                elif not settingsChoice:
                    printadv(f"'up' set to 'w'.")
                    confData["up"] = "w"
                    w = "w"
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["2", "left"]:
                settingsChoice = inputadv(
                    "edit keybind 'left' - default: a\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == a:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'left' set to '{settingsChoice}'.")
                    confData["left"] = settingsChoice
                    a = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["3", "down"]:
                settingsChoice = inputadv(
                    "edit keybind 'down' - default: s\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == s:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'down' set to '{settingsChoice}'.")
                    confData["down"] = settingsChoice
                    s = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["4", "right"]:
                settingsChoice = inputadv(
                    "edit keybind 'right' - default: d\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == d:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'right' set to '{settingsChoice}'.")
                    confData["right"] = settingsChoice
                    d = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["5", "select"]:
                settingsChoice = inputadv(
                    "edit keybind 'select' - default: z\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == z:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'select' set to '{settingsChoice}'.")
                    confData["select"] = settingsChoice
                    z = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["6", "cancel"]:
                settingsChoice = inputadv(
                    "edit keybind 'cancel' - default: x\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == x:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'cancel' set to '{settingsChoice}'.")
                    confData["cancel"] = settingsChoice
                    x = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

            elif choice in ["7", "misc"]:
                settingsChoice = inputadv(
                    "edit keybind 'misc' - default: c\n" f"![{keybindList}] [;]"
                )
                if settingsChoice == ";" or settingsChoice == c:
                    saveNeeded = cs.RESET_ALL
                    return settingsFunc()
                elif settingsChoice not in keybindList:
                    printadv(f"'misc' set to '{settingsChoice}'.")
                    confData["misc"] = settingsChoice
                    c = settingsChoice
                    sleepadv(1)

                elif settingsChoice in keybindList:
                    printadv(f"keybind '{settingsChoice}' already used.")
                    sleepadv(1)

                else:
                    huh("dnu")

    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        printadv("that page is unavailable (unavailable pages are marked by #'s)")
        sleepadv(0.5)
    elif choice == x:
        clearAll()
        return None
    elif choice == c:
        # universal settings config
        sv.save(confData, "conf", confData["saveMsg"].format(savenum=saveNum))
        saveNeeded = cs.RESET_ALL  # 'none'

        # update savedirlistfiltered
        sv.saveDirListFiltered = []  # clear
        for i in range(len(os.listdir("savefiles"))):
            if sv.saveDirList[i].endswith(".json") and sv.saveDirList[i].startswith(
                "savefile"
            ):
                sv.saveDirListFiltered.append(sv.saveDirList[i])

        currentConfData = copy.deepcopy(
            confData
        )  # updates currentConfData, representative of whats in conf.json

        sleepadv(1)

    if currentConfData != confData:
        saveNeeded = fCol["yellow"]
    else:
        saveNeeded = cs.RESET_ALL

    return settingsFunc()  # goes here afterwards


def creditsFunc():
    global credPage, nextP, prevP, rebound
    clearAll()
    printadv(f"{cbg.WHITE}{cfg.BLACK}// [credits]{cs.RESET_ALL}")
    if credPage == 1:
        nextP = True
        prevP = False
        rebound = False
        printadv("## page 1 - dev >>\n" "1: pleasantBlue\n")
    elif credPage == 2:
        nextP = True
        prevP = True
        printadv("<< page 2 - contributors >>\n" "...wip\n")
    elif credPage == 3:
        nextP = False
        prevP = True
        rebound = True
        printadv("<< page 3 - special thanks ##\n" "...wip\n")
    choice = inputadv(f"[<] [>] [#] [{x}] [help]")
    try:
        int(choice)
        choiceInt = True
    except ValueError:
        choiceInt = False
    if choice == "help":
        printadv(
            f"[<]: previous page (also use {a})\n"
            f"[>]: next page (also use {d})\n"
            f"[<<] first page\n"
            f"[>>] last page\n"
            f"[{x}]: exit\n"
            f"thanks to everyone on here!\n"
            f"i hope this list grows big someday :)\n"
        )
        inputadv("[enter] to leave")
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
    elif choice == x:
        clearAll()
        return None
    elif (
        choice in ["next", ">", d]
        and not nextP
        or choice in ["prev", "previous", "<", a]
        and not prevP
    ):
        printadv("that page is unavailable (unavailable pages are marked by #'s)")
        sleepadv(1.5)
        return creditsFunc()
    elif choiceInt:
        # pg 1. dev
        if settingsPage == 1:
            printadv(
                "hi! im the main dev of this game, but i dont like talking about myself very much...\n"
                "its kinda my first time coding (emphasis on 'kinda'), so... i try :)\n"
            )
            inputadv("[enter] to leave")
    elif not choice and not rebound:
        credPage += 1
    elif not choice and rebound:
        credPage -= 1
    return creditsFunc()


def quitFunc():
    clearAll()
    printadv(f"{cbg.WHITE}{cfg.BLACK}// [quit]{cs.RESET_ALL}")
    printadv("thanks for playing!")
    sleepadv(1)
    clearAll()
    sys.exit()


# gameloop var
loadData = _loadData
actionCount = 3


def gameInit(stdscr):
    # clear, refresh, block cursor
    crs.curs_set(2)
    stdscr.clear()
    stdscr.refresh()

    # instant key response
    stdscr.nodelay(False)
    stdscr.keypad(True)

    # colors
    crs.start_color()
    crs.init_pair(1, crs.COLOR_WHITE, crs.COLOR_BLACK)  # white/blck
    if _loadData == sv.defaultData:  # if the loaded data is equal to the base data
        stdscr.addstr(0, 0, 'welcome to medievalKingdom! to start, type "help".')
    else:
        stdscr.addstr(0, 0, confData["actionMsg"])
    stdscr.refresh()
    stdscr.getch()


def gameLoop(act=actionCount):
    for _ in range(act):
        # if command == "help":
        #     pass # to~do once settings menu is finished...
        clearAll()
        act -= 1


# start!
while True:
    clearAll()

    printadv(f"{cbg.WHITE}{cfg.BLACK}// [medievalKingdom]{cs.RESET_ALL}")
    printadv(
        f"{caret1} [files]\n"
        f"{caret2} [settings]\n"
        f"{caret3} [credits]\n"
        f"{caret4} [quit]"
    )
    choice = inputadv("")
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
            filePage = 1
            fileFunc()
        elif currentCaret == 2:
            settingsPage = 1
            rebound = False
            currentConfData = copy.deepcopy(confData)  # static variable
            settingsFunc()
        elif currentCaret == 3:
            credPage = 1
            rebound = False
            creditsFunc()
        elif currentCaret == 4:
            quitFunc()
    # quit
    elif choice == x:
        quitFunc()
        # collapsable
    if breakOut:
        gameInit(stdscr=crs.initscr())
        crs.wrapper(gameInit)
        gameLoop()
        break
    # can be optimized when i learn how to
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
# sz16, cascadia semibold -> 48*208

#
