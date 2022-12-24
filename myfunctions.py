import win32api
import win32con
import pyautogui
import numpy as np
def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def dis(x, y):
    SCREEN_SIZE = tuple(pyautogui.size())
    return np.sqrt((int(SCREEN_SIZE[0]/2) - x) ** 2 + (int(SCREEN_SIZE[1]/2) - y) ** 2)
