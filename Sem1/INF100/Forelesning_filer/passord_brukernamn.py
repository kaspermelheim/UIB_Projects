# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:44:18 2019

@author: Kasper
"""

#Innlogging med passord og brukernamn

print('\n --- Innlogging til rabattering og prising av varer i butikk ---')

import sys

passord = "passord123"
username = "kaspermelheim"

username_input = input("Skriv inn brukernamn: ")
if username_input == username:
    print("Brukernamn godkjent.")
    print("Brukernamn: " +username + ".")
else:
    sys.exit("Feil brukernamn.")
passord_input = input("Skriv inn passord: ")
if passord_input == passord:
    print("Passord " +passord+ " godkjent.")
    print("Du er nå logget inn.")
else:
    sys.exit("Feil passord.")
    
pris = float(input("Ordinær pris: "))
rabpris = float(input("Rabattert pris: "))
grense = float(input("Rabattgrense: "))
kvantum = float(input("Kvantum: "))

if kvantum <= grense:
    betaling = kvantum * pris
else:
    betaling = grense * pris + (kvantum - grense)*rabpris
print("Til betaling: %.2f" % betaling )