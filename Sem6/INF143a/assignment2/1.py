import math
#1
#Find the last two digits of the number 987654321^12345678987654321

#Answer:
#num = 987654321**12345678987654321
a = 987654321
b = 12345678987654321

#I find that:
#987654321 mod 10 = 1
#987654321 mod 100 = 21
#987654321 mod 1000 = 321
#987654321 mod 10000 = 4321

#We see a clear pattern here using modulo

#So finding the last two digits of 987654321^12345678987654321 we can use pretty simple form of modular arithmetic:
#987654321^12345678987654321 mod 100 = last two digits
#Since this is a very large number, just doing 987654321**12345678987654321 % 100 in Python wont give us a answer (at least not for a very long time)

#I wrote this code that does it much faster (the built in pow() calculates modulo in a much faster way)
def two_last_digits(base, power):
    result = pow(base, power, 100)
    return result

#Real data:
#Testing it with our numbers a and b we find that the two last digits are 21
print(two_last_digits(a, b)) #output 21

