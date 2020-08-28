from multiprocessing import Process, Array
import time
import pyaudio
import audioop
from multiprocessing import Pool, Lock
import pandas as pd
# from model.dnn_1 import model_1

# time delay between each process ~ 0.0003s

sampling_format = pyaudio.paInt16
sampling_channels = 1
sampling_rate = 44100
chunk = 4096
devList = [2, 3, 4]

    
audio = pyaudio.PyAudio()

def listen(dev):
    # setup of the device get passed down
    stream = audio.open(format = sampling_format, rate = sampling_rate, channels = sampling_channels, \
                        input_device_index = dev, input = True, \
                        frames_per_buffer = chunk)
    print("recording")
    if dev == dev_1:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list[0] = rms
    elif dev == dev_2:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list[1] = rms
    elif dev == dev_3:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list[2] = rms
        
def initArray(list):
    list = list

if __name__ == "__main__":
    # setup the lock
    # lock = Lock()
    
    # array to hold values of microphones
    list = Array('i', range(3), lock=False)
    
    # getting microphone numbers
     info = audio.get_host_api_info_by_index(0)
     num = info.get('deviceCount')
     count = 0
     for i in range(0, num):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')):
            str = audio.get_device_info_by_host_api_device_index(0, i).get('name')
            check = "Audio" in str
            if(check):
                devList[count] = i
                count = count + 1
    
    # setting microphone numbers
    dev_1 = devList[0]
    dev_2 = devList[1]
    dev_3 = devList[2]
    
    # creating a pool of 3 workers
    pool = Pool(processes = 3, initializer=initArray, initargs=(list,))
    
    # mapping each worker to the function listen
    pool.map_async(listen, [dev_1, dev_2, dev_3])
    
    # array to hold the inputs values
    input = []
    
    # outside worker to make predictions
    while True:
        time.sleep(0.5)
        for m in range(3):
            input.append(list[m])
        
        # predict the peak
        output = model_1.predict(input)
        
        # rotate
        