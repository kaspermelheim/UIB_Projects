#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer ulike operasjonar på lister
@author: nmidd
"""
from random import randint
   
def lagListe(liste): 
    for i in range(0,10):
        liste.append([])
        for j in range(0,10):
            liste[i].append("⬜")
        x = randint(0,9)
        liste[i][x] = "⬛"
        #print("  ".join(liste[i]))
    return liste

def sjekkSmitte(liste):
    for i in range(0,10):
        print("  ".join(liste[i]))
        for j in range(0,10):
            if liste[i][j] == "⬛" and (j-1 > -2 and j+1 < 10):
                liste[i][j+1] = "⬛"
                liste[i][j-1] = "⬛"
    print()
    
    for n in range(0,10):
        print("  ".join(liste[n]))
    
def main():
    baseliste = []
    lagListe(baseliste)
    sjekkSmitte(baseliste)
    
main()