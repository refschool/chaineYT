import time
import curses

def blinkon(stdscr):
        # First frame
        stdscr.addstr(0, 0, "====*====\n")
        stdscr.addstr(1, 0, "==== ====\n")
        stdscr.refresh()
        time.sleep(0.5)
        stdscr.clear()

def blinkoff(stdscr):

        # Second frame
        stdscr.addstr(0, 0, "==== ====\n")
        stdscr.addstr(1, 0, "====*====\n")
        stdscr.refresh()
        time.sleep(0.5)
        stdscr.clear()


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    while True:
        blinkon(stdscr)
        blinkoff(stdscr)


curses.wrapper(main)
