#3
#Suppose the RSA encryption scheme is used with the public
#key (n, e) = (15151, 17), and suppose that you have intercepted the ciphertext y = 832

#Find the prime factorization of n, i.e. find the primes p, q such that n = pq

#Answer:

n = 15151
e = 17
cipher = 832


#Find the two primes by prime factorization of n
#Standard prime factorization function
def primeFactorization(n):
    result = []

    for x in range(2,n + 1):
        if n % x == 0:
            total = 1
            for y in range(2, (x // 2 + 1)):
                if(x % y == 0):
                    total = 0
                    break
            if(total == 1):
                #We have found our prime
                result.append(x)
    return result
print(primeFactorization(n))

#Using this code we find that p = 109 and q = 139
# p = pq = 109 * 139 = 15151
p = 109
q = 139

#Compute ϕ(n)

#Answer:
#Formula ϕ(n) = (p - 1)(q - 1)
#             = (109 - 1) * (139 - 1)
#             = 14904
ϕ_n = 14904

#Using the above, find the private key d

#Answer:
#To calculate the private key d we need to find modular inverse d, this formula:
#d = e^-1 mod ϕ(n)
#Using a online calculator we find that d = 6137

#Implementation:
def modularInverse(e, ϕ_n):
    for num in range(1, ϕ_n):
        if (e % ϕ_n) * (num % ϕ_n) % ϕ_n == 1:
            return num
print(modularInverse(e, ϕ_n))

#This code also shows that d = 6137
d = 6137

#Using the private key, decrypt the ciphertext y

#Answer:
#To decrypt the ciphertest we need to apply the formula:
#Plaintext ≡ cipher^d (mod n)
#          ≡ 832^6137 (mod 15151)
def decrypt(cipher, d, n):
    return (cipher**d) % n
print(decrypt(cipher, d, n))

#We then find that plaintext = 1781
plaintext = 1781