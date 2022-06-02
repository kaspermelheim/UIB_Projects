#Problem 2

#gold.py code:

import itertools
import os
import binascii
import hashlib

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
    #Split into blocks of 256, add padding to last block
    bin_array = []
    i = 0
    while i < len(bin_str):
        if(i + 256 > len(bin_str)):
            rest = len(bin_str) - i
            offset = 256 - rest
            bin_array.append(bin_str[i:]+offset*"0")
            break
        bin_array.append(bin_str[i:i+256])
        i += 256
    return bin_array

#Convert from string to list of ints
def strToList(bin_array):
    return [int(x) for x in bin_array]

#Convert from list of ints to string
def listToStr(a):
    a = map(str, a)    
    return "".join(a)

##################################################################

#Sha hash function
def sha(block):
    data = binascii.a2b_hex("{0:0>4X}".format(int(block,2))) #use binascii on hex version of block
    result = hashlib.sha256(data).digest()
    result_final = ''.join(format(i, '08b') for i in result)
    return result_final

#Matyas Meyer-Oseas 
def encryptSHA256(filename, K, IV):
    #Read file as binary 0 and 1
    bin_str = readAsBinary(filename)
    #Split into blocks of 32, add padding to last block
    bin_array = pad(bin_str)
    #Build our result on this string
    cipher = ""
    #Initial M0 value
    M0 = IV
    
    #Iterate over every block of 256 8====D´´´´ length
    for block in bin_array:
        #Compute K||M_i-1
        conc = K + M0

        #Convert from str to list
        block_ls = strToList(block)

        #Encrypt block M_i using h(K||M_i-1)
        M_i = xor(block_ls, strToList(sha(listToStr(conc))))

        #Choose new M0
        M0 = block_ls

        #Add result to our cipher
        cipher += listToStr(M_i)

    #Return cipher
    return cipher

#IV
IV = 256*[1]
#Key
K = 128*[0,1]

#Answer
sha = encryptSHA256("gold_plaintext.in", K, IV)
print(strToList(sha))