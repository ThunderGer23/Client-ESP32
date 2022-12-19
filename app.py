import network
from config.inter import internet
from src.sendData import sendData
from src.pinSelector import sensorTurbiedadSelector

sta_if = network.WLAN(network.STA_IF)
sta_if = internet(sta_if)

def main():    
    while True:
        for i in range(0, 15):
            sensor = sensorTurbiedadSelector(i)
            NTU = -(1120.4 * sensor* sensor) + (5742.3* sensor)-4352.9
            sendData('Sensor '+ str(i)+ ' valor' + str(NTU))