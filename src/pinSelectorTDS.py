from machine import Pin
from time import sleep
from config.gravityTDS import sensorTDS
# Setting up the pins on the ESP32.
SW = [Pin(5, Pin.OUT), Pin(6, Pin.OUT), Pin(7, Pin.OUT), Pin(8, Pin.OUT)]

def sensorTDSSelector(item):
    selector = bin(item).replace('0b', '0') if (item <8) else bin(item).replace('0b', '')
    for i in range(0,3):
        SW[i].value = selector[i]
        sleep(0.1)
    sleep(0.1)    
    return sensorTDS(35)