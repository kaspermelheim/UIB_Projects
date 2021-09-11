#Import socket and datetime
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime

#New socket and bind
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("localhost", 55555))

while True:
    msg, addr = sock.recvfrom(2048)
    text = msg.decode()

    if text == "GET":
        
        #Opens a file and reads from it
        with open("WeatherData.txt", 'r') as file:
            data = file.read()

        print(f"{addr[0]} sent command: {msg.decode()}")
        sock.sendto((data.encode()), addr)
    else:
        sock.sendto(("Unknown command.".encode()), addr)

