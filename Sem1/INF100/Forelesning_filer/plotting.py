#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plottar tilfeldige data
@author: nmidd
"""

from matplotlib import pyplot
from random import random

def lag_tilfeldig_liste(n):
    """
    Lagar og returnerer tilfeldig liste med lengd n
    """
    tilfeldig = [None]*n
    for i in range(n):
        tilfeldig[i] = random()
    return tilfeldig

def akkumuler(liste):
    """
    Erstattar alle liste[i] med liste[0]+...+liste[i]
    """
    summen = 0.0
    for i in range(len(liste)):
        summen += liste[i]
        liste[i] = summen
        
def lag_akkumulert(liste):
    """
    Lagar og returnerer liste med akkumulerte verdiar i liste
    """
    kopi = list(liste)
    akkumuler(kopi)
    return kopi

def lag_glatta(liste, vekt):
    """
    Lagar og returnerer liste med glatta verdiar i liste,
    der vekta på kvart naboelement er lik vekt
    """
    glatta_liste = list(liste)
    n = len(liste)
    if n > 1:
        verdi = (1-vekt)*liste[0] + vekt*liste[1]
        glatta_liste[0] = verdi
        for i in range(1, n-1):
            verdi = vekt*liste[i-1] + (1-2*vekt)*liste[i] + vekt*liste[i+1]
            glatta_liste[i] = verdi
        verdi = vekt * liste[n-2] + (1-vekt)*liste[n-1]
        glatta_liste[n-1] = verdi
    return glatta_liste
def main():
    observasjonar = lag_tilfeldig_liste(10)
    pyplot.plot(observasjonar, 'y')
    akkumulert = lag_akkumulert(observasjonar)
    pyplot.plot(akkumulert, 'b')
    glatta_observasjonar = lag_glatta(observasjonar, 0.2)
    pyplot.plot(glatta_observasjonar, 'r')
    pyplot.show()
    
main()
