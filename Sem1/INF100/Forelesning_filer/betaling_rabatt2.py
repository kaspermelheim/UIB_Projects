# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:14:06 2019
Skriv ut om eit innlest namn er langt,
passeleg langt eller kort.
@author: Kasper
"""

pris = float(input("Ordinær pris: "))
rabpris = float(input("Rabattert pris: "))
grense = float(input("Rabattgrense: "))
kvantum = float(input("Kvantum: "))
kundenr = int(input("Kundenr.: "))

betaling = kvantum * pris
if kundenr < 100:
    if kvantum > grense/2:
        betaling = grense/2 * pris + (kvantum-grense/2)*rabpris
elif kvantum > grense: 
    betaling = grense*pris + (kvantum-grense)*rabpris
print("Til betaling: %.2f NOK" % betaling)
