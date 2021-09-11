import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
text = "test text"

s.sendto(text.encode("utf-8"), ("localhost", 1234))