#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:34:44 2019

@author: roler
"""

class Person:
    def __init__(self, navn, alder, kjønn, høyde, sult_følelse, lykkenivå):
        self.navn = navn                 #(string)"Navn på person"
        self.alder = alder               #(int)   "Alder i år"
        self.kjønn = kjønn               #(string)"kjønn, mann, kvinne, annet"
        self.høyde = høyde               #(int)   "Høyde til personen"
        self.sult_følelse = sult_følelse #(int)   "Nåværende sultfølelse, 1-10"
        self.lykkenivå = lykkenivå       #(int)   "Nåværende lykkenivå, 1-10" 
    
    def __repr__(self):
      return(self.navn)
    
    def __lt__(self, other):
        return( (self.lykkenivå, self.sult_følelse, self.alder) < 
               (other.lykkenivå, other.sult_følelse, other.alder) )    
    
