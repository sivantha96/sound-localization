from multiprocessing import Process, Value, Lock
import pyaudio
import sys
import time
import audioop
from pynput.keyboard import Key, Listener
sys.path.append('/home/pi/Documents/Projects/sound-localization')

from helper_functions import get_threshold

# the function to measure and send volumes from a given microphone
def listen(mic, should_stop, shared_mic, lock):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    threshold = get_threshold(stream, should_stop)
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        if rms > threshold:
            lock.acquire()
            shared_mic.value = rms
            lock.release()
        if should_stop.value == 1:
            break
        time.sleep(1)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('\nprocess '+ str(mic) + ' stopped')

def on_release(key):
    global should_stop
    global listener
    time.sleep(2)
    if key == Key.space:
        should_stop.value = 1
        listener.stop()
        
def localize(num, should_stop, listener, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    array_A = []
    array_B = []
    array_C = []
    while True:
        lock_A.acquire()
        lock_B.acquire()
        lock_C.acquire()
        if mic_A != 0 or mic_B != 0 or mic_B != 0:
            array_A.append(mic_A.value)
            array_B.append(mic_B.value)
            array_C.append(mic_C.value)
            mic_A.value = 0
            mic_B.value = 0
            mic_C.value = 0
        lock_B.release()
        lock_C.release()
        lock_A.release()
        time.sleep(1)
        if should_stop == 1:
            break
    print('\nprocess '+ str(num) + ' stopped')

def keyboard_listen(num, should_stop, listener):
    try:
        listener.start()
        listener.join()
    finally:
        listener.stop()
    print('\nprocess '+ str(num) + ' stopped')

# main function
if __name__ == "__main__":
    global should_stop
    global listener
    listener = Listener(on_release = on_release)
    should_stop = Value('d')
    should_stop.value = 0
    
    mic_A = Value('d')
    mic_B = Value('d')
    mic_C = Value('d')

    lock_A = Lock()
    lock_B = Lock()
    lock_C = Lock()

    p1 = Process(target=listen, args=(0, should_stop, mic_A, lock_A))
    p2 = Process(target=listen, args=(1, should_stop, mic_B, lock_B))
    p3 = Process(target=listen, args=(2, should_stop, mic_C, lock_C))
    p4 = Process(target=localize, args=(3, should_stop, listener, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C))
    p4 = Process(target=keyboard_listen, args=(4, should_stop, listener))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
