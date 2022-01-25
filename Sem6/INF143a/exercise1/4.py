#Finne key når vi vet cipher og plaintext
encrypted = "AAAAA AAAAA"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decrypted1 = "HELLO THERE"
decrypted1_alphabet_index = [7, 4, 11, 11, 14, 19, 7, 4, 17, 4]

decrypted2 = "HELLO WORLD"
decrypted2_alphabet_index = [7, 4, 11, 11, 14, 22, 14, 17, 11, 3]

decrypted3 = "WHITE CHALK"
decrypted3_alphabet_index = [22, 7, 8, 19, 4, 2, 7, 0, 11, 10]

#Finne alfabet index til key
nyliste = []
for tall in decrypted3_alphabet_index:
    nyliste.append((0 - tall)+26)
print(nyliste)

#Print alphabet med indeks
for i,j in enumerate(alphabet):
    print(str(i) + " -> "+ j)

#Alfabet indeks til bokstaver i key
key1_index = [19, 22, 15, 15, 12, 7, 19, 22, 9, 22]
key2_index = [19, 22, 15, 15, 12, 4, 12, 9, 15, 23]
key3_index = [4, 19, 18, 7, 22, 24, 19, 26, 15, 16]

#Bruker dette til å finne key
key1 = "TWPPMHTWJW"
key2 = "TWPPMEMJPX" 
key3 = "ETSHWYTAPQ"

