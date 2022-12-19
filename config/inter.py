import time
from docs.messages import conectado, accessPoint, password

def internet(sta_if):
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect(accessPoint, password)
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        time.sleep_ms(100)
        continue
    print(conectado)
    return sta_if