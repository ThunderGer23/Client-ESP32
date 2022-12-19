import network
from config.inter import internet
from src.sendData import sendData
from src.pinSelector import sensorSelector

sta_if = network.WLAN(network.STA_IF)
sta_if = internet(sta_if)

def main():    
    while True:
        for i in range(0, 15):
            Sensor = sensorSelector(i)
            sendData(str(Sensor))