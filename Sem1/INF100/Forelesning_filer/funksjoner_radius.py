# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

from math import pi

def skriv_areal(radius):
    areal = pi*(radius**2)
    print("Arealet til ein sirkel med radius %.1f er %.1f."
          % (radius, areal))

def finn_areal(radius):
    areal = pi*(radius**2)
    return areal

radius1 = float(input("Radius til første sirkel: "))
skriv_areal(radius1)

radius2 = float(input("Radius til andre sirkel: "))
skriv_areal(radius2)  
    
areal3 = finn_areal(5)
print("Arealet til tredje sirkel er %.1f." % (areal3))