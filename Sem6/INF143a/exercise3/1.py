#1

#For the functions to be linear we need f(x + y) = f(x) + f(y)

#(x, y) = (000000, 000001)
#00 maps to row 0, 0000 maps to col 0 = 14
#01 maps to row 1, 0000 maps to col 0 = 0
#x XOR y = 000001 = 0 from the table
#Since 14 + 0 != 0, we have a non-linear function

#(x, y) = (111111, 100000)
#11 maps to row 3, 1111 maps to col 15 = 13
#10 maps to row 2, 0000 maps to col 0 = 4

#(x, y) = (101010, 010101)
#10 maps to row 2, 0101 maps to col 5 = 6
#01 maps to row 1, 1010 maps to col 10 = 12

def xor(plaintext, cipher):
    s = ""
    for i in range(len(plaintext)):
        calc = int(plaintext[i]) ^ int(cipher[i])
        s += str(calc)
    return s
print(xor("000000", "000001"))

#2
#Input 6 bits, use table 1 to find number then convert to 4 bits
sbox =  [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]]

in1 = "000000"
in2 = "000001"

def s1(input1):
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

    print("x: " + str(x))
    print("y: " + str(y))
    print("sbox[x][y]: " + str(sbox[x][y]))
    
    #return(format(sbox[x][y], "04b"))
    return sbox[x][y]

print(s1(in1))
print(s1(in2))

#3

def isLinear(in1, in2):
    return s1(in1) + s1(in2) == s1(xor(in1, in2))

print(isLinear(in1, in2))

def countLinear():
    linear_count = 0
    nonlinear_count = 0
    val1 = "000000"
    val2 = "000001"
    
    if (isLinear(val1, val2)):
        linear_count += 1
    else:
        nonlinear_count += 1

    return linear_count, nonlinear_count

print(countLinear())