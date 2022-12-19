#This is a refactor the original library to Micropython version for the implementation in this module

#  DFRobot Gravity: Analog TDS Sensor/Meter
#  <https://www.dfrobot.com/wiki/index.php/Gravity:_Analog_TDS_Sensor_/_Meter_For_Arduino_SKU:_SEN0244>
 
#  This sample code shows how to read the tds value and calibrate it with the standard buffer solution.
#  707ppm(1413us/cm)@25^c standard buffer solution is recommended.
 
#  Created 2018-1-3
#  By Jason <jason.ling@dfrobot.com@dfrobot.com>
 
#  GNU Lesser General Public License.
#  See <http://www.gnu.org/licenses/> for details.
#  All above must be included in any redistribution.
from machine import Pin
ReceivedBufferLength = 15
TdsFactor = 0.5 # tds = ec / 2

class GravityTDS(object):
    
    pin = None
    aref = 3.0  # default 5.0V on Arduino UNO, 3.0 in ESP32
    adcRange = None
    temperature = None
    kValueAddress = None #the address of the K value stored in the EEPROM
    # cmdReceivedBuffer[ReceivedBufferLength+1] #store the serial cmd from the serial monitor
    cmdReceivedBufferIndex = ''
 
    kValue = 0      # k value of the probe,you can calibrate in buffer solution ,such as 706.5ppm(1413us/cm)@25^C 
    analogValue = 0
    voltage = 0
    ecValue = 0 #before temperature compensation
    ecValue25 = 0 #after temperature compensation
    tdsValue = 0

    

    def GravityTDS():
        pin = Pin(35, Pin.INPUT)
        temperature = 25.0
        aref = 5.0
        adcRange = 1024.0
        kValueAddress = 8
        kValue = 1.0
