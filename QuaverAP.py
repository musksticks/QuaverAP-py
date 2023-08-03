from definitions import check_and_press_key
from threading import Thread
import keyboard

while True:

    # CREATE THREADS
    a = Thread(target=check_and_press_key, args=(748, 900, 'a'))
    s = Thread(target=check_and_press_key, args=(890, 900, 's'))
    d = Thread(target=check_and_press_key, args=(1032, 900, 'd'))
    f = Thread(target=check_and_press_key, args=(1174, 900, 'f'))

    # START THREADS
    a.start()
    s.start()
    d.start()
    f.start()

    # SYNC THREADS
    a.join()
    s.join()
    d.join()
    f.join()

    # SAFETY
    if keyboard.is_pressed("q"):
        break