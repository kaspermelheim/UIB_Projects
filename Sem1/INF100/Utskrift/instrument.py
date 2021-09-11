#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oppgåve 6, eksamen inf100, våren 2019
@author: nmidd
"""

rapportar = []
status = {}

def registrer(typen, laborant, vellukka):
    """
    Oppgåve 6a
    Registrerer eit eksperiment med oppgitt resultat
    (parameteren vellukka) utført av oppgitt laborant på
    instrument av oppgitt type.
    """
    rapport = (typen, laborant, vellukka)
    rapportar.append(rapport)
    nystatus = status.get(typen, [0, 0])
    # Alternativ 1
    """
    nystatus[int(vellukka)] += 1
    status[typen] = nystatus
    """
    # Atlernativ 2
    if vellukka: 
        nystatus[1] += 1
    else:
        nystatus[0] += 1
    status[typen] = nystatus
    return status
    
def godkjent(typen):
    """
    Oppgåve 6b
    Returnerer boolsk verdi som seier om instrumentet av
    oppgitt type er godkjent.
    """
    s = status.get(typen, [0,0])
    tot = sum(s)
    return tot >= 10 and s[1] >= 0.9*tot

def oversikt():
    """
    Oppgåve 6c
    Returnerer oppslagstabell der nøklane er alle
    registrerte instrumenttypar, og tilhøyrande verdiar
    seier om instrumenttypen er godkjent.
    """
    svar = {}
    for typen in status:
        """
        Alternativ:
            
        if godkjent(typen) == True:
            svar[typen] = True
        elif godkjent(typen) == False:
            svar[typen] = False
        """
        svar[typen] = godkjent(typen)
    return svar
def konkluder(godkjente, underkjente):
    """
    Oppgåve 6d
    Skriv alle registrerte instrumenttypar til fil. Dei
    godkjente skal skrivast til file med namn gitt med
    parameteren godkjente, dei andre til fila med namn gitt
    med parameteren underkjente.
    """
    filgod = open(godkjente, "w")
    filunder = open(underkjente, "w")
    filgod.write("Godkjente instrument: \n")
    filunder.write("Underkjente instrument: \n")
    konklusjon = oversikt()
    for typen in konklusjon:
        if konklusjon[typen]:
            filgod.write(typen + "\n")
        else:
            filunder.write(typen + "\n")
    filgod.close()
    filunder.close()
    
def plukk(laborant):
    """
    Oppgåve 6e
    Returnerer liste med alle rapportar
    (tuppel) registrerte av oppgitt laborant.
    """
    utplukk = []
    for rapport in rapportar:
        if rapport[1] == laborant:
            utplukk.append(rapport)
    return utplukk
def slett(laborant):
    """
    Oppgåve 6f
    Slettar alle rapportar registrerte av oppgitt laborant.
    """
    sletteliste = plukk(laborant)
    for rapport in sletteliste:
        (typen, vellukka) = (rapport[0], rapport[2])
        rapportar.remove(rapport)
        nystatus = status[typen]
        nystatus[int(vellukka)] -= 1
    return len(sletteliste)

def verifiser(godkjente, underkjente):
    """
    Oppgåve 6g
    Verifiserer at alle instrumenttypar lagra på fila med
    namn godkjente (underkjente) faktisk er godkjente
    (underkjente). Skriv feilmelding for alle avvik.
    Returnerer True dersom alt er rett, False elles
    """
    filgod = open(godkjente, "r")
    filunder = open(godkjente, "r")
    filgod.readline()
    filunder.readline()
    godliste = filgod.readlines()
    underliste = filunder.readlines()
    filgod.close()
    filunder.close()
    ok = True
    for t in godliste:
        typen = t.strip()
        if typen in status:
            if not godkjent(typen):
                print("Underkjent instrument %s på fil for godkjente." % typen)
                ok = False
        else:
            print("Ukjent instrument %s på fil for godkjente." % typen)
            ok = False
    for t in underliste:
        typen = t.strip()
        if typen in status:
            if godkjent(typen):
                print("Godkjent instrument %s på fil for underkjente. " % typen)
                ok = False
        else:
            print("Ukjent instrument %s på fil for underkjente." % typen)
            ok = False
            
    return ok
        


def main():
    registrer('nano1', 'Martha', True)
    registrer('bio-x', 'Martha', True)
    registrer('nano1', 'Dag', False)
    print(status)
    
    print(oversikt())
    konkluder('godkjente.txt', 'underkjente.txt')
    print(plukk('Martha'))
    slett('Dag')
    print(verifiser('godkjente.txt', 'underkjente.txt'))

main()
