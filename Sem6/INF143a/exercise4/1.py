#1 
#finite field F28 with p(x) = x^8 + x^4 + x^3 + x + 1 used in the AES cipher
def add(num1, num2, modulo):
    result = (num1 + num2) % modulo
    return result

def mult(num1, num2, modulo):
    result = (num1 * num2) % modulo
    return result

def raiseNum(num1, power):
    return num1 ** power

print(add(7, 5, 11))
print(mult(7, 5, 11))
print(raiseNum(2, 2))