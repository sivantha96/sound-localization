import multiprocessing
import time
import pyaudio
import audioop
import pandas as pd


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
DEV_LIST = [ 2, 3, 4]

audio = pyaudio.PyAudio()
manager = multiprocessing.Manager()
sound_values = multiprocessing.Array('i', range(3))
sound_values[0] = 0
sound_values[1] = 0
sound_values[2] = 0

def listen(dev, sound_values):
    stream = audio.open(format = FORMAT, rate = RATE,channels = CHANNELS, input_device_index = dev, input = True,frames_per_buffer = CHUNK)
    if dev == 2:
        while True:
            data = stream.read(CHUNK, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            sound_values[0] = rms
            
    elif dev == 3:
        while True:
            data = stream.read(CHUNK, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            value = rms / 12
            sound_values[1] = int(value)
            
    elif dev == 4:
        while True:
            data = stream.read(CHUNK, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            sound_values[2] = rms
            
def print_val(dev, sound_values):
    while True:
            print(str(sound_values[0]) + "," + str(sound_values[1]) + "," + str(sound_values[2]))
            time.sleep(5)

process1 = multiprocessing.Process(target=listen, args=(2, sound_values))
process2 = multiprocessing.Process(target=listen, args=(3, sound_values))
process3 = multiprocessing.Process(target=listen, args=(4, sound_values))
process4 = multiprocessing.Process(target=print_val, args=(1, sound_values))

process1.start()
process2.start()
process3.start()
process4.start()
process1.join()
process2.join()
process3.join()
process4.join()