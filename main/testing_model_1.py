from multiprocessing import Process, Value, Lock
import pyaudio
import sys
import time
import audioop
import pandas as pd
from threading import Thread
from keras.models import model_from_json
from pynput.keyboard import Key, Listener
sys.path.append('/home/pi/Documents/Projects/sound-localization')
from helper_functions import get_threshold, get_encoder, predict_category

# the function to measure and send volumes from a given microphone
def listen(mic, should_stop, shared_mic, lock):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    print('initializing mic ' + str(mic))
    threshold = get_threshold(stream, should_stop)
    if threshold > 600:
        threshold = threshold + 30
    print('mic '+ str(mic) +' threshold acquired')
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        if rms > threshold:
            lock.acquire()
            shared_mic.value = rms
            lock.release()
        if should_stop.value == 1:
            break
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
    # set the categories
    categories = pd.DataFrame(['AB', 'AC', 'BC'])

    # get the encoder
    encoder = get_encoder(categories)

    # open model.json
    json_file = open('/home/pi/Documents/Projects/sound-localization/model.json', 'r')
    model_json = json_file.read()
    json_file.close()

    # load model
    model = model_from_json(model_json)
    model.load_weights("/home/pi/Documents/Projects/sound-localization/model.h5")

    # compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    print("Model is ready")
    time.sleep(20)
    timer = 20
    while True:
        print('starting to listen  in '+ str(timer) +' seconds ...')
        time.sleep(1)
        timer = timer - 1
        if timer == 0:
            break
    while True:
        lock_A.acquire()
        lock_B.acquire()
        lock_C.acquire()
        if mic_A.value != 0 or mic_B.value != 0 or mic_C.value != 0:
            print(predict_category(model, encoder, mic_A.value, mic_B.value, mic_C.value))
            mic_A.value = 0
            mic_B.value = 0
            mic_C.value = 0
            time.sleep(0.1)
        lock_B.release()
        lock_C.release()
        lock_A.release()
        time.sleep(0.6)
        if should_stop.value == 1:
            break
    print('\nthread '+ str(num) + ' stopped')

def keyboard_listen(num, should_stop, listener):
    time.sleep(10)
    print('listening to keyboard...')
    try:
        listener.start()
        listener.join()
    finally:
        listener.stop()
    print('\nthread '+ str(num) + ' stopped')

def main_process(num, should_stop, listener, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    t1 = Thread(target=localize, args=(1, should_stop, listener, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C))
    t2 = Thread(target=keyboard_listen, args=(2, should_stop, listener))
    t2.start()
    t1.start()
    
    t2.join()
    t1.join()
    
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
    
    mic_A.value = 0
    mic_B.value = 0
    mic_B.value = 0

    lock_A = Lock()
    lock_B = Lock()
    lock_C = Lock()

    p1 = Process(target=listen, args=(0, should_stop, mic_A, lock_A))
    p2 = Process(target=listen, args=(1, should_stop, mic_B, lock_B))
    p3 = Process(target=listen, args=(2, should_stop, mic_C, lock_C))
    p4 = Process(target=main_process, args=(3, should_stop, listener, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
