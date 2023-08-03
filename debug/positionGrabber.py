import pyautogui
import time
import keyboard
import win32api, win32con

while True:
    x,y = pyautogui.position()
    print(x,y)

# 1 700,980
# 2 875,980
# 3 1050,980
# 4 1210,980, 869

#def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.01)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)