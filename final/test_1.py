from multiprocessing import Process
import time
import pyaudio
import audioop

def listen(mic, mic_left):
    audio = pyaudio.PyAudio()
    stream = audio.open(format = pyaudio.paInt16, rate = 44100, channels = 1, input_device_index = mic, input = True, frames_per_buffer = 4096)
    while True:
        data = stream.read(chunk, exception_on_overflow = False)
        rms = audioop.rms(data, 2)
        mic_left.send(rms)

def stream(mic1_right, mic2_right, mic3_right):
    while True:
        val1 = mic1_right.recv()
        val2 = mic2_right.recv()
        val3 = mic3_right.recv()
        print(str(val1) + '-' + str(val2) + '-' + str(val3))


if __name__ == "__main__":
    mic1_left, mic1_right = Pipe()
    mic2_left, mic2_right = Pipe()
    mic3_left, mic3_right = Pipe()
    p1 = Process(target=listen, args=(2, mic1_left,))
    p2 = Process(target=listen, args=(3, mic2_left,))
    p3 = Process(target=listen, args=(4, mic3_left,))
    p3 = Process(target=stream, args=(mic1_right, mic2_right, mic3_right))