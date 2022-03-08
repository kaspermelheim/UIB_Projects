#f1(x) = x^4+x^3+1 and f2(x) = x^4+x+1
#Check if they are irreducible

def isReducible(num):
    print((num**4 + num**3 + 1) == 0)
    print((num**4 + num + 1) == 0)

for i in range(2):
    isReducible(i)

#The polynomials are irreducible in the F2 field.
