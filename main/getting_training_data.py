from multiprocessing import Process, Pipe, Value, Lock
import time
import pyaudio
import audioop
import pandas as pd

audio = pyaudio.PyAudio()

# the function to measure and send volumes from a given microphone
def listen(mic, mic_left, mic_shared, lock):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic, input=True, frames_per_buffer=4096)
    stop_threshold_time = time.time() + 10
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        threshold_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    
    max_count = max(stop_threshold_time)
    threshold = stop_threshold_time.index(max_count)

    print('mic' + str(mic) + ' threshold:' + str(threshold))

    # while True:
    #     data = stream.read(4096, exception_on_overflow=False)
    #     rms = audioop.rms(data, 2)
    #     lock.acquire()
    #     vol_arr[0] = vol_arr[1]
    #     vol_arr[1] = vol_arr[2]
    #     vol_arr[2] = vol_arr[3]
    #     vol_arr[3] = vol_arr[4]
    #     vol_arr[4] = rms
    #     avg = (vol_arr[1] + vol_arr[2] + vol_arr[3]) / 3.0
    #     if avg > vol_arr[0] and avg > vol_arr[4] and avg > threshold:
    #         mic_left.send(time.time())
    #     mic_shared.value = rms
    #     lock.release()
    #     # mic_left.send(rms)
    #     # time.sleep(0.5)

# the function to receive volumes and manipulate


def stream(mic1_right, mic2_right, mic3_right, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    array_A = []
    array_B = []
    array_C = []
    count = 0
    time_A = 0
    time_B = 0
    time_C = 0
    while True:
        if time_A != mic1_right.recv() and time_B != mic2_right.recv() and time_C != mic3_right.recv():
            time_A = mic1_right.recv()
            time_B = mic2_right.recv()
            time_C = mic3_right.recv()
            print("peak " + '=' + str(time_A) + '-' +
                  str(time_B) + '-' + str(time_C))
        lock_A.acquire()
        lock_B.acquire()
        lock_C.acquire()
        array_A.append(mic_A.value)
        array_B.append(mic_B.value)
        array_C.append(mic_C.value)
        print(str(count) + '=' + str(mic_A.value) + '-' +
              str(mic_B.value) + '-' + str(mic_C.value))
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
    # p4.start()
    p2.start()
    p1.start()
    p3.start()
    # p4.join()
    p2.join()
    p1.join()
    p3.join()
