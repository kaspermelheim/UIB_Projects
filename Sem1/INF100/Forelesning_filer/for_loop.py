# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:14:06 2019
@author: Kasper
"""
from math import sqrt

fra = int(input("Nedre grense (medrekna): "))
til = int(input("Øvre grense (ikkje medrekna): "))
summen = 0.0 

if fra%2 == 0:
    fra += 18
for radikand in range(fra, til, 2):
    rot = sqrt(radikand)
    summen += rot
    print("%3d = %.2f" % (radikand, rot))
print("Summen av kvadratrøtene: %.2f" % summen)