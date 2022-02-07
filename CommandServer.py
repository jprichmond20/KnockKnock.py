from socket import *
import threading
import random

def getIPAddress():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def processReq(clientsocket,addr,starts,punchlines):
    print("Connection from", addr)
    done = False
    while not done:
        jokeNum = random.randint(0, len(starts))
        clientsocket.send("Knock-Knock".encode("ascii"))
        print("Knock-Knock")
        msg = clientsocket.recv(1024)
        msg = msg.decode("ascii")
        if jokeNum == len(starts):
            if msg == "\tWho's there?":
                clientsocket.send("Banana".encode("ascii"))
                print("\tWho's there?")
                print(starts[jokeNum])
            else:
                print("Error...")
                clientsocket.send("Error...".encode("ascii"))
                clientsocket.close()
            msg = clientsocket.recv(1024)
            msg = msg.decode("ascii")
            print(msg)
            while msg != "\tBanana WHO!?":
                clientsocket.send("Banana".encode("ascii"))
                print("Banana")
                msg = clientsocket.recv(1024)
                msg = msg.decode("ascii")
                print(msg)
            print("Orange")
            msg = clientsocket.recv(1024)
            msg = msg.decode("ascii")
            print(msg)
            print("Orange you glad I didn't say Banana")
            clientsocket.send("Orange you glad I didn't say Banana".encode("ascii"))
            clientsocket.close()
            done = True
        else:

            if msg == "\tWho's there?":
                clientsocket.send(starts[jokeNum].encode("ascii"))
                print("\tWho's there?")
                print(starts[jokeNum])
            else:
                print("Error...")
                clientsocket.send("Error...".encode("ascii"))
                clientsocket.close()

            msg = clientsocket.recv(1024)
            msg = msg.decode("ascii")

            print(msg)

            clientsocket.send(punchlines[jokeNum].encode("ascii"))
            print(punchlines[jokeNum])

            clientsocket.close()
            done = True

def cmdServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    f = open("Starts.txt", "r")
    f2 = open("Punchlines.txt", "r")
    initial = f.readlines()
    starts = []
    initialPunch = f2.readlines()
    punchlines = []
    for thing in initial:
        starts.append(thing.strip("\n"))
    for thing in initialPunch:
        punchlines.append(thing.strip("\n"))
    ip = getIPAddress()
    serversocket.bind(ip,2000)
    serversocket.listen(1)
    print("Waiting on ", ip)
    ### USE TRY CATCH :)
    while True:
        clientsocket,addr = serversocket.accept()
        threading.Thread(target=processReq, args=(clientsocket,addr,starts,punchlines)).start()
