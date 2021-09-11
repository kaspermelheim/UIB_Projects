#Import socket
from socket import socket, AF_INET, SOCK_DGRAM

#New socket
sock = socket(AF_INET, SOCK_DGRAM)

#Check inputs from users
while ((text := input('> ').lower()) != "shut down"):
    if(text == "GET"):
        sock.sendto(text.encode(), ("localhost", 55555))
        msg, addr = sock.recvfrom(2048)
        print(msg.decode())
    else:
        print("Unknown command. Type 'GET' to retrieve all data.")