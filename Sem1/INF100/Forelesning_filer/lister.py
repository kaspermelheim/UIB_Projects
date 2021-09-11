# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""
n = int(input("Antal observasjonar: "))
talliste = []
for i in range(n):
    tal = float(input(
            "%3d. observasjon: " % (i+1)))
    talliste.append(tal)
summen = sum(talliste)
snitt = summen/n
print()
print("%7s %7s" % ("Verdi", "Avvik"))
for tal in talliste:
    avvik = tal - snitt
    print("%7.2f %7.2f" % (tal, avvik))
