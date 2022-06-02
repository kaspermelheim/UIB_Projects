"""
DES Feistel Implementation
Created by: Kasper Melheim
"""

from collections import deque
from unittest import result

#Step 1

print("Step 1, obtain keys: ")
print()

def convert(s):
    new = ""
  
    for x in s:
        new += x 
   
    return new

#Key for encryption
Key = "0001001100110100010101110111100110011011101111001101111111110001"
testKey = 64*"0"
PKey = ""

#PC1 table for permutation
pc1 = [[57, 49, 41, 33, 25, 17, 9],
       [1, 58, 50, 42, 34, 26, 18],
       [10, 2, 59, 51, 43, 35, 27],
       [19, 11, 3, 60, 52, 44, 36],
       [63, 55, 47, 39, 31, 23, 15],
       [7, 62, 54, 46, 38, 30, 22],
       [14, 6, 61, 53, 45, 37, 29],
       [21, 13, 5, 28, 20, 12, 4]]

#Loop through PC1 table and create PKey
for i in range (len(pc1)):
    for n in range (len(pc1[i])):
        PKey += Key[(pc1[i][n])-1]

#Lists for keeping track of all the keys we need 
keyListCi = []
keyListDi = []

#Split PKey in two halves C0 and D0
C0 = PKey[0:28]
D0 = PKey[28:]

#Add halves in our keyList
keyListCi.append(C0)
keyListDi.append(D0)

#List to keep track of number of leftshifts we will perform when creating our keys
leftshifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

#Create our keys
for i in range(16):
    Ci = deque(keyListCi[i])
    Di = deque(keyListDi[i])
    for i in range (int(leftshifts[i])):
        Ci.rotate(-1)
        Di.rotate(-1)
    keyListCi.append(convert(Ci))
    keyListDi.append(convert(Di))
    
print(keyListCi)
print(keyListDi)

#PC2 table for permutation
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

keyList = []

#Permutation function
def generatePermutation(testKey, table):
    k = ""
    for i in range(0,len(table)):
        k += testKey[table[i]-1]
    return k

#Generate all the permuted keys
for i in range(1,len(keyListCi)):
    keyList.append(generatePermutation((keyListCi[i] + keyListDi[i]), PC2))
print("KeyList:")
print(keyList)

#Step 2
print()
print("Step 2:")
print()

#Plaintext for encryption
M = "0000000100100011010001010110011110001001101010111100110111101111"
testM = 64*"0"
testM2 = 56*"0"+"10000000"

#Table for initial permutation
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

#Permutation from table IP
permutedIP = generatePermutation(M, IP)
print("Permuted key: " + permutedIP)

#Split key in halves L0 and R0
L0 = permutedIP[0:32]
R0 = permutedIP[32:]
print("L0: " + L0)
print("R0: " + R0)

#E_Bit table
E_Bit = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]

E_R0 = ""

#Find E_R0
for i in range(len(E_Bit)):
    E_R0 += R0[(E_Bit[i])-1]

#Find E_R0 xor keyList
xorM = ""
for i in range(len(E_R0)):
    xorM += str( int(E_R0[i]) ^ int(keyList[0][i]) )

print(xorM)

#SBoxes

sbox1 =  [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

sbox2 =  [[ 15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

sbox3 =  [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]]

sbox4 =  [[ 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]]

sbox5 =  [[ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]]

sbox6 =  [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]]

sbox7 =  [[ 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]]

sbox8 =  [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 ]]

#Find correct 4 bits using the SBoxes
def sboxFunc(input1, sbox):
    x = 0
    if(input1[0] + input1[-1] == "10"):
        x = 2
    elif(input1[0] + input1[-1] == "00"):
        x = 0
    elif(input1[0] + input1[-1] == "01"):
        x = 1
    elif(input1[0] + input1[-1] == "11"):
        x = 3

    y = int(input1[1:5], 2)

    #print("sbox[x][y]: " + str(sbox[x][y]))
    
    return(format(sbox[x][y], "04b"))

#Concat output from every SBox into one string
sBoxOutput = sboxFunc(xorM[0:6], sbox1) + sboxFunc(xorM[6:12], sbox2) + sboxFunc(xorM[12:18], sbox3) + sboxFunc(xorM[18:24], sbox4) + sboxFunc(xorM[24:30], sbox5) + sboxFunc(xorM[30:36], sbox6) + sboxFunc(xorM[36:42], sbox7) + sboxFunc(xorM[42:48], sbox8)
print(sBoxOutput)

#P table
P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

#Find f
f = generatePermutation(sBoxOutput, P)
print("f:")
print(f)
print("L0:")
print(L0)

#XOR function
def xor(plaintext, cipher):
    s = ""
    for i in range(len(plaintext)):
        calc = int(plaintext[i]) ^ int(cipher[i])
        s += str(calc)
    return s

#Result after L0 xor f
Result = xor(L0, f)
print(Result)

#Final result after adding R0
print(R0 + Result)

#The answer is: 0000000000000000000000000000000011011000110110001101101110111100

IP_1 =[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]