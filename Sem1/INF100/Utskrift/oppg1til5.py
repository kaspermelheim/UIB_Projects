#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oppgåve 1-5, eksamen INF100, våren 2019
@author: nmidd
"""

def oppg1a():
    a = 1
    print(a)
    a = 3

def oppg1b():
    x = 0
    def f(x=1):
        print(x)
    f(2)

def oppg1c():
    def f(x):
        return x+1
    a = 1
    print(a + f(a))

def oppg1d():
    def f(x):
        y = x // 3
        a = x % 3
        b = a % 2
        return y + b
    print(f(9) + f(10))

def oppg1e():
    def f(x, y=1):
        return x - y
    x = 9
    y = 4
    print(f(y))

def oppg2a():
    def vurdering(x):
        if x <= 1:
            print('nei')
        if x <= 3:
            print('tvilsamt')
        if x <= 5:
            print('kanskje')
        if x <= 7:
            print('truleg')
        else:
            print('ja')
    vurdering(3)


def oppg2b():
    def vurdering(x):
        if x <= 1:
            print('nei')
        elif x <= 3:
            print('tvilsamt')
        elif x <= 5:
            print('kanskje')
        elif x <= 7:
            print('truleg')
        else:
            print('ja')
    vurdering(3)

def oppg2c():
    liste1 = [5, 2, 6, 9]
    liste2 = []
    for i in range(len(liste1)):
        verdi = liste1[i]
        if i > 0:
            verdi = i + liste1[i]/i
        liste2.append(verdi)
    print(liste2)


def oppg2d():
    pos = ord('a')
    streng = ''
    while len(streng) < 3:
        streng += chr(pos)
        pos += 2
    print(streng)


def oppg3a():
    def snittMedSmå(mengd):
        return mengd.intersection(range(10))
    print(snittMedSmå({12, 0, 9, 10}))


def oppg3b():
    def f(x):
        x = x[:-1]
        x += 'sann!'
        print(x)
    hallo = 'hei!'
    f(hallo)
    print(hallo)

def oppg3c():
    def f(hallo):
        for x in hallo:
            print(x[:-1] + 'sann!')
        hallo.clear()  # Fjern alle element
        hallo.add('heisann!')
    hallo = {'hei!'}
    f(hallo)
    for x in hallo:
        print(x)

def oppg3d():
    x = [1, 2, 3]
    y = [x, x, x]
    x[1] += 1
    y[2] = [4, 4, 4]
    x[2] = 0
    produkt = 1
    for i in range(len(y)):
        produkt *= y[i][i]
    print(produkt)

def er_nær(a, b):
    """
    Oppgåve 4a
    Returnerer True dersom a og b er nær kvarandre i
    følge definisjonen i oppgåveteksten, False elles
    """
    return max(a, b) < 2*min(a,b)

def nærliste(liste):
    """
    Oppgåve 4b
    Returnerer ei liste over element i oppgitt liste som
    er nær både første og siste element i oppgitt liste.
    """
    nyliste = []
    for verdi in liste:
        if er_nær(verdi, liste[0]) and er_nær(verdi, liste[-1]):
            nyliste.append(verdi)
    return nyliste
    

def faktor(a, b):
    """
    Oppgåve 4c
    Skriv ut alle tal som både a og b er delelege med.
    """
    print("Felles faktorar for %d og %d" % (a,b))
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            print(i)
            

def resultat(lag, mål):
    """
    Oppgåve 5a
    Skriv ut resultata i alle kampane mellom lag i lista
    lag gitt måla i den todimensjonale lista mål.
    """
    n = len(lag)
    for i in range(n):
        for j in range(i+1, n):
            print("%s - %s %d - %d" % (lag[i], lag[j], mål[i][j], mål[j][i]))

def målskilnad(lag, mål):
    """
    Oppgåve 5b
    Returnerer oppslagstabell med målskilnaden til kvart
    lag i lista lag gitt måla i den todimensjonale lista
    mål.
    """
    n = len(lag)
    svar = {}
    for i in range(n):
        skilnad = 0
        for j in range(n):
            if i != j:
                skilnad += (mål[i][j] - mål[j][i])
        svar[lag[i]] = skilnad
    return svar
def main():
    print(er_nær(3, 4))
    print(er_nær(5, 2))
    print(nærliste([3, 7, 5]))
    print(nærliste([4, 5, 6, 7, 8]))
    print(nærliste([7]))
    faktor(12, 18)
    faktor(49, 21)
    faktor(4, 12)
    faktor(8, 13)
    elitedivisjonen = ['Brann', 'Molde', 'Rosenborg', 'Viking']
    scoringar = \
               [ [0, 3, 2, 2],
               [1, 0, 2, 4],
               [1, 0, 0, 1],
               [0, 3, 2, 0] ]
    resultat(elitedivisjonen, scoringar)
    print(målskilnad(elitedivisjonen, scoringar))    

main()