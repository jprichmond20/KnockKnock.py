from socket import *
import threading


def getIPAddress():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def processReq(s,addr):
    print("Connection from", addr)
    done=False
    while not done:
        #send

def cmdServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    ip = getIPAddress()
    serversocket.bind(ip,2000)
    serversocket.listen(1)
    print("Waiting on ", ip)
    while True:
        clientsocket,addr = serversocket.accept()
        threading.Thread(target=processRequest, args=(clientsocket,addr)).start()
