import threading
import time
import pyaudio
import audioop

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
    count = 0;
    sum = 0;
    if dev == 2:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            print("\n" + str(dev-1) + " - " + str(rms))
    else:
        while True:
            time.sleep(0.5)
            data = stream.read(chunk, exception_on_overflow = False)
            rms = audioop.rms(data, 2)
            print(str(dev-1) + " - " + str(rms))

if __name__ == "__main__":
    t1 = threading.Thread(target = listen, args=(dev_1,))
    t1.start()
    t2 = threading.Thread(target = listen, args=(dev_2,))
    t2.start()
    t3 = threading.Thread(target = listen, args=(dev_3,))
    t3.start()
