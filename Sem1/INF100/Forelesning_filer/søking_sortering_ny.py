#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer søking i lister og sortering av lister
@author: nmidd
"""

from random import randint, choice
from time import time

def les_strengar(filnamn):
    """
    Returnerer ei liste med strengar lest
    frå fila med namn filnamn
    """
    with open(filnamn, 'r') as lesefil:
        strengliste = lesefil.read().split()
    return strengliste

def søk_etter_lengd1(liste, lengd):
    """
    Returnerer posisjonen til første element (f.eks. streng)
    i oppgitt liste med oppgitt lengd
    """
    for i in range(len(liste)):
        if len(liste[i]) == lengd:
            return i
    return -1

# Alternativt:
def søk_etter_lengd2(liste, lengd):
    """
    Returnerer posisjonen til første element (f.eks. streng)
    i oppgitt liste med oppgitt lengd
    """
    pos = -1
    i = 0
    while pos == -1 and i < len(liste):
        if len(liste[i]) == lengd:
            pos = i
        else:
            i += 1
    return pos

def søk_etter_lengste(liste):
    """
    Returnerer posisjonen til lengste element
    (f.eks. streng) i oppgitt liste
    """
    (pos, lengste) = (-1, -1)
    for i in range(len(liste)):
        if len(liste[i]) > lengste:
            (pos, lengste) = (i, len(liste[i]))
    return pos

def søk_etter_flest(liste, streng):
    """
    Returnerer posisjonen til strengen med
    flest førekomstar av karakterar i oppgitt streng
    """
    (pos, flest) = (-1, -1)
    for i in range(len(liste)):
        n = 0
        for karakter in streng:
            n += liste[i].count(karakter)
        if  n > flest:
            (pos, flest) = (i, n)
    return pos

def søk_sortering(liste):
    """
    Returnerer største verdi av pos slik at
    liste[0] <= liste[1] <= ... <= liste[pos]
    """
    pos = -1
    if len(liste) > 0:
        pos = 0
        while pos < len(liste)-1 and \
                liste[pos] <= liste[pos+1]:
            pos += 1
    return pos

def er_stigande(liste):
    """
    Returnerer True dersom liste er sortert i
    stigande rekkjefølgje, False elles
    """
    return søk_sortering(liste) == len(liste)-1
        
def byt(liste, i, j):
    """
    Byter om elementa i og j i liste
    """
    hjelp = liste[i]
    liste[i] = liste[j]
    liste[j] = hjelp

def sorter(liste):
    """
    Sorterer ei strengliste etter stigande strenglengd
    """
    n = len(liste)
    for i in range(n-1):
        minste = i
        minste_lengd = len(liste[i])
        for j in range(i+1, n):
            lengdj = len(liste[j])
            if lengdj < minste_lengd:
                minste = j
                minste_lengd = lengdj
        byt(liste, i, minste)


def lag_alfabetet():
    """
    Returnerer lista ['a', ..., 'z', 'æ', 'ø', 'å']
    """
    alfabetet = []
    for kode in range(ord('a'), ord('z')+1):
        alfabetet.append(chr(kode))
    alfabetet.append('æ')
    alfabetet.append('ø')
    alfabetet.append('å')
    return alfabetet

def lag_tilfeldig_liste(listelengd, maks_ordlengd):
    """
    Returnerer ei tilfeldig liste med listelengd strengar
    samansett av 1-maks_ordlengd bokstavar ('a'-'å')
    """
    strengliste = [None]*listelengd
    for i in range(listelengd):
        lengd = randint(1, maks_ordlengd)
        streng = ""
        for j in range(lengd):
            bokstav = choice(ALFABETET)
            streng += bokstav
        strengliste[i] = streng
    return strengliste

def søk(liste, f, verdi, args=[]):
    """
    Generisk søkefunksjon som returnerer posisjonen til
    første element i liste der funksjonen f
    returnerer verdien verdi.
    """
    for i in range(len(liste)):
        if f(liste[i], *args) == verdi:
            return i
    return -1

def forekomst(streng, karakterar):
    """
    Returnerer antal forekomstar i streng
    av karakterane i strengparameteren karakterar
    """
    n = 0
    for karakter in karakterar:
        n += streng.count(karakter)
    return n
        
def main():
    (n, m) = (6, 40)
    strengliste = lag_tilfeldig_liste(n, m)
    start_sorter = time()
    sorter(strengliste)
    slutt_sorter = time()
#    print(strengliste)
    print('Tid til sortering av %d strengar: %.1f sekund'
          % (n, slutt_sorter-start_sorter))
    
    liste = ['CCC', 'aa', 'B']
    poslen2 = søk(liste, len, 2)
    pos3c = søk(liste, forekomst, 3, ['Cc'])
    if poslen2 >= 0:
        print('Strengen %s er den første med lengd 2' % liste[poslen2])
    if pos3c >= 0:
        print('Strengen %s er den første med 3 "c" eller "C"' % liste[pos3c])

ALFABETET = lag_alfabetet()    
main()
