from pynput.keyboard import Key, Listener


def on_release(key):
    if key == Key.space:
        print("end")
        listener.stop()
    else:
        print("continue")

with Listener(on_release=on_release) as listener:
    listener.join()