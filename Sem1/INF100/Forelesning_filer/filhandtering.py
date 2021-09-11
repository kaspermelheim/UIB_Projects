#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les namn frå tastatur og skriv dei til fila 'mentor.txt'
Les namna frå fila, skriv dei til skjermen
@author: nmidd
"""

def skriv_til_fil(filnamn, tilføy = False):
    """
    Skriv mentornamn innleste
    frå tastaturet til ei tekstfil
    """
    modus = 'w'
    if tilføy:
        modus = 'a'
    mentorfil = open(filnamn, modus)
    ferdig = False
    while not ferdig:
        namn = input('Namn på mentor: ')
        if len(namn) > 0:
            mentorfil.write(namn + '\n')
        else:
            ferdig = True
    mentorfil.close()

# Alternativ 1:
def les_frå_fil1(filnamn):
    """
    Skriv mentornamn leste frå
    ei tekstfil ut i konsollen
    """
    mentorfil = open(filnamn, 'r')
    ferdig = False
    while not ferdig:
        namn = mentorfil.readline()
        namn = namn[:-1]
        if len(namn) > 0:
            print(namn)
        else:
            ferdig = True
    mentorfil.close()

# Alternativ 2:
def les_frå_fil2(filnamn):
    """
    Skriv mentornamn leste frå
    ei tekstfil ut i konsollen
    """
    with open(filnamn, 'r') as mentorfil:
        for namn in mentorfil:
            print(namn[:-1])
    
def les_fil_til_streng(filnamn):
    """
    Les mentornamn frå ei tekstfil,
    og plasserer dei i ein streng
    som blir returnert
    """
    mentorfil = open(filnamn, "r")
    streng = mentorfil.read()
    mentorfil.close()
    mentorfil.close()
    return streng
    

    
def les_fil_til_liste(filnamn):
    """
    Les mentornamn frå ei tekstfil,
    og plasserer dei i ei liste
    som blir returnert
    """
    mentorfil = open(filnamn, "r")
    liste = mentorfil.readlines()
    mentorfil.close()
    return liste

# Alternativ 1:
def snu1(namn):
    """
    Returnerer ein streng oppgitt på forma
    'etternamn, førenamn' omgjort til
    'førenamn etternamn'
    """
    komma = namn.find(",")
    etternamn = namn[:komma].strip()
    førenamn = namn[komma+1].strip()
    return førenamn + " " + etternamn

# Alternativ 2:        
def snu2(namn):
    """
    Returnerer ein streng oppgitt på forma
    'etternamn, førenamn' omgjort til
    'førenamn etternamn'
    """
    ordliste = namn.split(",")
    etternamn = ordliste[0].strip()
    førenamn = ordliste[1].strip()
    return førenamn + " " + etternamn

def fjern_kom(streng):
    """
    Returnerer strippa kopi av delstrengen
    til, men ikkje med, første '#' i streng
    """
    kopi = streng
    pos = kopi.find("#")
    if pos >= 0:
        kopi = kopi[:pos]
    return kopi.strip()
        
def snu_namn_på_fil(namn_gammal, namn_ny):
    """
    Skriv alle strengar på forma
    'etternamn, førenamn' i fila namn_gammal
    til fila namn_ny omgjort til forma
    'førenamn etternamn'
    """
    with open(namn_gammal, "r") as lesefil:
        with open(namn_ny, "w") as skrivefil:
            for namn in lesefil:
                kopi = fjern_kom(namn)
                if len(kopi) > 0:
                    omvendt = snu2(kopi)
                    skrivefil.write(omvendt + "\n")
            
    
    
def main():
     skriv_til_fil('mentor.txt', True)
#     les_frå_fil2('mentor.txt')
#     mentorstreng = les_fil_til_streng('mentor.txt')
#     print('Streng:', mentorstreng)
#     mentorliste = les_fil_til_liste('mentor.txt')
#     print('Liste:', mentorliste)
#     snu_namn_på_fil('etterfør_kom.txt', 'føretter.txt')
    
main()
