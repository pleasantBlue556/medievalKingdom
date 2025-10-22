from colorama_ex.ansi_ex_fore import Fore, Fore_EX, Fore_Gray

for i in range(3):
    colorlist = []
    if i == 0:
        colorlist = Fore.__dict__.items()
    elif i == 1:
        colorlist = Fore_EX.__dict__.items()
    elif i == 2:
        colorlist = Fore_Gray.__dict__.items()
    for name, value in colorlist:
        if not name.startswith("__") and not callable(value):
            print(f"\033[{value}{name}\033[0m")
