#!/usr/bin/env python
# Kasper Melheim
# -*- coding: utf-8 -*-

import random


def formaterNavn(navn):
    """ Formaterer navnene i mengden navn slik at navnene er 
    kommasepererte og har `og` mellom de to siste navnene

    >>> formaterNavn({})
    ''
    >>> formaterNavn({'a'})
    'a'
    """

    if len(navn) == 0:
        return ''
    elif len(navn) == 1:
        return navn.pop()
    else:
        navneListe = list(navn)
        return ", ".join(navneListe[:-1]) + " og " + navneListe[-1]


personer = {"Atle", "Erna", "Tone", "Celine", "Pål", "Linda", "Ragnar",
           "Gunnar", "Inger", "Irmelin", "Arnfinn", "Oda", "Sebastian", "Ann",
           "Emilie", "Hanna", "Beate", "Ina"}
facebookBrukere = {"Atle", "Pål", "Irmelin", "Arnfinn", "Oda", "Sebastian",
                   "Hanna", "Beate"}
instagramBrukere = {"Erna", "Celine", "Pål", "Linda", "Inger", "Irmelin",
                    "Oda", "Emilie", "Beate"}

def oppgave1():
    """ Finner ut hvem som hører til hvor i et 
    Facebook-Instagram venn-diagram.
    """
    print("Personene som har Facebook:",formaterNavn(facebookBrukere))
    
    print("Personene som har Instagram:",formaterNavn(instagramBrukere))
    
    facebookBruker = facebookBrukere.difference(instagramBrukere)
    print("Personene som kun har Facebook:",formaterNavn(facebookBruker))
    
    beggeBruker = facebookBrukere.intersection(instagramBrukere)
    print("Personene som har Facebook og Instagram:",formaterNavn(beggeBruker))
    ingen = set()
    for person in personer:
        if person not in facebookBrukere:
            if person not in instagramBrukere:
                ingen.add(person)
    print("Personene uten Facebook og Instagram:",formaterNavn(ingen))
        
    
    


def oppgave2():
    """ Samler data om de mest brukte programmeringsspråkene fra en csv-fil.
    """
    csvfil = open("mostPopularLanguages.csv", "r")
    csvliste = csvfil.readlines()
    csvfil.close()
        
    """
    Lager 2 liste der posisjon "i" i listene har verdier som hører til
    hverandre.
    """
    
    språk_liste = []
    prosent_liste = []
    
        
    for tegn in csvliste:
        posListe = tegn.split(";")
        språk = posListe[0].strip()
        prosent = posListe[1].strip()
        språk_liste.append(språk)
        prosent_liste.append(prosent)
        
    """
    Fjerner titlene "Language" og "Usage" for å få lister kun bestående av
    verdiene vi er intereserte i.
    """
    del prosent_liste[0]
    del språk_liste[0]
    
    """
    Lager en liste med med hvert programmeringspråk og prosenten som hører
    til språket i egen nøstet liste.
    """
    resultat = []
    for x, y in enumerate(språk_liste):
        resultat.append([språk_liste[x], prosent_liste[x]])
    
    for i in range(len(resultat)):
        if resultat[i][0] == "Python":
            python_prosent = float(resultat[i][1])
            print("Python scorte %.3f prosent." % python_prosent)
        elif resultat[i][0] == "C#":
            csharp_prosent = float(resultat[i][1])
            differanse = python_prosent - csharp_prosent
            print("Python fikk %.3f prosent bedre score enn C#." % differanse)
                  
    summen = 0
    for n in range(len(resultat)):
        summen += float(resultat[n][1])
    print("De 10 største språkene utgjør %.3f prosent." % summen)
            
    """
    Alternativ metode der eg bruker 2 lister, ein for programmeringspråk,
    og ein for prosent.
    
    for i in range(len(språk_liste)):
        if språk_liste[i] == "Python":
            print("Python scorte %.3f prosent. " % float(prosent_liste[i]))
            prosent1 = float(prosent_liste[i])
        elif språk_liste[i] == "C#":
            prosent2 = float(prosent_liste[i])
            differanse = prosent1 - prosent2
            print("Python fikk %.3f og C# fikk %.3f. Python scorte %.3f prosent mer enn C#." 
                  % (prosent1, prosent2, differanse))
    
    summen = 0
    for n in range(len(prosent_liste)):
        summen += float(prosent_liste[n])
    print("De 10 største språkene utgjør %.3f prosent." % summen)
       """ 
    
                

def oppgave3(filnamn, tilføy = False):
    """ 
    Skriver resultatet av et myntkast-experimentet til en csv-fil. 
    Verdien 0 tilsvarer mynt, verdien 1 tilsvarer kron.
    """
    modus = 'w'
    if tilføy:
        modus = 'a'
    skrivefil = open(filnamn, modus)
    ferdig = False
    
    skrivefil.write("Måned;Resultat;Venn1;Venn2;Stilling\n")
    venn1 = 0 # Vil ha mynt
    venn2 = 0 # Vil ha kron
    
    while not ferdig:
        for mnd in range(1,13):
            stilling = ""
            result = random.randint(0,1)
            if result == 0:
                venn1 += 1
                verdi = "Mynt"
            else:
                venn2 += 1
                verdi = "Kron"
            
            if mnd == 12:
                if venn1 > venn2:
                    stilling = "Venn1 vant!"
                elif venn1 < venn2:
                    stilling = "Venn2 vant!"
                else:
                    stilling = "Uavgjort!"
                ferdig = True
            elif venn1 > venn2:
                stilling = "Venn1 leder!"
            elif venn1 == venn2:
                stilling = "Det er likt!"
            else:
                stilling = "Venn2 leder!"
            skrivefil.write("%d;%s;%d;%d;%s \n" % (mnd,verdi,venn1,venn2,stilling))
    skrivefil.close()
        

def main():
    """ Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt.
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet
    foran oppgave-funksjonen slik at den blir "skrudd på".
    Før du leverer kan det være lurt å sjekke alle funksjonene. Dette gjør
    du ved å fjerne alle #-tegnene nedenfor.
    """
    # oppgave1()
    # print()
    # oppgave2()
    # print()
    oppgave3("myntkast-eksperiment.csv", True)


main()
