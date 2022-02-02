
#SimpleClient

from socket import *

def simpleClient(location):

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((location, 2000))
    outgoing = "asdf?"
    msg = client.recv(1024)
    msg = msg.decode("ascii")
    if msg == "Knock-Knock":
        client.send("   Who's there?".encode('ascii'))
    else:
        print("Error")
        client.send("Error".encode("ascii"))
        client.close()
    msg = client.recv(1024)
    response = msg.decode('ascii')
    print(response)

    client.close()

simpleClient("172.16.212.44")
