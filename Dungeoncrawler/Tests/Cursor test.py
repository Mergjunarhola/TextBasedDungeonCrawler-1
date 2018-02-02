

from ctypes import windll, byref
from ctypes.wintypes import SMALL_RECT

STDOUT = -11

hdl = windll.kernel32.GetStdHandle(STDOUT)
rect = SMALL_RECT(0, 50, 50, 80) # (left, top, right, bottom)
windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))




from ctypes import windll, Structure, c_long, byref
import time

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def MousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


while True:
    print(MousePosition())
    time.sleep(1)
