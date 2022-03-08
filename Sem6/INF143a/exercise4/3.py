#g(x) = x^4 + x^3 + x^2 + x + 1
#Show that the polynomial is irreducible but not primtive

def isReducible(num):
    print((num**4 + num**3 + num**2 + num + 1) == 0)

for i in range(2):
    isReducible(i)

#The polynomial is irreducible in the F2 field.
#Since it is irreducible in the F2 field it is primtive.