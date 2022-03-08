p = "1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0"
plaintext = p.replace(", ", "")
print(plaintext)

c = "0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1"
cipher = c.replace(", ", "")
print(cipher)

def xor(plaintext, cipher):
    s = ""
    for i in range(len(plaintext)):
        calc = int(plaintext[i]) ^ int(cipher[i])
        s += str(calc)
    return s

#XOR c with p and you get keystream
keystream = xor(plaintext, cipher)
print(keystream)

#Length 30, each number has 10 bits each, starting a pos 20 so we have: s2, s3 and s4
#s2 = "1100010111" = 791
#s3 = "1010110100" = 692
#s4 = "1011000101" = 709

# I: 709 = 692A + B (mod 1024)
# II: 692 = 791A + B (mod 1024)

# B = 709 - 692A (mod 1024)
# put I into II

# 692 = 791A + ((709 - 692A)mod 1024) (mod 1024)
# => 99A = (-17 mod 1024) (mod 1024)
# => 99A = 1007 (mod 1024)
#find modular inverse which is 331 and multiply 1007
# => A = (1007 * 331) mod 1024
# A = 517

# We find B using A
# B = 709 - 692*517 (mod 1024)
# B = 321

# Now we need to solve s2 = As1 + B (mod 1024) to find s0 using s1
# 517s1 = 791 - 321 (mod 1024) = 470 (mod 1024)
# inverse of 517 mod 1024 is 717
# => s1 = (470 * 717) mod 1024
# s1 = 94

# Now we need to solve s1 = As0 + B (mod 1024) to find s0
# 517s0 = 94 - 321 (mod 1024) = 797 (mod 1024)
# inverse of 517 mod 1024 is 717
# => s0 = (797 * 717) mod 1024
# s0 = 57

# We end up with the secret key (A, B, s0) = (517, 321, 57)


