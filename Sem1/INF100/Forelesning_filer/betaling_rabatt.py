# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:17:41 2019

@author: Kasper
"""
pris = float(input("Ordinær pris: "))
rabpris = float(input("Rabattert pris: "))
grense = float(input("Rabattgrense: "))
kvantum = float(input("Kvantum: "))

if kvantum <= grense:
    betaling = kvantum * pris
else:
    betaling = grense * pris + (kvantum - grense)*rabpris
print("Til betaling: %.2f" % betaling )


    


    