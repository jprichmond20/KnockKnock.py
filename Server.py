# SimpleServer.py
# Study http://docs.python.org/3/library/socket.html  for more info on sockets

from socket import *
import random


def simpleServer():
    # create a socket object
    #   socket is a function that returns a variable of type socket (a constructor)
    #   AF_INET is the Address Format:Internet -- you are going to connect with an IP Address
    #   SOCK_STREAM it the type of socket --- how to package the data.
    serversocket = socket(AF_INET, SOCK_STREAM)
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
    print(len(starts))
    print(len(punchlines))
    print(starts)
    print(punchlines)
    # allow your server to reuse the address instead of waiting for a timeout
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Be sure that your socket communicates on it's IP address, on a specific port
    #   The port is 2000 -- this was chosen somewhat randomly
    #   NOTE: bind takes a tuple, not two parameters.

    serversocket.bind(("172.16.212.44", 2023))

    # Start listening for requests.
    #   Argument is the size of the request buffer
    serversocket.listen(1)
    def getIPAddress():
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        return s.getsockname()[0]
    while True:
        # Block here until there is a request
        #   when you accept, you should know 2 values
        #   clientsocket and addr (who connected to you)
        print("Waiting for connection....")
        print("on " + getIPAddress() + "....")
        clientsocket, addr = serversocket.accept()
        print("Connnection from", addr)

        jokeNum = random.randint(0,len(starts)-1)

        clientsocket.send("Knock-Knock".encode("ascii"))
        print("Knock-Knock")
        msg = clientsocket.recv(1024)
        msg = msg.decode("ascii")

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


        #if msg == "Who?":
        #    print(msg)
        #    clientsocket.send("I am Groot".encode("ascii"))
        #elif msg == "Why?":
        #    print(msg)
        #    clientsocket.send("Because.".encode("ascii"))
        #elif msg == "Where?":
        #    print(msg)
        #    clientsocket.send(gethostname().encode('ascii'))
        #elif msg == "What?":
        #    print(msg)
        #    clientsocket.send("Command Server".encode("ascii"))
        #elif msg == "When?":
        #    print(msg)
        #    clientsocket.send("Hammer time".encode("ascii"))
        #else:
        #    print(msg)
        #    clientsocket.send("No hablo espanol.".encode("ascii"))



        # Send some information back to the client -
        # You don't know that another Python program connected,
        # so you have to convert your string to ASCII

        #clientsocket.send(gethostname().encode('ascii'))
        #clientsocket.close()
        #serversocket.close()


simpleServer()


