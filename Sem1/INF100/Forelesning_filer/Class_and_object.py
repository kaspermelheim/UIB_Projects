#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finn gjennomsnittet av 3 tilfeldig genererte bankkontoar."
@author: kasper

"""
from random import randint

#personer = ["Kasper", "Markus", "Oskar"]
#banker = ["Luster Sparebank", "Danske Bank", "Sparebank Vest", "S-Banken"] 
persons = {"Kasper" : "Luster Sparebank",
           "Markus" : "Danske Bank",
           "Oskar" : "Sparebank Vest"}

class Bankkonto():
    
    def __init__(self, namn, bank, penger, kontoer):
        self.namn = namn
        self.bank = bank
        self.penger = penger
        self.kontoer = kontoer
        
    def __repr__(self):
        return("Person: {}. Bank: {}. Totalt {} kroner fordelt på {} kontoer.".format(self.namn,
                self.bank, self.penger, self.kontoer))
        
    def legg_inn_penger(self, tillegg):
        self.penger += tillegg
        return self.penger
    
    def ta_ut_penger(self, uttak):
        if uttak > self.penger:
            return "Valgt uttak overstiger summen {} kr i banken.".format(self.penger)
        else:
            self.penger -= uttak
            return self.penger

def lag_kontoer():
    summen = 0
    
    for i, y in enumerate(persons):
        antall_penger = randint(0,300000)
        antall_kontoer = randint(0,10)
        summen += antall_penger
        min_konto = Bankkonto(y, persons[y], antall_penger, antall_kontoer)
        print(min_konto)
    return summen

def finn_gjennomsnitt(summen):
    for i in range(len(persons)):
        personer = i+1
    gjennomsnitt = summen / personer
    #print("Gjennomsnittet:",gjennomsnitt, "kroner.")
    print("Gjennomsnitt: %.2f kroner." % gjennomsnitt)

def styre_konto():
    bank = input("Navn på bank: ")
    namn = input("Navn på kontoeier: ")
    penger = randint(0,30000)
    kontoer = randint(1, 3)
    
    min_konto = Bankkonto(namn, bank, penger, kontoer)
    print(min_konto)
    
    ferdig = False
    while not ferdig:
        spm = input("Vil du ha innskudd eller uttak (dersom nei, trykk enter): ")
        if spm == "innskudd":
            antall = int(input("Hvor mye vil du legge inn: "))
            min_konto.legg_inn_penger(antall)
        elif spm == "uttak":
            antall = int(input("Hvor mye vil du ta ut: "))
            min_konto.ta_ut_penger(antall)
        else:
            ferdig = True
    
    print("Ny status på bank:", min_konto)

def main():
    print("------------------- Bankkonto ---------------------\n")
    #summen = lag_kontoer()
    #finn_gjennomsnitt(summen)
    
    styre_konto()
    print("-----------------------------------------------------")
    
main()

#min_konto = Bankkonto("Kasper Melheim", "Luster Sparebank", 350000, 3)
#print(min_konto)
