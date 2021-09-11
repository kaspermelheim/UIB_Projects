from socket import socket

from task2 import response

if __name__ == "__main__":
    sock = socket()
    sock.bind(("localhost", 12000))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        while True:
            request_message = conn.recv(1024)
            if not request_message:
                conn.close()
                break
            conn.sendall(response(request_message.decode()).encode())
