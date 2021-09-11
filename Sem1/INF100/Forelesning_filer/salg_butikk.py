# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:52:38 2019

@author: Kasper
"""

vare1 = "Bøker"
vare2 = "Minnepinner"

antalStr = input("Totalt antal " + vare1 + ": ")
antal1 = int(antalStr)
beløpStr = input("Totalbeløp for " + vare1 + ": ")
beløp1 = float(beløpStr)
antallStr = input("Totalt antal " + vare2 + ": ")
antal2 = int(antalStr)
beløpStr = input("Totalbeløp for " + vare2 + ": ")
beløp2 = float(beløpStr)

snitt1 = beløp1/antal1
snitt2 = beløp2/antal2
print()
print("Vare         Antall   Snitt")
print("%-13s %5d %7.2f " % (vare1, antal1, snitt1))
print("%-13s %5d %7.2f" % (vare2, antal2, snitt2))