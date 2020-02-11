from multiprocessing import Process
import time
import pyaudio
import audioop
from multiprocessing import Pool

# time delay between each process ~ 0.0003s

sampling_format = pyaudio.paInt16
sampling_channels = 1
sampling_rate = 44100
chunk = 4096
dev_1 = 2
dev_2 = 3
dev_3 = 4
audio = pyaudio.PyAudio()

def listen(dev):
    stream = audio.open(format = sampling_format, rate = sampling_rate, channels = sampling_channels, \
                        input_device_index = dev, input = True, \
                        frames_per_buffer = chunk)
    print("recording")
    if dev == 2:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            print("\n" + str(dev-1) + " - " + str(rms))
    elif dev == 3:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            print(str(dev-1) + " - " + str(rms))
    else:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            print(str(dev-1) + " - " + str(rms))

def run_process(process):
    process.start()
    
if __name__ == "__main__":
    pool = Pool(processes = 3)
    pool.map(listen, [dev_1, dev_2, dev_3])