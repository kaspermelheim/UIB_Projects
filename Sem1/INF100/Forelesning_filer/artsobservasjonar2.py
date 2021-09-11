#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les observasjonar avslutta med <enter>,
skriv gjennomsnittet
@author: nmidd
"""

from matplotlib import pyplot

summen = 0
artar = 0
fleire = True
while fleire:
    namn = input('Artsnamn (avslutt med <enter>): ')
    if len(namn) > 0:
        obs = int(input('Observasjonar av %s: ' % namn))
        summen += obs
        artar += 1
    else:
        fleire = False
if artar > 0:
    snitt = summen/artar
    print('Gjennomsnittleg observasjonar av %d artar: %.1f'
          % (artar, snitt))
else:
    print('Ingen observasjonar.')    