"""
Task 4.1: Exhaustive search
Author: Kasper Melheim

In this task I construct every single key possible (2**16 keys) and attempt enceyption for every single one.
After a couple seconds of running the code we find:

Key = 1011101001101111

this succesfully encrypts to the given cipher: 11110100011101010101100111111110
"""

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
    return multiplication(x,k,[0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1]);

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
        #Plaintext
        INPUT = "10101010101010101010101010101010"

        #----------------------EXHAUSTIVE SEARCH FOR KEY THAT GIVES encrypt(plaintext, key) == cipher---------------------
        #Generate keys
        keys = []
        for i in range(2**16):
            i = str(bin(i))[2::]
            while len(i) < 16:
                i = "0" + i
            keys.append(i)
        #-------------------------------------------------------------------------------------

        #Test encryption with every single key
        for i in range(len(keys)):
            KEY = keys[i]

            INPUT_BLOCK = []
            KEY_BLOCK = []

            for i in range(len(INPUT)):
                if INPUT[i] == '0':
                    INPUT_BLOCK.append(0)
                else:
                    INPUT_BLOCK.append(1)
            for i in range(len(KEY)):
                if KEY[i] == '0':
                    KEY_BLOCK.append(0)
                else:
                    KEY_BLOCK.append(1)

            E = encrypt(INPUT_BLOCK,KEY_BLOCK)
            Estr = ""
            for i in range(len(E)):
                if E[i] == 0:
                    Estr += '0'
                else:
                    Estr += '1'
            if(Estr == "11110100011101010101100111111110"):
                print("Key that encrypts to correct cipher 11110100011101010101100111111110: ")
                print(KEY)   
main()
