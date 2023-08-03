from pyscreeze import pixel
import keyboard
import time
from timeit import default_timer as timer

def check_and_press_key(x,y,key):
    pixel_1 = pixel(x,y)
    pixel_2 = pixel(x,y-95) # 115

    if pixel_1[0] == 255:
        keyboard.press(key)
        time.sleep(0.01)
        keyboard.release(key)
    elif pixel_2[0] == 117:
        keyboard.press(key)
    elif pixel_1[0] == 37 and pixel_2[0] != 117:
        keyboard.press(key)
        time.sleep(0.01)
        keyboard.release(key)
    else: 
        keyboard.release(key)