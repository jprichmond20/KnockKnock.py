
#SimpleClient

from socket import *
import random

def simpleClient(location):
    numC = 0
    done = False
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((location, 2023))
    #outgoing = "asdf?"
    msg = client.recv(1024)
    msg = msg.decode("ascii")
    if msg == "Knock-Knock":
        print(msg)
        client.send("\tWho's there?".encode('ascii'))
        print("\tWho's there?")
    else:
        print("Error")
        client.send("Error".encode("ascii"))
        client.close()

    msg = client.recv(1024)
    response = msg.decode('ascii')
    print(response)
    if response == "Banana":
        while not done:
            numC = random.randint(0,10)
            if numC > 7:
                client.send(("\t" + response + " WHO!?").encode("ascii"))
                msg = client.recv(1024)
                response = msg.decode('ascii')
                print(response)
                client.send(("\t" + response + " who?").encode("ascii"))
                msg = client.recv(1024)
                response = msg.decode('ascii')
                print(response)
                client.close()
            else:
                client.send(("\t" + response + " who?").encode("ascii"))
                msg = client.recv(1024)
                response = msg.decode('ascii')
                print(response)
    else:
        client.send(("\t" + response + " who?").encode("ascii"))
        print("\t" + response + " who?")
        msg = client.recv(1024)
        response = msg.decode("ascii")

    print(response)

    client.close()

simpleClient(input("Enter hostname:: "))
