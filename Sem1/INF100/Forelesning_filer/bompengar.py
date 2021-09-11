#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for handtering av bilar som passerer bomstasjonar
@author: nmidd
"""

import time
from random import uniform, choice
from bil import Bil

bilar = {}  # Nøkkel: Registreringsnummer. Verdi: Bilobjekt
bomstasjonar = {'Laksevåg', 'Sandviken', 'Fjøsanger'}

def klokka(sekund):
    """ Returnerer eit tuppel på forma
    (år, månad, dag, time, minutt, sekund) som svarer til
    tidspunktet oppgitt i sekund etter 01.01.1970 """
    tid = time.localtime(sekund)
    return (tid.tm_year, tid.tm_mon, tid.tm_mday,
            tid.tm_hour, tid.tm_min, tid.tm_sec)

def nybil(regnr, eigar):
    """ Opprettar ein ny bil i registeret bilar.
    Returnerer det nye bilobjektet """
    bil = Bil(regnr, eigar)
    bilar[regnr] = bil
    return bil

def nybil_kode(bokstavkode, eigar):
    """ Opprettar ein ny bil med oppgitt
    bokstavkode i registeret bilar.
    Returnerer det nye bilobjektet. """
    bil = Bil.ny(bokstavkode, eigar)
    if bil is not None:
        regnr = bil.hent_regnr()
        bilar[regnr] = bil
    else:
        print('Kunne ikkje registrera bil med kode %s til %s'
              % (bokstavkode, eigar))
    return bil
    
def slett(regnr):
    """ Slettar bilen med oppgitt registreringsnummer,
    og returnerer tilhøyrande objekt. Returnerer None
    dersom det ikkje finst ein bil med oppgitt
    registreringsnr """
    if regnr in bilar:
        return bilar.pop(regnr)
    else:
        return None
    
def registrer(regnr, stasjon, sekund = None):
    """ Tar imot ein observasjon av eit registreringsnummer
    på ein bomstasjon. Returnerer passeringsobjektet. """
    if stasjon in bomstasjonar:
        bil = bilar[regnr]
        if sekund is None:
            tid = klokka(time.time())
        else:
            tid = klokka(sekund)
        passering = bil.ny_passering(tid, stasjon)
        return passering
    else:
        print('Ugyldig bomstasjon: ' + stasjon)
        return None
    

def simuler_passering(tidleg, seint, kort, lang):
    """ Lagar tilfeldige passeringsobjekt på tilfeldige
    tidspunktet i intervallet [tidleg, seint) oppgitt i
    sekund etter 01.01.1970. Tida mellom to passeringar
    er tilfeldig mellom kort og lang sekund.
    I kvar passering er alle bilar og bomstasjonar
    like sannsynlege. """
    sekund = tidleg + uniform(kort, lang)
    while sekund < seint:
        regnr = choice(list(bilar.keys()))
        stasjon = choice(list(bomstasjonar))
        registrer(regnr, stasjon, sekund)
        sekund += uniform(kort, lang)
    
def main():
    hans_sin_bil = nybil_kode('SU', 'Hans Hansen')
    oline_sin_bil = nybil_kode('SU', 'Oline Olsen')
    hans_reg = hans_sin_bil.hent_regnr()
    oline_reg = oline_sin_bil.hent_regnr()
    registrer(hans_reg, 'Sandviken')
    time.sleep(5)
    registrer(oline_reg, 'Laksevåg')
    for bil in bilar.values():
        bil.skriv_passeringar()
    
#    tidleg = time.time()
#    seint = tidleg + 4*60*60
#    simuler_passering(tidleg, seint, 1800, 3600)
#    for bil in bilar.values():
#        bil.skriv_passeringar()
        
main()
