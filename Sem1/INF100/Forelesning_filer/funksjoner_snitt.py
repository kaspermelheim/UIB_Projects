# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

def les_antal(vare):
    antal = int(input("Totalt antal " + vare + ": "))
    return antal

def les_belop(vare):
    belop = float(input("Totalbeløp for " + vare + ": "))
    return belop

def skriv_snitt(vare, antal, belop):
    snitt = belop/antal
    print("%-13s %5d %7.2f" % (vare, antal, snitt))

vare1 = input("Første vare: ")
vare2 = input("Andre vare: ")
antal1 = les_antal(vare1)
belop1 = les_belop(vare1)
antal2 = les_antal(vare2)
belop2 = les_antal(vare2)

print("%-13s %5s %7s" % ("Vare", "Antal", "Snitt"))

skriv_snitt(vare1, antal1, belop1)
skriv_snitt(vare2, antal2, belop2)


  
    