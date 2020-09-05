from multiprocessing import Process, Pipe, Value, Lock
import time
import pyaudio
import audioop
import pandas as pd
import numpy as np

audio = pyaudio.PyAudio()

# the function to measure and send volumes from a given microphone


def listen(mic):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    stop_threshold_time = time.time() + 10
    threshold_array = np.zeros((20,), dtype=int)
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        if rms < 10:
            threshold_array[0] = threshold_array[0] + 1
        elif rms < 20:
            threshold_array[1] = threshold_array[1] + 1
        elif rms < 30:
            threshold_array[2] = threshold_array[2] + 1
        elif rms < 40:
            threshold_array[3] = threshold_array[3] + 1
        elif rms < 50:
            threshold_array[4] = threshold_array[4] + 1
        elif rms < 60:
            threshold_array[5] = threshold_array[5] + 1
        elif rms < 70:
            threshold_array[6] = threshold_array[6] + 1
        elif rms < 80:
            threshold_array[7] = threshold_array[7] + 1
        elif rms < 90:
            threshold_array[8] = threshold_array[8] + 1
        elif rms < 100:
            threshold_array[9] = threshold_array[9] + 1
        elif rms < 110:
            threshold_array[10] = threshold_array[10] + 1
        elif rms < 120:
            threshold_array[11] = threshold_array[11] + 1
        elif rms < 130:
            threshold_array[12] = threshold_array[12] + 1
        elif rms < 140:
            threshold_array[13] = threshold_array[13] + 1
        elif rms < 150:
            threshold_array[14] = threshold_array[14] + 1
        elif rms < 160:
            threshold_array[15] = threshold_array[15] + 1
        elif rms < 170:
            threshold_array[16] = threshold_array[16] + 1
        elif rms < 180:
            threshold_array[17] = threshold_array[17] + 1
        elif rms < 190:
            threshold_array[18] = threshold_array[18] + 1
        else:
            threshold_array[19] = threshold_array[19] + 1
        if stop_threshold_time < time.time():
            break
    stream.stop_stream()
    stream.close()
    audio.terminate()
    threshold = (np.argmax(stop_threshold_time) + 1)*10
    print('mic' + str(mic) + ' threshold:' + str(threshold))

# main function
if __name__ == "__main__":
    p1 = Process(target=listen, args=(0))
    p2 = Process(target=listen, args=(1))
    p3 = Process(target=listen, args=(2))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
