import RPi.GPIO as GPIO
import time
dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
maxVoltage = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(17,GPIO.OUT,initial =GPIO.HIGH)
GPIO.setup(4,GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal=decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
try:
    while True:
        for i in range(256):
            signal=bin2dac(i)
            voltage = i/256*maxVoltage
            time.sleep(0.0001)
            comparatorValue = GPIO.input(4)
            if comparatorValue==0:
                print("Digital value: {:^3}, Analog value: {:.2f}".format(i,voltage))
                break
            
            
        

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")