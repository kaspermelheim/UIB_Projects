"""
Task 3
Author: Kasper Melheim

In this task I have created two functions encrypt(p, k) and decrypt(c, k) which succesfully performs 8 rounds of Feistel
encryption and decryption. The code gets the correct results for the testdata, and therefore also solves the task.
"""
#3

#Irreducible polynom:
#p(x) = x32 + x15 + x9 + x7 + x4 + x3 + 1

#Key
K = "3ACDDEF2"
k = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1]

#Plaintext
P = "1F2A0E341F2A0E34"
p = [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0]

#Cipher
C = "AAAAAAAAAAAAAAAA"
c = [0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1]

irr_poly = [1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Reversed irr1
irr_poly_rev = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1]

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

def shift(l, n):
    return l[n:] + l[:n]

#Perform 8 rounds of Feistel encryption
def encrypt(p,k):

    #8 rounds
    for i in range(8):
        #Get left and right half of plaintext
        L0 = p[:32]
        R0 = p[32:]

        #Save right half in x
        x = R0

        #Perform multiple multiplications and xors
        mult1 = multiplication(multiplication(x,x,irr_poly_rev), k, irr_poly_rev)
        mult2 = multiplication(x, multiplication(k,k,irr_poly_rev), irr_poly_rev)
        mult3 = xor(mult1, mult2)
        mult4 = xor(mult3, L0)

        #New plaintext
        p = R0 + mult4

        #Shift key 4 pos to the left
        k = shift(k, -4)

    return p

#Key we will use for decryption
k_end = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]

#Perform 8 rounds of Feistel decryption
def decrypt(c, k):

    #Swap positions before for loop starts since we are decrypting
    c = c[32:] + c[:32]
    
    #8 rounds
    for i in range(8):
        #Get left and right half of cipher
        L0 = c[:32]
        R0 = c[32:]

        #Save right half in x
        x = R0

        #Perform multiple multiplications and xors
        mult1 = multiplication(multiplication(x, x,irr_poly_rev),k,irr_poly_rev)
        mult2 = multiplication(x, multiplication(k,k,irr_poly_rev),irr_poly_rev)
        mult3 = xor(mult1, mult2)
        mult4 = xor(L0,mult3)

        #New cipher
        c = R0 + mult4

        #Shift key 4 pos to the right
        k = shift(k, 4)

    #Swap result after for loop since we are decrypting
    return c[32:] + c[:32] 


#Encryption works for testdata - we encrypt the plaintext with the key and obtain the given cipher
print("Correct result for encrypting: " + str(encrypt(p,k) == c))

#Decryption works for testdata - we decrypt the cipher with the key and obtain the given plaintext
print("Correct result for decrypting: " + str(decrypt(c,k_end) == p))