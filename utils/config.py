from colorama import init as coloramaInit
from colorama_ex.ansi_ex_back import Back as cb
from colorama_ex.ansi_ex_fore import Fore as cf

coloramaInit(autoreset=True)

settings = {
    # page 1
    "textSpeed": 1,
    "caretColorless": ">",
    "caret": ">",
    "caretFore": cf.LIGHTWHITE_EX,
    "caretBack": cb.BLACK,
    "saveListCap": 4,
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
