# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:07:54 2019

@author: Kasper
"""
#Oppgåve 4a
def er_nær(a, b):
    #return max(a, b) < 2*min(a,b)
    return b/2 < a < 2*b

#Oppgåve 4b

def nærliste(liste):
    nyliste = []
    for i in liste:
        if er_nær(i,liste[0]) and er_nær(i, liste[-1]):
            nyliste.append(i)
    return nyliste

#Oppgåve 5
lag = ["Brann", "Molde", "Rosenborg", "Viking"]
mål = [[0, 3, 2, 2], [1, 0, 2, 4], [1, 0, 0, 1], [0, 3, 2, 0]]

def resultat(lag, mål):
    n = len(lag)
    for i in range(n):
        for j in range(i+1, n):
            print("%s - %s %d - %d" % (lag[i], lag[j], mål[i][j], mål[j][i]))

#5b
def målskilnad(lag, mål):
    skilnad = {}
    n = len(lag)
    for i in range(n):
        summen = 0
        for j in range(n):
            summen += mål[i][j] - mål[j][i]
        skilnad[lag[i]] = summen
    return skilnad

#Oppgåve 6a

rapportar = []
status = {}

def registrer(typen, laborant, vellukka):
    rapportar.append((typen, laborant, vellukka))
    status[typen] = status.get(typen, [0,0])
    if vellukka:
        status[typen][1] += 1
    else:
        status[typen][0] += 1
        
    return rapportar, status

#6b
def godkjent(typen):
    tot = sum(status.get(typen, [0,0]))
    return tot >= 10 and status[typen][1] >= 0.9 * tot

def oversikt():
    oversikt = {}
    typen = status.keys()
    for i in typen:
        oversikt[i] = godkjent(i)
    return oversikt

def konkluder(godkjente, underkjente):
    navn = status.keys()
    
    with open(godkjente, "w") as skrivefil:
        skrivefil.write("Godkjente instrument: \n")
        for typen in navn:
            if godkjent(typen):
                skrivefil.write(typen + "\n")
    
    with open(underkjente, "w") as skrivefil:
        skrivefil.write("Underkjente instrument: \n")
        for typen in navn:
            if not godkjent(typen):
                skrivefil.write(typen + "\n")
                
def plukk(laborant):
    laboranter = []
    for tuppel in rapportar:
        if laborant in tuppel:
            laboranter.append(tuppel)
    return laboranter

def slett(laborant):
    sletting = plukk(laborant)
    for rapport in sletting:
        rapportar.remove(rapport)
        typen = rapport[0]
        vellukka = rapport[2]
        status[typen][int(vellukka)] -= 1
    return len(sletting)

def verifiser(godkjente, underkjente):
    
    with open(godkjente, "r") as lesefil:
        lesefil.readline()
        godliste = lesefil.readlines()
    with open(underkjente, "r") as lesefil:
        lesefil.readline()
        underliste = lesefil.readlines()
    
    ok = True
    
    for i in underliste:
        typen = i.strip()
        if typen in status:
            if godkjent(typen):
                print("Godkjent instrument i txt fil for underkjente.")
                ok = False
        else:
            print("Ukjent instrument i txt fil for underkjente.")
            ok = False
    for i in godliste:
        typen = i.strip()
        if typen in status:
            if not godkjent(typen):
                print("Underkjent instrument i txt fil for godkjente.")
                ok = False
        else:
            print("Ukjent instrument i txt fil for godkjente.")
            ok = False
    return ok
                
def main():
    #4a
    """
    print(er_nær(3,4))
    print(er_nær(2,6))
    
    #4b
    print(nærliste([3,7,5]))
    print(nærliste([4,5,6,7,8]))
    print(nærliste([7]))
    
    #5a
    resultat(lag, mål)
    
    #5b
    print(målskilnad(lag, mål)) """
    
    #6
    registrer("nano1", "Martha", True)
    registrer("bio-x", "Martha", True)
    registrer("nano1", "Dag", False)
    print(rapportar)
    print(status)

    print(godkjent("nano1"))
    print(oversikt())
    
    konkluder("godkjente.txt", "underkjente.txt")
    
    print(plukk("Dag"))
    
    print(slett("Dag"))
    print(status)
    print(rapportar)
    
    print(verifiser("godkjente.txt", "underkjente.txt"))
    
    
main()
