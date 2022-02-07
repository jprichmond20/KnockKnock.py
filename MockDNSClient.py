
#SimpleClient

from socket import *

def simpleClient(location):
    def getIPAddress():
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        return s.getsockname()[0]
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((location, 2001))
    client.send(("pi-106," + getIPAddress()).encode("ascii"))
    msg = client.recv(1024)
    msg = msg.decode("ascii")
    print(msg)
    client.send(input("ok or who (name) ex: who pi-106"))
    msg = client.recv(1024)
    response = msg.decode("ascii")
    print(response)

    client.close()

simpleClient(input("Enter hostname:: "))
