import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

D1 = 21
D2 = 20
D3 = 16

A1 = 26
A2 = 19
A3 = 13

GPIO.setup(D1, GPIO.IN)
GPIO.setup(D2, GPIO.IN)
GPIO.setup(D3, GPIO.IN)
GPIO.setup(A1, GPIO.IN)
GPIO.setup(A2, GPIO.IN)
GPIO.setup(A3, GPIO.IN)

COUNT = 0

while True:
    D1_VAL = GPIO.input(D1)
    D2_VAL = GPIO.input(D2)
    D3_VAL = GPIO.input(D3)
    A1_VAL = GPIO.input(A1)
    A2_VAL = GPIO.input(A2)
    A3_VAL = GPIO.input(A3)
    
    print(COUNT)
    COUNT = COUNT + 1
    
    print('D1 : {}'.format(D1_VAL))
    print('D2 : {}'.format(D2_VAL))
    print('D3 : {}'.format(D3_VAL))
    print('A1 : {}'.format(A1_VAL))
    print('A2 : {}'.format(A2_VAL))
    print('A3 : {}'.format(A3_VAL))
    time.sleep(0.25)
    
    
    
