









"""
Test module color_console (Python 3.0). Does not work with Python 2.6.
"""

import color_console as cons
import sys

def test():
  """Simple Pyton 3.0 test for color_console."""
  default_colors = cons.get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  cons.set_text_attr(cons.FOREGROUND_BLUE | default_bg |
                     cons.FOREGROUND_INTENSITY)
  print('===========================================')
  cons.set_text_attr(cons.FOREGROUND_BLUE | cons.BACKGROUND_GREY |
                cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)
  print('And Now for Something', end=' ')
  sys.stdout.flush() # Force writing first part of the line in blue
  cons.set_text_attr(cons.FOREGROUND_RED | cons.BACKGROUND_GREY |
                cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)
  print('Completely Different!')
  cons.set_text_attr(default_colors)
  cons.set_text_attr(cons.FOREGROUND_RED | default_bg |
                     cons.FOREGROUND_INTENSITY)
  print('===========================================')
  cons.set_text_attr(default_colors)

if __name__ == "__main__":
  test()




input()









"""
import os
import sys
import ctypes

ENABLE_VIRTUAL_TERMINAL_INPUT =0x0200
ctypes.WINFUNCTYPE()

kernel32 = ctypes.windll.kernel32
ctypes.c_ulong().value |= ENABLE_VIRTUAL_TERMINAL_INPUT

sys.stdout.write("\033[33mYellow Submarine")
sys.stderr.write("\033[31mred, red , wine!")
print ("\x1b[2;32mhello \x1b[1;31mworld\x1b[0m")
input()
os.system("cls")
input()

"""



"""
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
input()
"""