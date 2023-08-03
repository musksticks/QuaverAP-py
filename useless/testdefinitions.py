import keyboard
from useless.grabPixel import fast_get_pixel
import time

def check_and_press_key(x, y, key):
    pixel_1 = fast_get_pixel(x, y)

    if pixel_1[0] == 252 or pixel_1[0] == 166:
        keyboard.press(key)
    else: 
        keyboard.release(key)

