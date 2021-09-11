#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finn utvegen i ein labyrint
@author: nmidd
"""

from random import random, randint
from grafikk import vis

OPEN = ' '
LUKKA = '*'

def dim(labyrint):
    """
    Returnerer talet på rekkjer og søyler i oppgitt
    todimensjonale liste som eit tuppel
    """
    return (len(labyrint), len(labyrint[0]))

def les_labyrint(filnamn):
    """
    Les ein labyrint frå fil, og returnerer han
    som ei todimensjonal boolsk liste
    """
    labyrint = []
    with open(filnamn, 'r') as lesefil:
        for streng in lesefil:
            rekkje = []
            for j in range(len(streng) - 1):
                rekkje.append(streng[j] == OPEN)
            labyrint.append(rekkje)
    return labyrint

def tilf_labyrint(m, n, p):
    """
    Returnerer ein tilfeldig generert labyrint
    med m rekkjer og n søyler, der kvar celle har
    sannsynet p for å vera open
    """
    labyrint = []
    for i in range(m):
        rekkje = []
        for j in range(n):
            tilfeldig = random()
            rekkje.append(tilfeldig <= p)
        labyrint.append(rekkje)
    return labyrint

def skriv_labyrint(labyrint, filnamn):
    """
    Skriv oppgitt labyrint til tekstfila med oppgitt namn
    """
    (m, n) = dim(labyrint)
    with open(filnamn, 'w') as skrivefil:
        for i in range(m):
            for j in range(n):
                if labyrint[i][j]:
                    skrivefil.write(OPEN)
                else:
                    skrivefil.write(LUKKA)
            skrivefil.write('\n')

def finn_naboar(labyrint):
    """
    Returnerer ein oppslagstabell over opne naboceller
    til kvar opne celle i oppgitt labyrint
    """
    naboar = {}
    (m, n) = dim(labyrint)
    for i in range(m):
        for j in range(n):
            if labyrint[i][j]:
                naboar[(i,j)] = set()
                kandidatar = {(i-1, j), (i+1,j),
                              (i, j-1), (i, j+1)}
                for (u,v) in kandidatar:
                    if u in range(m) and v in range(n):
                        if labyrint[u][v]:
                            naboar[(i,j)].add((u,v))
    return naboar

def initier_utveg(naboar, m, n):
    """
    Returnerer ein tabell med oppslaget None for
    kvar opne celle på kanten av oppgitt labyrint
    """
    utveg = {}
    for (i,j) in naboar:
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            utveg[(i,j)] = None
    return utveg

def oppdater_utveg(naboar, utveg):
    """
    Legg til oppslag i tabellen utveg for kvar opne
    celle (celle) som har ei nabocelle (nabo) som alt finst i
    tabellen. Oppslaget skal ha verdien utveg[celle] = nabo.
    Returnerer True dersom vi er ferdige
    (ingen nye oppslag blei lagt til), False elles
    """
    ferdig = True
    for celle in naboar:
        if celle not in utveg:
            for nabo in naboar[celle]:
                if nabo in utveg:
                    utveg[celle] = nabo
                    ferdig = False
    return ferdig
    
        
def finn_utveg(naboar, m, n):
    """
    Returnerer ein tabell med eit oppslag for alle opne
    celler som det finst utveg frå. Oppslaget er None
    for opne celler på kanten av labyrinten, og nabocella
    vi skal gå til for andre opne celler.
    """
    utveg = initier_utveg(naboar, m, n)
    ferdig = False
    while not ferdig:
        ferdig = oppdater_utveg(naboar, utveg)
    return utveg

def skriv_utveg(utveg, start):
    """
    Dersom det finst utveg frå celle start i labyrinten,
    skriv utvegen på skjermen. Elles skriv feilmelding.
    """
    if start in utveg:
        print("\tStart ved (%d, %d)" % start)
        celle = start
        while utveg[celle] is not None:
            print("\tGå til (%d, %d)" % utveg[celle])
            celle = utveg[celle]
        print("\tGå ut av labyrinten ved (&d, &d)" % celle)
    else:
        print("\tIngen utveg frå (%d, &d)" % start)
    
def skriv_utveg_frå_innlest_celle(utveg):
    """
    Les celle frå tastaturet, og skriv utvegen derifrå
    dersom det finst ein utveg. Skriv feilmelding elles.
    """
    streng = input('Celle du vil finna utvegen frå: ')
    ordet = streng.split(",")
    celle = (int(ordet[0]), int(ordet[1]))
    skriv_utveg(utveg, celle)
    
def skriv_utveg_frå_tilfeldig_celle(utveg, m, n):
    """
    Genererer tilfeldig celle, og skriv utvegen derifrå
    dersom det finst ein utveg. Skriv feilmelding elles.
    """
    celle = (randint(0, m-1), randint(0, n-1))
    skriv_utveg(utveg, celle)
    
def lag_liste(utveg, start):
    """
    Returnerer utvegsliste frå celle start i labyrinten
    dersom ein utveg finst, tom liste elles
    """
    liste = []
    celle = start
    while celle is not None:
        liste.append(celle)
        celle = utveg[celle]
    return liste
    
def main():
    labyrint = tilf_labyrint(100, 100, 0.7)
 #  labyrint = les_labyrint('labyrint.txt')
    (m, n) = dim(labyrint)
    naboar = finn_naboar(labyrint)
    utveg = finn_utveg(naboar, m, n)
    """celle = None
    while not celle in utveg:
        celle = (randint(0, m-1), randint(0, n-1))
    liste = lag_liste(utveg, celle)
    if len(liste) > 0:
        vis(labyrint, liste)"""
    skriv_utveg_frå_tilfeldig_celle(utveg, m, n)
        
main()