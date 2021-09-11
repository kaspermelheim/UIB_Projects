#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse som representerer ein
deltakar i verdscupen i vinteridrett
@author: nmidd
"""

class Deltakar:
    """
    Definisjon av klassen for deltakarar i
    verdscupen i vinteridrett
    """
    
    IDRETTAR = {'Langrenn', 'Hopp',
                'Skiskyting', 'Alpint'}
    
    def __init__(self, namn, idrett):
        """
        Opprettar deltakar med oppgitt namn og idrett
        """
        self._namn = namn
        self._idrett = idrett
        self._poeng = 0
        
    def __repr__(self):
        representasjon = "%s (%s): %d" % (self._namn, self._idrett, self._poeng)
        return representasjon
    
    def __gt__(self, d):
        return self._poeng > d._poeng
    
    def __lt__(self, d):
        return d > self
    
    def __ge__(self, d):
        return not (self < d)
    
    def __le__(self, d):
        return not (self > d)
    
    def __eq__(self, d):
        return self <= d and self >= d
        
    def hent_namn(self):
        """ Returnerer deltakarnamnet """
        return self._namn
    
    def hent_idrett(self):
        """ Returnerer idretten til deltakaren """
        return self._idrett
    
    def hent_poeng(self):
        """ Returnerer poenga til deltakaren """
        return self._poeng
    
    def registrer(self, nye):
        """ Aukar poengtalet til deltakaren """
        self._poeng += nye
        
    def nullstill(self):
        """ Nullstiller poenga til deltakaren """
        self._poeng = 0
        
    def set_idrett(self, idrett):
        """ Gir ny idrett til deltakaren """
        if idrett in Deltakar.IDRETTAR:
            self._idrett = idrett
    
        
