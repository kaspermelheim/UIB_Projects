#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse som representerer ein bompassering
@author: nmidd
"""

class Passering:
    """ Bompassering representert med motorvogn,
    tid og bomstasjon """
    
    def __init__(self, bil, tid, stasjon):
        """ Opprettar ein passering """
        self._bil = bil
        self._tid = tid
        self._stasjon = stasjon
        
    def hent_bil(self):
        """ Returnerer bilen som har passert """
        return self._bil
    
    def hent_tid(self):
        """ Returnerer tidspunktet for passeringa """
        return self._tid    
    
    def hent_stasjon(self):
        """ Returnerer bomstasjonen som blei passert """
        return self._stasjon
    
    def skriv(self):
        """ Skriv informasjon om passeringa til skjermen på forma
        'SU12345 passerte Sandviken 11.04.2019 kl. 10:15:01' """
        print('\t%7s passerte %s %02d.%02d.%4d kl. %02d:%02d:%02d'
              % (self._bil.hent_regnr(), self._stasjon,
                 self._tid[2], self._tid[1], self._tid[0],
                 self._tid[3], self._tid[4], self._tid[5]))
