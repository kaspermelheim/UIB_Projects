"""
Task 2
Author: Kasper Melheim
"""

from collections import deque
from itertools import repeat
#2

#K = (1, 0, 1, 0, . . . , 1, 0) 80 alternating 0s and 1s
#IV = (0, 1, . . . , 0, 1) 80 alternating 0s and 1s

#Actual data we want to test
K = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
IV = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

#Testdata - our code works for this data
K_ = [1] * 80
IV_ = [0] * 80

#Function to build K and IV as seen above
def buildKey():
    liste = []
    for i in range(80):
        if i % 2 == 1:
            liste.append(0)
        else:
            liste.append(1)
    return liste

#1152 = 4 x 288 iterations of warmup to mix IV and key

#Initialize state
#Load the key and IV into the first 80 bits of lfsr1 and lfsr2

lfsr1 = K + [0] * 4
lfsr2 = IV + [0] * 13
lfsr3 = [0] * 108 + [1,1,1]

#Result list
result = []

result_bits = 1000
test_result_bits = 50

#By following the Figure 1: Trivium cipher I ended up with a for loop performing warmup rounds + result:

#Warmup 1152 iterations + output
for i in range(1152 + result_bits): #change this to test_result_bits for testdata

    #Perform first round of XOring
    t_1 = lfsr2[65] ^ (lfsr2[90] & lfsr2[91]) ^ lfsr2[92]
    t_2 = lfsr1[68] ^ (lfsr1[81] & lfsr1[82]) ^ lfsr1[83]
    t_3 = lfsr3[65] ^ (lfsr3[108] & lfsr3[109]) ^ lfsr3[110]

    #Save the result of XORing all of the above in our result list
    result.append(t_1 ^ t_2 ^ t_3)

    #Calculate shift by XORing above calculations with the 77, 86 and 68 bit in each lfsr (python index start at 0)
    shift1 = t_1 ^ lfsr1[77] 
    shift2 = t_2 ^ lfsr3[86]
    shift3 = t_3 ^ lfsr2[68]

    #Remove used element
    lfsr1.pop()
    lfsr2.pop()
    lfsr3.pop()

    #Insert new value at the start of the lfsr
    lfsr1.insert(0, shift1)
    lfsr3.insert(0, shift2)
    lfsr2.insert(0, shift3)

#Testdata result
expected_test_result = [1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1]
#print("Our result match the expected test result: " + str(expected_test_result == result[1152:]))

"""
Answer:
"""
#Print the bits after the warmup rounds, this is the result
print(result[1152:])

    



