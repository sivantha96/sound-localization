import threading
import time

def printThread(name):
    while True:
        time.sleep(0.25)
        print(name)

if __name__ == "__main__":
    t1 = threading.Thread(target = printThread, args=(1,))
    t1.start()
    t2 = threading.Thread(target = printThread, args=(2,))
    t2.start()