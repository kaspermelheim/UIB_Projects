# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:20:00 2019

@author: Kasper
"""

class Person:
    
    def __init__(self, navn, alder, kjønn, høyde, sult_følelse, lykkenivå):
        self.navn = navn
        self.alder = alder
        self.kjønn = kjønn
        self.høyde = høyde
        self.sult_følelse = sult_følelse
        self.lykkenivå = lykkenivå
        
    def __repr__(self):
        return("{}".format(self.navn))
    
        