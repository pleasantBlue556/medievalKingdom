from colorama_ex.ansi_ex_fore import Fore, Fore_EX, Fore_Gray

for name, value in Fore.__dict__.items():
    if not name.startswith('__') and not callable(value):
        print(f"\033[{value}{name}\033[0m")

for name, value in Fore_EX.__dict__.items():
    if not name.startswith('__') and not callable(value):
        print(f"\033[{value}{name}\033[0m")

for name, value in Fore_Gray.__dict__.items():
    if not name.startswith('__') and not callable(value):
        print(f"\033[{value}{name}\033[0m")


