#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bil import Bil
from person import Person
# from Person import Person

def oppgave1():
    """ Tester ut klassen Bil
    """
    gertie = Bil('Gertie', 0, 0, 0)
    roadrunner = Bil('Roadrunner', 0, 0, 0)
    
    gertie.fyllBensin(20)
    roadrunner.fyllBensin(15)
    gertie.kjørØst(10)
    gertie.kjørSør(8)
    roadrunner.kjørNord(10)
    roadrunner.kjørØst(6)
    gertie.printStatus()
    roadrunner.printStatus()
    
    gertie.kjørVest(5)
    roadrunner.fyllBensin(10)
    roadrunner.kjørVest(5)
    gertie.printStatus()
    roadrunner.printStatus()

    
def oppgave2a():
    """
    Input: None
    Output: liste av samfunn i rekkefølge: per, trine, peder, tiril, petra
    """
    per = Person("Per Arne Kjelland", 25, "mann", 180, 7, 4)
    trine = Person("Trine Koss", 31, "kvinne", 168, 4, 7)
    peder = Person("Peder Kjekkas", 22, "mann", 182, 9, 8)
    tiril = Person("Tiril Piril", 35, "kvinne", 171, 3, 5)
    petra = Person("Petra Halvorsen", 23, "annet", 183, 7, 7)
    
    samfunn = [per, trine, peder, tiril, petra]
    return samfunn

    
def hent_alder(person):
    """ Hent alder
    Til bruk i oppgave 2b
    Input: Person objekt
    Output: alderen til personen (int)
    """
    return person.alder

def hent_lykke(person):
    return person.lykkenivå

def hent_sult(person):
    return person.sult_følelse

def hent_høyde(person):
    return person.høyde
    
def oppgave2b(samfunn):
    """ Sorter etter alder
    Input: Liste med personer i samfunn
    Output: Sorterte personer i samfunn etter alder
    """
    samfunn.sort(key = hent_alder, reverse=False)
    return samfunn
    
def oppgave2c(samfunn):
    """ Sorter etter hierarki
    Input: Liste med personer i samfunn
    Output: Sorterte personer i samfunn etter lykekenivå, sult_følelse, alder
    """
    samfunn.sort(key=lambda person: (hent_lykke(person), hent_sult(person), hent_høyde(person)), reverse=True)
    return samfunn

def main():
    """ Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt.
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet
    foran oppgave-funksjonen slik at den blir "skrudd på".
    Før du leverer kan det være lurt å sjekke alle funksjonene. Dette gjør
    du ved å fjerne alle #-tegnene nedenfor.
    """
    # Bil
    """
    oppgave1()
    print()
    """
    # Samfunn
    
    samfunn = oppgave2a()
    print(samfunn)
    
    sortert_samfunn = oppgave2b(samfunn)
    print(sortert_samfunn)

    hierarki = oppgave2c(samfunn)
    print(hierarki)

main()
