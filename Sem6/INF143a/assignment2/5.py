#5
from itertools import product

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

"""
This solution works for testdata:
Primitive polynom: x^3 + x + 1 = [1,1,0,1] with n = 3 gives:
[0, 5, 6, 7, 4, 3, 1, 2]
"""


"""
Actual data:
"""
#Primitive polynom:
#p(x) = x32 + x15 + x9 + x7 + x4 + x3 + 1

irr_original = [1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Reversed irr_poly
irr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1]

n1 = 4
n2 = 5
n3 = 6

#Gold function 
def goldFunc(n):

    nums = [0,1]
    combs = list(product(nums, repeat=n))

    res = []

    for c in combs:
        i = list(c)
        res.append(multiplication(multiplication(i,i,irr), i, irr))
    return res

#List for n1, n2 and n3
list_n1 = goldFunc(n1)
list_n2 = goldFunc(n2)
list_n3 = goldFunc(n3)

#Convert from list of ints to list of strings
def convert(list_raw, n):
    list_new = []
    for i in list_raw:
        el = "".join([str(x) for x in i])

        #Convert to int
        list_new.append(int(el,2))

    return list_new

#Result for n = 4, n = 5 and n = 6:

#[0, 0, 0, 0, 1, 1, 1, 1, 8, 9, 10, 11, 15, 14, 13, 12]
#[0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 16, 17, 18, 19, 21, 20, 23, 22, 30, 31, 28, 29, 26, 27, 24, 25]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 5, 5, 5, 5, 7, 7, 7, 7, 6, 6, 6, 6, 32, 33, 34, 35, 36, 37, 38, 39, 42, 43, 40, 41, 46, 47, 44, 45, 60, 61, 62, 63, 57, 56, 59, 58, 53, 52, 55, 54, 48, 49, 50, 51]

print(convert(list_n1, n1))
print(convert(list_n2, n2))
print(convert(list_n3, n3))


