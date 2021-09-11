#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse som representerer ei motorvogn
@author: nmidd
"""

from passering import Passering

class Bil:
    """
    Motorvogn representert med registreringsnummer, eigar
    og bompasseringar
    """
    
    _bokstavkoder = {'SU', 'DR', 'EL', 'RL', 'VJ'}
    _neste_ledige = {}
    for kode in _bokstavkoder:
        _neste_ledige[kode] = 10000
    
    def __init__(self, regnr, eigar):
        """
        Opprettar ei motorvogn
        """
        self._regnr = regnr
        self._eigar = eigar
        self._passeringar = []
    
    def hent_regnr(self):
        """ Returnerer registreringsnummeret """
        return self._regnr
        
    def hent_eigar(self):
        """ Returnerer eigaren """
        return self._eigar
    
    def n_passeringar(self):
        """ Returnerer talet på passeringar så langt """
        return len(self._passeringar)
    
    def hent_passering(self, i):
        """ Returnerer den i-te passeringen,
        None dersom det ikkje finst ein slik passering """
        if i in range(self.n_passeringar()):
            return self._passeringar[i]
        else:
            return None
    
    def hent_siste_passering(self):
        """ Returnerer den siste passeringen,
        None dersom det ikkje finst passeringar """
        if self.n_passeringar() > 0:
            return self._passeringar[-1]
        else:
            return None
        
    def ny_passering(self, tid, stasjon):
        """ Registrerer ein ny passering,
        returnerer referanse til nytt passeringsobjekt"""
        passering = Passering(self, tid, stasjon)
        self._passeringar.append(passering)
        return passering
        
    def skriv_passeringar(self):
        """ Skriv alle passeringar til skjermen """
        print('Passering av motorvogn med kjenneteikn %7s (%s):'
              % (self._regnr, self._eigar))
        for passering in self._passeringar:
            passering.skriv()
   
         
    def ny(bokstavkode, eigar):
        """ Returnerer referanse til nytt bilobjekt
        registrert med oppgitt bokstavkode på oppgitt eigar """
        bil = None
        if bokstavkode in Bil._bokstavkoder:
            nr = Bil._neste_ledige[bokstavkode]
            if nr <= 99999:
                regnr = bokstavkode + str(nr)
                bil = Bil(regnr, eigar)
                Bil._neste_ledige[bokstavkode] += 1
        return bil
