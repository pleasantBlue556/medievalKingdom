import curses as crs
from colorama import Style as cs
stdscr = crs.initscr()

def inputadv(msg="", caret='>'):
    crs.curs_set(2)
    stdscr.clear()
    inp = ''
    if caret:
        stdscr.addstr(0, 0, f"{msg}\n{caret}{cs.RESET_ALL} ")
    else:
        stdscr.addstr(f"{msg}\n{cs.RESET_ALL} ", 0, 0)
    ch = stdscr.getch()
    while True:
        if ch in [10, 13]: #10 is \n or enter and 13 is \r
            break
        elif ch in [crs.KEY_BACKSPACE, 127, 8]:
            if len(inp) > 0:
                inp = inp[:-1]
                stdscr.addstr(0, len(msg), + len(inp) + ' ')
                stdscr.move(0, len(msg) + len(inp))
        elif 32 <= ch <= 126: # printable ascii
            inp += chr(ch)
            stdscr.addstr(0, len(msg), inp)

    stdscr.refresh()
    crs.curs_set(0)
    return inp

def main(stdscr=crs.initscr()):
    name = inputadv('whats ur name')
    stdscr.clear()
    stdscr.addstr(1, 1, f"hello {name}.")
    stdscr.refresh()
    stdscr.getch()

crs.wrapper(main)