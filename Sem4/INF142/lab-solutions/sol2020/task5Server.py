from selectors import EVENT_READ, DefaultSelector
from socket import socket

from task2 import response


def accept(sock):
    conn, address = sock.accept()
    print('accepted', conn, 'from', address)
    conn.setblocking(False)
    sel.register(conn, EVENT_READ)


def read(conn):
    request_message = conn.recv(1024)
    if not request_message:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
    else:
        conn.sendall(response(request_message.decode()).encode())


sel = DefaultSelector()
sock = socket()
sock.bind(("localhost", 12000))
sock.listen()
sock.setblocking(False)
sel.register(sock, EVENT_READ, True)

while True:
    events = sel.select()
    for key, _ in events:
        if key.data:
            accept(key.fileobj)
        else:
            read(key.fileobj)
