import socket

def sendData(data):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        addr = ("192.168.4.1",80)
        print(addr)
        s.connect(addr) 
        message = bytes(data,'utf-8')
        s.sendall(message)
        print(str(s.recv(4096),'utf-8'))
    except Exception as e:
        print(e,'!!!')
        pass
    finally:
        s.close()
    return