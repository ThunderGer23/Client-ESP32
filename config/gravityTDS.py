from machine import Pin, ADC

VREF = 3.3 
averageVoltage = 3;


def sensorTDS(selector):    
    TdsSensor = ADC(Pin(selector))
    TdsSensor.atten(ADC.ATTN_11DB)
    
    compensationVolatge = averageVoltage/TdsSensor.read()
    compensVol = compensationVolatge* compensationVolatge
    tdsValue = (133.42 * compensVol * compensationVolatge - 255.86 * compensVol + 857.39 * compensationVolatge) * 0.5;
    return tdsValue
# TODO: Implementar OneWire de https://how2electronics.com/aquarium-water-quality-monitor-with-tds-sensor-esp32/#Source_CodeProgram