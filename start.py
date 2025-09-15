# import keyboard as k
from utils import helpers as h
# from utils import save as s
currentSave = 0

# ↑↓←→
currentCaret = 1
caret1 = h.settings["caret"]
caret2 = "↓"
caret3 = "↓"
caret4 = "↓"

# settings keywords
settingsKeywords = ["text", "text speed", "speed", "caret", "save", "save message", "load", "load message",
                    "new day message", "day message", "end message", "end", "action message", "action", "act",
                    "up", "left", "down", "right", "select", "cancel", "misc"]
numbersList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# shorter keybind var
w = h.settings["up"]
a = h.settings["left"]
s = h.settings["down"]
d = h.settings["right"]
z = h.settings["select"]
x = h.settings["cancel"]
c = h.settings["misc"]
keybindList = [w, a, s, d, z, x, c]

# settings var
nextP = False
prevP = False
page = 1

# credits var
credPage = 1
# nextP and prevP carry on with credits page

def fileFunc():
    h.clearAll()
    print("// [files]")
    choice = h.inputadv("[save] [load] [help]")
    if choice == "help":
        h.clearAll()
        print(f"use [help], [save], [load], [#], and [{x}/quit]...\n"
              "to navigate and configure the save file menu.\n")
        choice = h.inputadv("[enter] to leave")
        if choice:
            return fileFunc()
    elif choice in [x, "quit"]:
        h.clearAll()
    else:
        print("did not understand.\n")
        h.sleepadv(1)
        return fileFunc()
def settingsFunc():
    global nextP, prevP, page
    h.clearAll()
    print("// [settings]")
    if page == 1:
        nextP = True
        prevP = False
        print("## page 1 - customization >>\n"
              f"1. text speed: {h.settings["textSpeed"]}\n"
              f"2. caret: '{h.settings["caret"]}'\n")
    elif page == 2:
        nextP = True
        prevP = True
        print("<< page 2 - messages >>\n"
              f"1. save message: {h.settings["saveMsg"]}\n"
              f"2. load message: {h.settings["loadMsg"]}\n"
              f"3. new day message: {h.settings["newDayMsg"]}\n"
              f"4. action message: {h.settings["actionMsg"]}\n")
    elif page == 3:
        nextP = False
        prevP = True
        print("<< page 3 - keybinds ##\n"
              f"1. up: [{w}]\n"
              f"2. left: [{a}]\n"
              f"3. down: [{s}]\n"
              f"4. right: [{d}]\n"
              f"5. select: [{z}]\n"
              f"6. cancel: [{x}]\n"
              f"7. misc: [{c}]\n"
              f"[: exit] [< prev] [> next]\n")
        print(keybindList)
    choice = h.inputadv("[<] [>] [#] [help]")
    if choice == "help":
        h.clearAll()
        print("use [help], [next/>], [prev/<], [#], and [x/quit]...\n"
              "to navigate and configure the settings menu.\n")
        choice = h.inputadv("[enter] to leave")
        if choice:
            return settingsFunc()
    elif choice in ["next", ">", d] and nextP is not False:
        page += 1
        return settingsFunc()
    elif choice in ["prev", "previous", "<", a] and prevP is not False:
        page -= 1
        return settingsFunc()
    elif choice in numbersList or choice in settingsKeywords:
        # pg 1. customization
        if page == 1:
            # text spd
            if choice in ["1", "text", "text speed", "speed"]:
                settingsChoice = h.inputadv("makes the text move faster or slower - default: 1\n"
                                            "speed multipliers: [0] [0.25], [0.5], [1], [2], [3]\n")
                if settingsChoice in [0, 0.25, 0.5, 1, 2, 3]:
                    h.settings["textSpeed"] = float(settingsChoice)
                    print(f"speed set to {h.settings["textSpeed"]}.\n")
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print("did not understand.")
                    h.sleepadv(1)
                    return settingsFunc()
            # caret type
            elif choice in ["2", "caret"]:
                settingsChoice = h.inputadv("change the caret of every input statement - default: >\n"
                                            "examples: ->, -, o\n"
                                            "note: the newline and extra space after the caret are given automatically.\n")
                h.settings["caret"] = settingsChoice
                print(f"caret set to {h.settings["caret"]}.\n")
                h.sleepadv(1)
                return settingsFunc()
        # pg 2. messages
        elif page == 2:
            # save message
            if choice in ["1", "save", "save message"]:
                settingsChoice = h.inputadv(
                    "edit the save message - default: 'file {saveNum} saved.'\n"
                    "[{saveNum}: save number] [blank: remove message]\n")
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    h.settings["saveMsg"] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    h.settings["saveMsg"] = ""
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print("did not understand.")
                    h.sleepadv(1)
                    return settingsFunc()
            # load message
            if choice in ["2", "load", "load message"]:
                settingsChoice = h.inputadv(
                    "edit the load message - default: 'file {saveNum} loaded.'\n"
                    "[{saveNum}: save number] [blank: remove message]\n")
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    h.settings["loadMsg"] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    h.settings["loadMsg"] = ""
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print("did not understand.")
                    h.sleepadv(1)
                    return settingsFunc()
            # new day message
            if choice in ["3", "new day message", "day message", "end message", "end"]:
                settingsChoice = h.inputadv("edits the 'day is ending' messages - default: 'the day is ending...'\n"
                                                  "[{day}: day number] [blank: remove messages]\n")
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    h.settings["newDayMsg"] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    h.settings["newDayMsg"] = ""
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print("did not understand.")
                    h.sleepadv(1)
                    return settingsFunc()
            # act message
            if choice in ["4", "action message", "action", "act"]:
                settingsChoice = h.inputadv("edits the action message - default: 'what is your action?'\n"
                                            "[blank: remove messages]\n")
                if settingsChoice != "":
                    print(f"message '{settingsChoice}' added.\n")
                    h.settings["newDayMsg"] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()

                elif settingsChoice.strip() == "":
                    print("messages removed.\n")
                    h.settings["newDayMsg"] = ""
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print("did not understand.")
                    h.sleepadv(1)
                    return settingsFunc()
        # pg 3. keybinds
        elif page == 3:
            if choice in ["1", "up"]:
                settingsChoice = h.inputadv("edit keybind 'up' - default: w\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'up' set to '{settingsChoice}'.")
                    h.settings[w] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["2", "left"]:
                settingsChoice = h.inputadv("edit keybind 'left' - default: a\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'left' set to '{settingsChoice}'.")
                    h.settings[a] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["3", "down"]:
                settingsChoice = h.inputadv("edit keybind 'down' - default: s\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'down' set to '{settingsChoice}'.")
                    h.settings[s] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["4", "right"]:
                settingsChoice = h.inputadv("edit keybind 'right' - default: d\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'right' set to '{settingsChoice}'.")
                    h.settings[d] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["5", "select"]:
                settingsChoice = h.inputadv("edit keybind 'select' - default: z\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'select' set to '{settingsChoice}'.")
                    h.settings[z] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["6", "cancel"]:
                settingsChoice = h.inputadv("edit keybind 'cancel' - default: x\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'cancel' set to '{settingsChoice}'.")
                    h.settings[x] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
            elif choice in ["7", "misc"]:
                settingsChoice = h.inputadv("edit keybind 'misc' - default: c\n"
                                            f"can't use: [{keybindList}]")
                if settingsChoice != keybindList:
                    print(f"'misc' set to '{settingsChoice}'.")
                    h.settings[c] = settingsChoice
                    h.sleepadv(1)
                    return settingsFunc()
                else:
                    print(f"keybind {settingsChoice} already used.")
                    h.sleepadv(1)
                    return settingsFunc()
    elif choice in ["next", ">", d] and not nextP or choice in ["prev", "previous", "<", a] and not prevP:
        print("that page is unavailable (unavailable pages are marked by #'s)")
        h.sleepadv(1.5)
        return settingsFunc()
    elif choice in ["quit", "x", ":"]:
        h.clearAll() # exits
        # collapsable
    else:
        print("did not understand.")
        h.sleepadv(1)
        return settingsFunc()
