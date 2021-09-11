# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:14:06 2019
@author: Kasper
"""
from matplotlib import pyplot

n = int(input("Antal observerte artar: "))
for i in range(n):
    art = input("Observert art: ")
    observasjonar = int(input("Antal observasjonar av " + art + ": "))
    farge = "Orange"
    if art.startswith("Blå"):
        farge = "blue"
    elif art.startswith("Grå"):
        farge = "grey"
    elif art.startswith("Svart"):
        farge = "black"
    elif art.startswith("Rød"):
        farge = "red"
    elif art.startswith("Grøn"):
        farge = "green"
    elif art.startswith("Lilla"):
        farge = "purple"
    elif art.startswith("Gul"):
        farge = "yellow"
    pyplot.bar(art, observasjonar, color=farge)
pyplot.show()