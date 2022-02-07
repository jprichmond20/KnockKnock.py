
#SimpleClient

from socket import *

def simpleClient(location):

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

    client.send(("\t" + response + " who?").encode("ascii"))
    print("\t" + response + " who?")
    msg = client.recv(1024)
    response = msg.decode("ascii")

    print(response)

    client.close()

simpleClient(input("Enter hostname:: "))