def creditsFunc():
    global credPage, nextP, prevP
    h.clearAll()
    print("// [credits]")
    if credPage == 1:
        nextP = True
        prevP = False
        print("## page 1 - dev >>\n"
              "1: pleasantBlue")
    elif credPage == 2:
        nextP = True
        prevP = True
        print("<< page 2 - contributors >>\n"
              "...wip")
    elif credPage == 3:
        nextP = False
        prevP = True
        print("<< page 3 - special thanks ##\n"
              "...wip")
    choice = h.inputadv("[<] [>] [help]")
    if choice == "help":
        h.clearAll()
        print("use [help], [next/>], [prev/<], and [x/quit]...\n"
              "to navigate the credits menu. thanks to everyone on here!\n")
        choice = h.inputadv("[enter] to leave")
        if choice:
            return creditsFunc()
    elif choice in ["next", ">", d] and nextP is not False:
        credPage += 1
        return creditsFunc()
    elif choice in ["prev", "previous", "<", a] and prevP is not False:
        credPage -= 1
        return creditsFunc()
    elif choice in ["x", "quit"]:
        h.clearAll()
        # collapsable
    elif choice in ["next", ">", d] and not nextP or choice in ["prev", "previous", "<", a] and not prevP:
        print("that page is unavailable (unavailable pages are marked by #'s)")
        h.sleepadv(1.5)
        return creditsFunc()
    elif choice in ["1"]:
        # pg 1. dev
        if page == 1:
            print("hi! im the main dev of this game, but i dont like talking about myself very much...\n")

    else:
        print("did not understand.")
        h.sleepadv(1)
        return creditsFunc()
def quitFunc():
    print("// [quit]")
    h.clearAll()
    # s.save()
    print("thanks for playing!")
    h.sleepadv(1)
    h.clearAll()
    quit()

# start func
while True:
    h.clearAll()
    print(f"{caret1} [files]\n"
          f"{caret2} [settings]\n"
          f"{caret3} [credits]\n"
          f"{caret4} [quit]")
    choice = h.inputadv("")
    # down
    if choice == s:
        if currentCaret == 1:
            currentCaret += 1
            caret1 = "↑"
            caret2 = h.settings["caret"]
        elif currentCaret == 2:
            currentCaret += 1
            caret2 = "↑"
            caret3 = h.settings["caret"]
        elif currentCaret == 3:
            currentCaret += 1
            caret3 = "↑"
            caret4 = h.settings["caret"]
        elif currentCaret == 4:
            pass
    # up
    elif choice == w:
        if currentCaret == 1:
            pass
        elif currentCaret == 2:
            currentCaret -= 1
            caret2 = "↓"
            caret1 = h.settings["caret"]
        elif currentCaret == 3:
            currentCaret -= 1
            caret3 = "↓"
            caret2 = h.settings["caret"]
        elif currentCaret == 4:
            currentCaret -= 1
            caret4 = "↓"
            caret3 = h.settings["caret"]
    # select
    elif choice == z:
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
        #collapsable



