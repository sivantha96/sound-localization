import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
MAX_TIME = 0.04

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.01)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start = time.time()
    timeout = start + MAX_TIME
    while GPIO.input(ECHO) == False and start<timeout:
        start = time.time()
        time.sleep(0.00001)
     
    end = time.time()
    timeout = start + MAX_TIME 
    while GPIO.input(ECHO) == True and end<timeout:
        end = time.time()
        time.sleep(0.00001)
    
    signal_time = end - start

    distance = signal_time / 0.000058
    
    print('Distance: {} cm'.format(distance))
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        print('Stooped by user')
        
    
