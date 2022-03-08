#1
#Google LFSR

#2
# si+4 = si+3 ⊕ si+1 ⊕ si
# Polynomal expression: x^4 + x^3 + x + 1

#3
# Running LFSR states:
# We need to take number in pos4 XOR pos3 XOR pos1
# 0000 (loop)

# 0001 
# 1 XOR 0 XOR 0 = 1, push 1 at the end out:
# 1000
# 1100
# 1110
# 0111
# 0011

# 0010
# 1001
# 0100

# 0101
# 1010

# 0110
# 1011
# 1101

# 1111 (loop)

#4
# Generate 10 bits of out from 1001
#1001 -> 0100 -> 0010
# Gives output stream: 1001001001