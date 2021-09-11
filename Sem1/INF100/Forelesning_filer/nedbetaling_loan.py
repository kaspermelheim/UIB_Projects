# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

beløp = float(input("Lånebeløp i NOK: "))
startår = int(input("Startår: "))
rente = float(input("Årleg rente i %: "))
betaling = float(input("Årleg betaling av avdrag og renter i NOK: "))

if betaling > beløp * rente / 100.0:
    balanse = beløp
    år = startår
    while balanse > 0.0:
        print("%4d: %10.2f" % (år, balanse))
        balanse += balanse*rente/100.0
        balanse -= betaling
        år += 1
else:
    print("For liten innbetaling.")