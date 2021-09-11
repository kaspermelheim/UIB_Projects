#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eksempel på operasjonar på ei liste med innleste tal
@author: nmidd
"""

resultat = ["Haugesund", "Molde", "Vålerenga", "Sogndal"]
for n in range(0,5):
    lag = str(input("Skriv inn namnet på laget: "))
    tall = int(input("Kvar ligg laget på tabellen: "))
    del resultat[tall-1]
    resultat.insert(tall-1, lag)
    print(resultat)