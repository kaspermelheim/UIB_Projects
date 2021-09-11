# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:50:24 2019

@author: Kasper
"""

namn = input("Skriv namnet ditt: ")
namn_lengd = len(namn)
print(namn_lengd)


if namn_lengd > 10:
    print("Namnet er lengre enn 10 karakterar.")
    forkorting = namn[:10]
    print("Forkorta versjon: " ,forkorting,".")
elif namn_lengd < 10:
    print("Namnet er kortere enn 10 karakterar.")
else:
    print("Namnet er 10 karakterer langt, og treng ikkje forkorting.")
    
print("Ha det bra, " + namn + "!")