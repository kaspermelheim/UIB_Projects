#1

#To represent each element me need 2^(n-1) = MAX
#Solving for n, and MAX = 32768
#n-1 * log2 = log 32768
#n = 16, which means 15 bits is needed to represent each number (2^15 = 32768 = MAX)

#2

s0 = 1001
A = 1103515245
B = 12345
MAX = 32768
keystream = ""

for i in range(8):
    formula = (A * s0 + B) % MAX
    print(f"{s0} / {format(s0, '015b')}")
    keystream = keystream + format(s0, '015b')
    s0 = formula

print("Keystream of length 120:")
print(keystream)


#3
plaintext = "HELLO"
liste = []
ptext = ""
print(ord("H"))
for i in plaintext:
    liste.append(format(ord(i), '08b'))
    ptext += format(ord(i), "08b")
print("HELLO:")
print(liste)
print(ptext)

#4
encrypted = ""

for i in range (len(ptext)):
    xor = int(ptext[i]) ^ int(keystream[i])
    encrypted += str(xor)
print(encrypted)

#5
#Using ASCII table
#11111000 = "ø"
#10011000 = ""
#00100000 = " "
#01110011 = "s"
#10000001 = ""



