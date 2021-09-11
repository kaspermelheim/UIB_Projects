#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finn gjennomsnittleg nedbør på ulike stader til ulike tidspunkt
@author: nmidd
"""

from matplotlib import pyplot
from random import random

def lag_nedbør(n_stader, n_dagar, sannsyn, maks):
    """
    Lagar og returnerer matrise med tilfeldige nedbørskvanta på
    n_stader stader over n_dagar dagar. Sannsynet for nedbør
    er gitt med parameteren sannsyn, og teoretisk største
    nedbørskvantum er gitt med maks
    """  
    nedbør = []
    for stad in range(n_stader):
        nedbør.append([])
        for dag in range(n_dagar):
            regnversdag = random()
            if regnversdag <= sannsyn: 
                regn = random()*maks
                nedbør[stad].append(regn)
            else:
                nedbør[stad].append(0.0)
    return nedbør

def les_nedbør(n_stader, n_dagar):
    """
    Les nedbørsdata frå n_stader stader over n_dagar dagar.
    Returnerer ei matrise med innleste data
    """
    nedbør = []
    for stad in range(n_stader):
        nedbør.append([])
        print('Nedbør (mm) på stad %d: ' % (stad+1))
        for dag in range(n_dagar):
            innlest = float(input('\tDag %d: ' % (dag+1)))
            nedbør[stad].append(innlest)
    return nedbør

def skriv_nedbør(nedbør):
    """
    Skriv ut ei nedbørsmatrise
    """
    print('      ', end='')
    for dag in range(len(nedbør[0])):
        print(' Dag%2d' % (dag+1), end='')
    print()
    
    for stad in range(len(nedbør)):
        print('Stad%2d' % (stad+1), end='')
        for dag in range(len(nedbør[stad])):
            print('%6.1f' % nedbør[stad][dag], end='')
        print()

def skriv_snitt_stad(nedbør):
    """
    Reknar ut og skriv ut gjennomsnittleg nedbør for kvar stad
    """
    n_stader = len(nedbør)
    for stad in range(n_stader):
        summen = sum(nedbør[stad])
        n_dagar = len(nedbør[stad])
        if n_dagar > 0:
            snitt = summen/n_dagar
            print("Totalnedbør på stad %d: %.1f" % (stad+1, summen))
            print("Gjennomsnittsnedbør på stad %d: %.1f" % (stad+1, snitt))
            
        
def skriv_snitt_dag(nedbør):
    """
    Reknar ut og skriv ut gjennomsnittleg nedbør for kvar dag
    """
    n_stader = len(nedbør)
    if n_stader > 0:
        n_dagar = len(nedbør[0])
        for dag in range(n_dagar):
            summen = 0.0
            for stad in range(n_stader):
                summen += nedbør[stad][dag]
            snitt = summen/n_stader
            print("Totalnedbør på dag %d: %.1f" % (dag+1, summen))
            print("Gjennomsnittsnedbør på dag %d: %.1f" % (dag+1, snitt))
        
def plott(nedbør):
    """
    Plottar ei kurve over nedbør for kvar stad som funksjon av tid
    """
    for stad in range(len(nedbør)):
        pyplot.plot(nedbør[stad])
    pyplot.show()
    
def teikn_histogram(liste, tittel):
    """
    Teiknar histogram som svarer til verdiane i liste.
    Titlane på søylene er gitt i lista tittel.
    """
    n_stader = len(liste)
    for stad in range(n_stader):
        pyplot.bar("Stad " + str(stad+1), liste[stad])
    pyplot.title(tittel)
    pyplot.show()
    
def teikn_hist_maks(nedbør):
    """
    Teiknar histogram over maksimalt nedbørskvantum for kvar stad
    Returnerer ei liste over verdiane i histogrammet
    """
    n_stader = len(nedbør)
    maksliste = [None]*n_stader
    for stad in range(n_stader):
        maks = max(nedbør[stad])
        maksliste[stad] = maks
    teikn_histogram(maksliste, "Maksimalnedbør")
    return maksliste

def teikn_hist_tot(nedbør):
    """
    Teiknar histogram over totalt nedbørskvantum for kvar stad.
    Returnerer ei liste over verdiane i histogrammet
    """
    n_stader = len(nedbør)
    maksliste = [None]*n_stader
    for stad in range(n_stader):
        maks = sum(nedbør[stad])
        maksliste[stad] = maks
    teikn_histogram(maksliste, "Maksimalnedbør")
    return maksliste

def finn_kor_maks(nedbør, dag):
    """
    Returnerer indeksen til staden der det regna mest
    på oppgitt dag
    """
    stad_maks = -1
    maks = -1
    n_stader = len(nedbør)
    for stad in range(n_stader):
        regn = nedbør[stad][dag]
        if regn > maks:
            stad_maks = stad
            maks = regn
    return stad_maks

def teikn_kake(nedbør):
    """
    Teiknar kakediagram over kor ofte kvar stad er den med mest nedbør
    """
    n_stader = len(nedbør)
    if n_stader > 0:
        n_stader = len(nedbør[0])
        frekvens = [0]*n_stader
        tekst = ["Stad "]*n_stader
        for stad in range(n_stader):
            tekst[stad] += str(stad+1)
        for dag in range(n_dagar):
            stad = finn_kor_maks(nedbør, dag)
            frekvens[stad] += 1
        pyplot.pie(frekvens, labels = tekst)

# Programmet:
n_stader = int(input('Talet på stader: '))
n_dagar = int(input('Talet på dagar: '))
nedbør = lag_nedbør(n_stader, n_dagar, 0.7, 50.0)
print()
skriv_nedbør(nedbør)
# skriv_snitt_stad(nedbør)
# skriv_snitt_dag(nedbør)
# plott(nedbør)
# teikn_hist_maks(nedbør)
teikn_hist_tot(nedbør)
# teikn_kake(nedbør)
