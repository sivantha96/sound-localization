import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

DO = 18
AO = 4

GPIO.setup(DO,GPIO.IN)
GPIO.setup(AO,GPIO.IN)

COUNT = 0
while True: 
    DO_VALUE = GPIO.input(DO)
    AO_VALUE = GPIO.input(AO)
    print(COUNT)
    COUNT = COUNT + 1
    print('Digital:{}'.format(DO_VALUE))
    print('Analogue:{}'.format(AO_VALUE))
    time.sleep(1)

