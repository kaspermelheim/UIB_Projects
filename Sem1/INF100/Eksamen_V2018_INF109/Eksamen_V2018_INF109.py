# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:47:38 2019

@author: Kasper
"""

# Oppgåve 1

def nyPris(gammelPris, nedProsent):
    return int(gammelPris * (1 - (nedProsent/100)))

def test(verdi, prosent):
    minPris = verdi
    minPris = nyPris(minPris, prosent)
    print(minPris)
    
# Oppgåve 2
# a)
    
def lagbruker(namn):
    fornamn = namn[:3].lower()
    for i in range(len(namn)):
        if namn[i] == " ":
            etternamn = (namn[i+1] + namn[i+2] + namn[i+3]).lower()
    brukernamn = fornamn + "." + etternamn
    return brukernamn

def les_bruker_til_fil(navnfil, brukerfil):
    
    with open(navnfil, "r") as lesefil:
        navnliste = lesefil.readlines()
    
    brukerliste = []
    for i in navnliste:
        brukerliste.append(lagbruker(i))
    
    with open(brukerfil, "w") as skrivefil:
        
        counts = dict()
        for i in brukerliste:
            counts[i] = counts.get(i, 0) + 1
            skrivefil.write(i + str(counts[i]) + "\n")
            
def oppgave3():
    
    slutt = False
    
    while not slutt:
        
        print("A) Finn spiller \nB) Legg inn spiller \nC) Avslutt")
        valg = input("Tast inn ditt valg: ")
        
        if valg == "B":
            with open("spelarar.txt", "a") as skrivefil:
                etternamn = input("Skriv etternamn: ")
                fornamn = input("Skriv fornamn: ")
                klubb = input("Skriv klubb: ")
                pos = input("Skriv posisjon: ")
                skrivefil.write(etternamn + " " + fornamn + " " + klubb + " " + pos + "\n")
        elif valg == "A":
            with open("spelarar.txt", "r") as lesefil:
                etternamn = input("Skriv etternamn på spilleren: ")
                for line in lesefil:
                    for part in line.split():
                        if etternamn in part:
                            printlist = line.split()
                            print(printlist[1] + " " + printlist[0] + " spiller " + printlist[3] + " for " + printlist[2])
        elif valg == "C":
            slutt = True
        else:
            print("Du har tastet inn en ugyldig bokstav.")
            
def isGeometric(liste):
    n = len(liste)
    k = liste[1] / liste[0]
    funn = 0
    for i in range(n-1):
        if (liste[i] * k) == liste[i+1]:
            funn += 0
        else:
            funn += 1
    if funn > 0:
        print("Lista er ikke geometrisk.")
    else:
        print("Lista er geometrisk.")
        
def longestStart(liste, s, k):
    nyliste = []
    for i in range(len(liste)):
        if liste[i] == s:
            start = i
            break
    nyliste.append(liste[i])
    start = i
    for n in range(start, len(liste)):
        if liste[n] == (2*liste[start]):
            nyliste.append(liste[n])
            start += (n - start)
    return nyliste
        
        
    
def main():
    
   test(1000,5)
   test(100, 25)
   
   print(lagbruker("Kasper Melheim"))
   
   les_bruker_til_fil("navn.txt", "bruker.txt")
   oppgave3()
   
   isGeometric([4,8,16,32])
   isGeometric([2,4,6,8])
   
   print(longestStart([1,2,3,4,5,6,7,8], 2, 3))
   print(longestStart([64, 2, 4, 2, 8, 33, 16, 3, 4, 32, 128], 4, 2))


   
main()