from definitions import check_and_press_key
from threading import Thread, Event
import keyboard


def run_check_and_press_key(x, y, key, stop_event):
    while not stop_event.is_set():
        check_and_press_key(x, y, key)


stop_event = Event()

threads = [
    Thread(target=run_check_and_press_key, args=(748, 900, 'a', stop_event)),
    Thread(target=run_check_and_press_key, args=(890, 900, 's', stop_event)),
    Thread(target=run_check_and_press_key, args=(1032, 900, 'd', stop_event)),
    Thread(target=run_check_and_press_key, args=(1174, 900, 'f', stop_event))
]

for thread in threads:
    thread.start()

try:
    while not keyboard.is_pressed("q"):
        pass
finally:
    stop_event.set()
    for thread in threads:
        thread.join()
