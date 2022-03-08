"""
Task 1
Author: Kasper Melheim
"""
# What is the maximum possible cycle length 
# (that is, the number of outputs that it can produce before it loops) 
# of an LFSR on 100 bits?
#Construct such an LFSR (you can give your answer either as a diagram or a polynomial).

"""Answer:"""

#If a polynom is primitive, it's maxiumum length cycle can be found using 2^(m) − 1 = 2^(100) - 1 = 1.2676506x^(30)

#A degree m LFSR can be represented using a polynomial p(x) on the form p(x) = x^m + am−1 * x^(m−1) + am−2 * x^(m−2) + · · · + a1*x + a0
# p(x) = x^100 + a99 * x^99 + a98 * x^(98) + . . . + a1*x + a0