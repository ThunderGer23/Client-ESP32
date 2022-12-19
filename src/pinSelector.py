from machine import Pin, ADC
from time import sleep

# Setting up the ADC (Analog to Digital Converter) on the ESP32.
Sensor = ADC(Pin(34))
Sensor.atten(ADC.ATTN_11DB)

# Setting up the pins on the ESP32.
SW = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

def sensorSelector(item):
    if (item <8):
        selector = bin(item).replace('0b', '0')
    else:
        selector = bin(item).replace('0b', '')
    for i in range(0,3):
        SW[i].value = selector[i]
        sleep(0.1)
    sleep(0.1)    
    return Sensor.read()