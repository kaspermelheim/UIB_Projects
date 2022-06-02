#4
#README:
"""
Meet in the middle attack
Author: Kasper Melheim

Explanation on how I solved this task:

On this task I constructed a meet in the middle attack to find 3 keypairs that encrypts to the correct cipher, 
all within 2 minutes.
Everything outside the main function is unchanged code from enc.py, it is inside the main function the search happens.

Workflow:

1. build keylist of size 2**16 that holds every possible key
2. build cipher and input lists from string (encryption() and decryption() takes two lists as parameters)
3. 
build one dictionary that holds every possible cipher retrieved from encrypting the input with the keys from keylist (k1_dict)
build one dictionary that holds every possible plaintext/cipher retrieved from decrypting the given cipher with the keys from
keylist (k2_dict)
4. Swap keys and values in k2_dict, loop over every value from k1_dict, if there is a value that now is a key in k2_dict,
we print k2_dict[k1_value]

So basically I perform a meet in the middle attack where i calculate every x output from encrypting with key, and every x output
from decrypting with key, and then I compare this middle value x in each dictionary - if we have a match we have found our key pair

This results in 3 key pairs that after two rounds of encryption retrieves the given cipher:
K = (K1, K2) = (0000000000000111, 1111100011011000)
K = (K1, K2) = (0100011110010111, 0011110000101111)
K = (K1, K2) = (1011111010001010, 1111000010101110)
"""

import time

start_time = time.time()

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

def round_function(x,k):
    return multiplication(x,k,[0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1])

def round(INPUT,K):
    L = INPUT[:16]
    R = INPUT[16:]
    NEWL = [] + R
    NEWR = [] + xor(L, round_function(R,K))
    return NEWL + NEWR

def encrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        INPUT_BLOCK = round(INPUT_BLOCK,KEY)
        KEY = KEY[-2:] + KEY[:-2]
    return INPUT_BLOCK[16:] + INPUT_BLOCK[:16]

def decrypt(INPUT_BLOCK, KEY):
    for i in range(8):
        KEY = KEY[2:] + KEY[:2]
        INPUT_BLOCK = round(INPUT_BLOCK,KEY)
    return INPUT_BLOCK[16:] + INPUT_BLOCK[:16]

def main():
            #Input before encryption
            INPUT = "10101010101010101010101010101010"

            #Cipher after two rounds of encryption
            CIPHER = "11000110100010110110000001101110"

            print("Searching for keys...")

            #----------------------Build keylist------------------
            size = 2**16
            keys = []
            for i in range(size):
                i = str(bin(i))[2::]
                while len(i) < 16:
                    i = "0" + i
                keys.append(i)

            print("1. Keylist successfully built in %s seconds" % (time.time() - start_time))
            #----------------------------------------------------------
            
            #Initiate input and key block
            INPUT_BLOCK = []
            CIPHER_BLOCK = []

            #Build plaintext and cipher list
            for i in range(len(INPUT)):
                if INPUT[i] == '0':
                    INPUT_BLOCK.append(0)
                else:
                    INPUT_BLOCK.append(1)

                if(CIPHER[i] == '0'):
                    CIPHER_BLOCK.append(0)
                else:
                    CIPHER_BLOCK.append(1)

            print("2. Cipher and input successfully built in %s seconds" % (time.time() - start_time))
            

            #Initiate encrypt and decrypt dict
            k1_dict = {}
            k2_dict = {}

            #Loop over all the keys and build encrypt and decrypt dict
            for key in keys:
                #Intiate key block
                KEY_BLOCK = []
                for i in range(len(key)):
                    if key[i] == '0':
                        KEY_BLOCK.append(0)
                    else:
                        KEY_BLOCK.append(1)
                
                #Perform encryption
                E = encrypt(INPUT_BLOCK, KEY_BLOCK)
                Estr = ""
                for i in range(len(E)):
                    if E[i] == 0:
                        Estr += '0'
                    else:
                        Estr += '1'

                #Perform decryption
                E2 = decrypt(CIPHER_BLOCK, KEY_BLOCK)
                Estr2 = ""
                for i in range(len(E2)):
                    if E2[i] == 0:
                        Estr2 += '0'
                    else:
                        Estr2 += '1'

                #Build encrypt(input, k1) dict
                k1_dict[key] = Estr
                #Build decrypt (cipher, k2) dict
                k2_dict[key] = Estr2
            
            print("3. k1_dict and k2_dict successfully built in %s seconds" % (time.time() - start_time))

            #Swap keys and values in k2_dict
            k2_dict_swapped = {value:key for key, value in k2_dict.items()}
            #Check if there is a middle value v1 that is in both dictionaries (if yes we have found our keys)
            for k1,v1 in k1_dict.items():
                if v1 in k2_dict_swapped:
                    print(k1)
                    print(k2_dict_swapped[v1])  
                    print("Keys found in %s seconds" % (time.time() - start_time))              
main()