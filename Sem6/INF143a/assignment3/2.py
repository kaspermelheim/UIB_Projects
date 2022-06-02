#Problem 2

#gold.py code:

import itertools
import os

#x^32 + x^15 + x^9 + x^7 + x^4 + x^3 + 1
irr = [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def bin2int(B):
    n = 0
    for i in range(len(B)):
        if B[i] == 1:
            n += (2**(len(B)-i-1))
    return n

def xor(v1,v2):
    result = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        result.append(b)
    return result

def multiplication(A,B,irr):
    result = [ ]
    for i in range(len(A)):
        result.append(0)
    
    for i in range(len(A)):
        if B[i] == 1:
            shift = A
            for s in range(i):
                do_we_have_overflow = (shift[-1] == 1)
                shift = [0] + shift[:-1]
                if do_we_have_overflow:
                    shift = xor(shift, irr)
            result = xor(result,shift)
    return result

def gold(P):
    return multiplication( P, multiplication(P, P, irr), irr)

def encrypt(P,K):
    assert len(P) == 32
    assert len(K) == 32
    return xor(P, gold(K))


##################### HELP FUNCTIONS ############################
def readAsBinary(filename):
    #Read file as binary and get content as 0 and 1s
    with open(filename, "rb") as f:
            data = f.read(1)
            lst = []
            while data:
                lst.append(ord(data))
                data = f.read(1)
            bin_str = ''.join(format(i, '08b') for i in lst)
            f.close()
            return bin_str
    return 0

def pad(bin_str):
    #Split into blocks of 32, add padding to last block
    bin_array = []
    i = 0
    while i < len(bin_str):
        if(i + 32 > len(bin_str)):
            rest = len(bin_str) - i
            offset = 32 - rest
            bin_array.append(bin_str[i:]+offset*"0")
            break
        bin_array.append(bin_str[i:i+32])
        i += 32
    return bin_array

#Convert from string to list of list of ints
def convert(bin_array):
    bin_array_ints = []
    for block in bin_array:
        b = []
        for num in block:
            b.append(int(num))
        bin_array_ints.append(b)
    return bin_array_ints

#Convert from string to list of ints
def strToList(bin_array):
    return [int(x) for x in bin_array]

##################################################################


#Matyas Meyer-Oseas 
def encryptMMO(filename, K):
    cipher_array = []

    #Read file as binary 0 and 1
    bin_str = readAsBinary(filename)
    #Split into blocks of 32, add padding to last block
    bin_array = pad(bin_str)
    #Convert from list of strings to list of list of ints
    bin_array_ints = convert(bin_array)

    #Send each block/list to encrypt() with Matyas Meyer-Oseas 
    for block in bin_array_ints:
        cipher = encrypt(block, K)
        K = xor(cipher, block)

    #Return cipher
    return K

#First round key
h0 = [1]*32

print("Matyas Meyer-Oseas:")
mmo = encryptMMO("gold_plaintext.in", h0)
print(mmo)

#What is the output size of this hash function?
#The size of the output is 32 bit long
print(len(mmo))

#What is the complexity of the birtday-attack?
#2**32