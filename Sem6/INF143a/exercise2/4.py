#Check if polynomials are primitive

#1
#f(x) = X^5 + x + 1
#10010
#11001
#11100
#01110
#10111
#01011
#00101
#next one is 10010, we have looped and no maximum length cycle = not primitive polynomial

#2
#g(x) = x^4 + 1
#0001
#1000
#0100
#0010
#next one is 0001, we have looped and no maximum length cycle = not primitive polynomial

#3
#h(x) = X^4 + x + 1
#0001
#1000
#1100
#1110
#1111
#0111
#1011
#0101
#1010
#1101
#0110
#0011
#1001
#0100
#0010
#next one is 0001, we have looped through all possible non-zero states (15 states), this is a maximum length cycle = primitive polynomial

