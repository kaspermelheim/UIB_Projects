#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program som tel ulike ord på tekstfiler.
@author: nmidd
"""

def stripp(ordliste):
    """
    Fjernar eit utval teikn frå alle ord i ei liste
    """
    rusk = ',.;:!?"\'|()[]{}\t\n '
    for i in range(len(ordliste)):
        ordliste[i] = ordliste[i].strip(rusk)

def les_ordliste(filnamn):
    """
    Returnerer ei liste over orda på fila med namn filnamn
    """
    with open(filnamn, "r") as lesefil:
        tekst = lesefil.read()
    ordliste = tekst.split()
    stripp(ordliste)
    return ordliste

def tel_førekomstar(filnamn):
    """
    Returnerer oppslagstabell over førekomster av
    ord på fila med namn filnamn.
    """
    ordliste = les_ordliste(filnamn)
    ordtabell = {}
    for ordet in ordliste:
        førekomstar = ordtabell.get(ordet, 0)
        ordtabell[ordet] = førekomstar + 1
    return ordtabell
    
def main():
    """
    ordliste = les_ordliste("uib.txt")
    n_ord = len(ordliste)
    print('Fila uib.txt har %d ord.'
          % n_ord)
    ordmengd = set(ordliste)
    n_ulike = len(ordmengd)
    print('Fila uib.txt har %d ulike ord.'
          % n_ulike)
    """
    ordtabell = tel_førekomstar("exphilord.txt")
    flest = max(ordtabell.values())
    grense = flest // 8
    print("Ord med minst %d førekomstar:" % grense)
    for ordet in ordtabell:
        if ordtabell[ordet] >= grense:
            print(ordet, ordtabell[ordet])
main()
