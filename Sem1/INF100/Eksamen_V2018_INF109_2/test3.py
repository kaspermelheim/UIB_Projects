#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer ulike operasjonar på lister
@author: nmidd
"""
spillere = ["Carlsen", "Caruana", "Ding", "Giri"]
parti = [[None, "s", "r", "r"], ["r", None, "h", "r"],["r", "h", None, "r"], ["r", "s", "r", None]]
vurderinger = []
oversikt = {}

def les(filnamn):
    with open(filnamn, "r") as lesefil:
        filliste = lesefil.readlines()
    for linje in filliste:
        nylinje = linje.split(":")
        nytuppel = (nylinje[0], nylinje[1], int(nylinje[2]))
        vurderinger.append(nytuppel)
        nyoversikt = oversikt[nylinje[0]]
        nyoversikt[int(nylinje[2])-1] += 1
    return vurderinger, oversikt

print(les("text.txt"))


















#print(isGeometric([4,8,16,32]))
#print(isGeometric([2,4,6,8]))
#print(fillesing("navn.txt", "brukernamn.txt"))
#reg()