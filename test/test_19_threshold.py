from multiprocessing import Process
import pyaudio
import sys
sys.path.append('/home/pi/Documents/Projects/sound-localization')

from helper_functions import get_threshold

audio = pyaudio.PyAudio()

# the function to measure and send volumes from a given microphone
def listen(mic):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    threshold = get_threshold(stream)
    print('mic' + str(mic) + ' threshold:' + str(threshold))
    stream.stop_stream()
    stream.close()
    audio.terminate()


# main function
if __name__ == "__main__":
    p1 = Process(target=listen, args=(0,))
    p2 = Process(target=listen, args=(1,))
    p3 = Process(target=listen, args=(2,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
