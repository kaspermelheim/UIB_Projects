#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Handterer artsobservasjonar lagra på fil
@author: nmidd
"""

from os import chdir

def summer(streng):
    """
    Returnerer summen av alle tal i strengen streng
    """
    liste = streng.split()
    summen = 0
    for ordet in liste:
        if ordet.isdigit():
            summen += int(ordet)
    return summen

def lag_totaloversikt(observasjonar, analyse, filnamn):
    """
    Les artsobservasjonar frå fila med namn filnamn i katalogen observasjonar.
    Skriv talet på observasjonar av kvar art på fila filnamn i katalogen analyse.
    """
    chdir(observasjonar)
    lesefil = open(filnamn)
    liste = lesefil.readlines()
    lesefil.close()
    chdir(analyse)
    with open(filnamn, "w") as skrivefil:
        for streng in liste:
            total = summer(streng)
            art = streng.split()[0]
            skrivefil.write(art + " " + str(total) + "\n")

def main():
    """lag_totaloversikt('/Users/nmidd/Observasjonar',
                      '/Users/nmidd/Analyse/',
                      'fugl.txt') """
    lag_totaloversikt("\Users\Kasper\OneDrive - University of Bergen\Documents\INF100\Forelesning_filer\Observasjonar","\Users\Kasper\OneDrive - University of Bergen\Documents\INF100\Forelesning_filer\Analyse","fugl.txt")
    
main()
