#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eksempel på operasjonar på ei liste med innleste tal
@author: nmidd
"""

def skriv(talliste):
    """
    Skriv ut verdiane i talliste,
    og posisjonane dei står i
    """
    for i in range(len(talliste)):
        print("%3d %7.2f" % (i, talliste[i]))

def store_avvik(talliste):
    """
    Skriv gjennomsnittsverdien i ei liste,
    og alle avvik på minst 50% i lista
    """
    summen = sum(talliste)
    n = len(talliste)
    snitt = summen/n
    print("Store avvik frå gjennomsnittet på %4.2f: "
          % snitt)
    print("%7s %7s" % ("Verdi", "Avvik"))
    for tal in talliste:
        avvik = tal - snitt
        if abs(avvik) > (snitt/2):
            print("%7.2f %7.2f" % (tal, avvik))
            
            
def to_like(talliste):
    """
    Finn første forekomst av to
    like naboelement i talliste
    """
    i = 0
    while i < len(talliste)-1:
        if talliste[i] == talliste[i+1]:
            return i
        i += 1 #Gå til neste element i talliste
    return -1

def main():
    n = int(input('Antal observasjonar: '))
    talliste = []
    for i in range(n):
        tal = float(input('%3d. observasjon: ' % (i+1)))
        talliste.append(tal)
        
    # Skriv lista:
    skriv(talliste)
    # Skriv store avvik i lista:
    store_avvik(talliste)
    # Skriv første forekomst av to like etterfølgjande tal i lista:
    pos = to_like(talliste)
    if pos >= 0:
        print('Elementa i posisjonane %d og %d er begge lik %.1f' %
              (pos, pos+1, talliste[pos]))
    else:
        print('Lista har ikkje to like etterfølgjande element.')
    
main()
