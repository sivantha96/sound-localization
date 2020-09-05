from multiprocessing import Process, Value
import pyaudio
import sys
import time
from pynput.keyboard import Key, Listener
sys.path.append('/home/pi/Documents/Projects/sound-localization')

from helper_functions import get_threshold

audio = pyaudio.PyAudio()

# the function to measure and send volumes from a given microphone
def listen(mic, should_stop):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    threshold = get_threshold(stream, should_stop)
    print('\nmic ' + str(mic) + ' threshold:' + str(threshold))
    
    while True:
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
        
def localize(num, should_stop, listener):
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
    
    p1 = Process(target=listen, args=(0, should_stop))
    p2 = Process(target=listen, args=(1, should_stop))
    p3 = Process(target=listen, args=(2, should_stop))
    p4 = Process(target=localize, args=(3, should_stop, listener))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
