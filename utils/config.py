from colorama import init as coloramaInit, Fore as cf, Back as cb, Style as cs
coloramaInit(autoreset=True)
settings = {
    # page 1
    "textSpeed": 1,
    "caretColorless": '>',
    "caret": ">",
    "caretFore": cf.WHITE,
    "caretBack": cb.BLACK,
    # page 2
    "actionMsg": "what is your action? ",
    "saveMsg": "file {saveNum} saved.",
    "loadMsg": "file {saveNum} loaded.",
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
settings['caret'] = (settings['caretFore'] + settings['caretBack']
                     + settings['caret'] + cs.RESET_ALL)
