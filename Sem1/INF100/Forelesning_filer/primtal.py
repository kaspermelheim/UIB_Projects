#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finn alle primtal mindre enn eller lik ein oppgitt skranke
@author: nmidd
"""

def primtal(n):
    """
    Returnerer mengda med primtal mindre enn eller lik n
    """
    prim = set(range(2, n+1))
    for k in range(2, n+1):
        for x in prim-{k}:
            if x % k == 0:
                prim.discard(x)
    return prim
    
def main():
    n = int(input('Største tal: '))
    prim = primtal(n)
    print(prim)

main()
