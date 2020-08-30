from multiprocessing import Process, Pipe, Value, Lock
import time
import pandas as pd
import matplotlib.pyplot as plt

# the function to measure and send volumes from a given microphone
def listen(mic, time_shared, mic_shared, lock):
    rms = 100
    while True:
        lock.acquire()
        mic_shared.value = rms
        time_shared = time.time()
        lock.release()
        rms = rms + 1

# the function to receive volumes and manipulate
def stream(mic1_right, mic2_right, mic3_right, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C):
    array_A = []
    array_C = []
    array_B = []
    while True:
        lock_A.acquire()
        lock_B.acquire()
        lock_C.acquire()
        array_A.append([mic_A.value, time_A.value])
        array_B.append([mic_B.value, time_B.value])
        array_C.append([mic_C.value, time_C.value])
        lock_B.release()
        lock_C.release()
        lock_A.release()
        count = count + 1
        if count == 1000:
            break

def live_plotter(y_A,y_B,y_C,t_A,line_A, t_B, t_C, init,identifier=''):
    if init == True:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig, axs = plt.subplots(1,1)
        line_A, = axs[0].plot(t_A, y_A)   
        line_B, = axs[0].plot(t_B, y_B)   
        line_C, = axs[0].plot(t_C, y_C)
        plt.ylabel('time')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line_A
    return line1

# main function
if __name__ == "__main__":

    mic_A = Value('d')
    mic_B = Value('d')
    mic_C = Value('d')
    time_A = Value('d')
    time_B = Value('d')
    time_C = Value('d')

    lock_A = Lock()
    lock_B = Lock()
    lock_C = Lock()

    # define 4 processes to run on each core (note - Pi have only 4 cores)
    p1 = Process(target=listen, args=(0, time_A, mic_A, lock_A))
    p2 = Process(target=listen, args=(1, time_B, mic_B, lock_B))
    p3 = Process(target=listen, args=(2, time_C, mic_C, lock_B))
    p4 = Process(target=stream, args=(time_A, time_B, time_C, mic_A, mic_B, mic_C, lock_A, lock_B, lock_C))

    # starting the execution of each process

    p2.start()
    p1.start()
    p3.start()
    p4.start()

    p2.join()
    p1.join()
    p3.join()
    p4.join()