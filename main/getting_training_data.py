from multiprocessing import Process, Pipe, Value, Lock
import time
import pyaudio
import audioop
import pandas as pd

audio = pyaudio.PyAudio()

# the function to measure and send volumes from a given microphone
def listen(mic, mic_left, mic_shared, lock):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    vol_arr = [0,0,0,0,0]
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        lock.acquire()
        vol_arr[0] = vol_arr[1]
        vol_arr[1] = vol_arr[2]
        vol_arr[2] = vol_arr[3]
        vol_arr[3] = vol_arr[4]
        vol_arr[4] = rms
        avg = ( vol_arr[1] + vol_arr[2] + vol_arr[3] ) / 3.0
        if avg > vol_arr[0] and avg > vol_arr[4]:
            print("peak")
        mic_shared.value = rms
        lock.release()
        # mic_left.send(rms)
        # time.sleep(0.5)

# the function to receive volumes and manipulate
def stream(mic1_right, mic2_right, mic3_right, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    array_A = []
    array_B = []
    array_C = []
    count = 0
    while True:
        # val1 = mic1_right.recv()
        # val2 = mic2_right.recv()
        # val3 = mic3_right.recv()
        lock_A.acquire()
        lock_B.acquire()
        lock_C.acquire()
        array_A.append(mic_A.value)
        array_B.append(mic_B.value)
        array_C.append(mic_C.value)
        print(str(count) + '=' + str(mic_A.value) + '-' + str(mic_B.value) + '-' + str(mic_C.value))
        lock_B.release()
        lock_C.release()
        lock_A.release()
        time.sleep(0.1)
        count = count + 1
        if count == 5000:
            break
    data = {'col1': array_A, 'col2': array_B, 'col3': array_C}
    df = pd.DataFrame(data=data)
    df.to_csv("output.csv")

# main function
if __name__ == "__main__":
    # define pipes to share data between processes
    mic1_left, mic1_right = Pipe()
    mic2_left, mic2_right = Pipe()
    mic3_left, mic3_right = Pipe()

    mic_A = Value('d')
    mic_B = Value('d')
    mic_C = Value('d')

    lock_A = Lock()
    lock_B = Lock()
    lock_C = Lock()

    # define 4 processes to run on each core (note - Pi have only 4 cores)
    p2 = Process(target=listen, args=(1, mic2_left, mic_B, lock_B))
    p1 = Process(target=listen, args=(0, mic1_left, mic_A, lock_A))
    p3 = Process(target=listen, args=(2, mic3_left, mic_C, lock_B))
    p4 = Process(target=stream, args=(mic1_right, mic2_right, mic3_right, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C))

    # starting the execution of each process
    p4.start()
    p2.start()
    p1.start()
    p3.start()
    p4.join()
    p2.join()
    p1.join()
    p3.join()
