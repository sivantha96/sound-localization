import time
import pyaudio
import audioop
from multiprocessing import Pool, Lock, Process, Array
import pandas as pd

# time delay between each process ~ 0.0003s

sampling_format = pyaudio.paInt16
sampling_channels = 1
sampling_rate = 44100
chunk = 4096
devList = [ 2, 3, 4]

    
audio = pyaudio.PyAudio()

def listen(dev):
    stream = audio.open(format = sampling_format, rate = sampling_rate, channels = sampling_channels, \
                        input_device_index = dev, input = True, \
                        frames_per_buffer = chunk)
    print("recording")
    count = 0
    if dev == dev_1:
        for j in range(10):
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list_1[count] = rms
            count = count + 1
            print(rms)
    elif dev == dev_2:
        for j in range(10):
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list_2[count] = rms
            count = count + 1
            print(rms)
    elif dev == dev_3:
        for j in range(10):
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            list_3[count] = rms
            count = count + 1
            print(rms)
        
def initArray(list_1, list_2, list_3):
    list_1 = list_1
    list_2 = list_2
    list_3 = list_3

if __name__ == "__main__":
    lock = Lock()
    list_1 = Array('i', range(1000), lock=False)
    list_2 = Array('i', range(1000), lock=False)
    list_3 = Array('i', range(1000), lock=False)
    
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
                
    dev_1 = devList[0]
    dev_2 = devList[1]
    dev_3 = devList[2]  
    pool = Pool(processes = 3, initializer=initArray, initargs=(list_1, list_2, list_3))
    pool.map_async(listen, [dev_1, dev_2, dev_3])
    time.sleep(10)
    print("--------------------------")
    # d = {'col1': list_1.value, 'col2': list_2.value, 'col3': list_3.value}
    # df = pd.DataFrame(data=d)
    # print(df)
    arr_1 = []
    for x in list_1:
        arr_1.append(x)
        
    arr_2 = []
    for x in list_2:
        arr_2.append(x)
        
    arr_3 = []
    for x in list_3:
        arr_3.append(x)
        
    d = {'col1': arr_1, 'col2': arr_2, 'col3': arr_3}
    df = pd.DataFrame(data=d)
    df.to_csv("output.csv")