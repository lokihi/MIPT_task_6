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
def dac1():
    value = 0
    i=7
    while (i >= 0):
        voltageDelta = 2**i
        bin2dac(value+voltageDelta)
        voltage = (voltageDelta + value)/256*maxVoltage
        time.sleep(0.001)
        comparatorValue = GPIO.input(4)
        if comparatorValue==1:
            value = value+voltageDelta
        i = i-1
    
    print("Digital value: {:^3}, Analog value: {:.2f}".format(value,voltage))
try:
    while True:
        dac1()
finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")