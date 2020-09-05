from multiprocessing import Process, Pipe, Value, Lock
import time
import pyaudio
import audioop
import pandas as pd

audio = pyaudio.PyAudio()

def get_distance(t_A, t_B, t_C):
    m_1 = t_A - t_C
    m_2 = t_C - t_B
    m_3 = t_A - t_B
    
    

# the function to measure and send volumes from a given microphone
def listen(mic_id,t, m, l):
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=mic_id, input=True, frames_per_buffer=4096)
    vol_arr = [0,0,0,0,0]
    threshold = 100
    t.send(0)
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        vol_arr[0] = vol_arr[1]
        vol_arr[1] = vol_arr[2]
        vol_arr[2] = vol_arr[3]
        vol_arr[3] = vol_arr[4]
        vol_arr[4] = rms
        l.acquire()
        m.value = rms
        l.release()
        avg = ( vol_arr[1] + vol_arr[2] + vol_arr[3]) / 3.0
        if avg > vol_arr[0] and avg > vol_arr[4] and avg > threshold:
            t.send(time.time())

# the function to receive volumes and manipulate
def stream(time_A, time_B, time_C, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    t_A = 0
    t_B = 0
    t_C = 0
    while True:
        if t_A != time_A.recv() or t_B != time_B.recv() or t_C != time_C.recv():
            t_A = time_A.recv()
            t_B = time_B.recv()
            t_C = time_C.recv()
            lock_A.acquire()
            lock_B.acquire()
            lock_C.acquire()
            m_A = mic_A.value
            m_B = mic_B.value
            m_C = mic_C.value
            lock_A.release()
            lock_B.release()
            lock_C.release()
            print("time " + ' = ' + str(t_A) + ' - ' + str(t_B) + ' - ' + str(t_C))
            print("volume " + ' = ' + str(m_A) + ' - ' + str(m_B) + ' - ' + str(m_C))

# main function
if __name__ == "__main__":
    # define pipes to share data between processes
    time_A_left, time_A_right = Pipe()
    time_B_left, time_B_right = Pipe()
    time_C_left, time_C_right = Pipe()
    
    mic_A = Value('d')
    mic_B = Value('d')
    mic_C = Value('d')

    lock_A = Lock()
    lock_B = Lock()
    lock_C = Lock()

    # define 4 processes to run on each core (note - Pi have only 4 cores)
    p2 = Process(target=listen, args=(1, time_A_left, mic_A, lock_A))
    p1 = Process(target=listen, args=(0, time_B_left, mic_B, lock_B))
    p3 = Process(target=listen, args=(2, time_C_left, mic_C, lock_C))
    p4 = Process(target=stream, args=(time_A_right, time_B_right, time_C_right, mic_A,
                                      mic_B, mic_C, lock_A, lock_B, lock_C))

    # starting the execution of each process
    p4.start()
    p2.start()
    p1.start()
    p3.start()
    p4.join()
    p2.join()
    p1.join()
    p3.join()

