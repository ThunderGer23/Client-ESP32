import network
from config.inter import internet
from src.sendData import sendData
from src.pinSelectorTurbiedad import sensorTurbiedadSelector
from src.pinSelectorTDS import sensorTDSSelector
sta_if = network.WLAN(network.STA_IF)
sta_if = internet(sta_if)

def main():    
    while True:
        for i in range(0, 15):
            sensor = sensorTurbiedadSelector(i)
            NTU = -(1120.4 * sensor* sensor) + (5742.3* sensor)-4352.9
            tds = sensorTDSSelector(i)
            sendData('Sensor '+ str(i)+ ' valor' + str(NTU)+ ', tds: '+ str(tds))