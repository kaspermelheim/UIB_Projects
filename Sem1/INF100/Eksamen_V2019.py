# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:58:47 2019

@author: Kasper
"""

# Oppgåve 1
# a)
a = 1
print(a)
a = 3
# Output: 1

# b)
x = 0
def f(x=1):
    print(x)   
f(2)
# Output: 2

# c)
def f(x):
    return x+1

a = 1
print(a + f(a))
# Output: 3

# d)
def f(x):
    y = x // 3
    a = x % 3
    b = a % 2
    return y + b
print(f(9) + f(10))
# Output: 7

# e
def f(x, y=1):
    return x - y

x = 9
y = 4
print(f(y))
# Output: 3

# Oppgåve 2
# a)
def vurdering(x):
    if x <= 1:
        print("nei")
    if x <= 3:
        print("tvilsamt")
    if x <= 5:
        print("kanskje")
    if x <= 7:
        print("truleg")
    else:
        print("ja")
        
vurdering(3)

# b)
def vurdering(x):
    if x <= 1:
        print("nei")
    elif x <= 3:
        print("tvilsamt")
    elif x <= 5:
        print("kanskje")
    elif  x <= 7:
        print("truleg")
    else:
        print("ja")
vurdering(3)
# Output 

# c)
liste1 = [5, 2, 6, 9]
liste2 = []
for i in range(len(liste1)):
    verdi = liste1[i]
    if i > 0:
        verdi = i + liste1[i]/i
    liste2.append(verdi)
print(liste2)

#d
pos = ord('a')
streng = ''
while len(streng) < 3:
    streng += chr(pos)
    pos += 2
print(streng)

#Oppgåve 3
#a
def snittMedSmå(mengd):
    return mengd.intersection(range(10))
print(snittMedSmå({12, 0, 9, 10}))

#b
def f(x):
    x = x[:-1]
    x += 'sann!'
    print(x)
hallo = 'hei!'
f(hallo)
print(hallo)

#c
def f(hallo):
    for x in hallo:
        print(x[:-1] + 'sann!')
        hallo.clear() # Fjern alle element
        hallo.add('heisann!')
hallo = {'hei!'}
f(hallo)
for x in hallo:
    print(x)
# d  
x = [1, 2, 3]
y = [x, x, x]
x[1] += 1
y[2] = [4, 4, 4]
x[2] = 0
produkt = 1
for i in range(len(y)):
    produkt *= y[i][i]
print(produkt)

# Oppgåve 4

def er_nær(a, b):
    return (a/2 >= b) or (b/2 >= a)
     
print(er_nær(3, 4))
print(er_nær(5, 2))

# 4b
def nærliste(liste):
    nyliste = []
    for i in liste:
        if (er_nær(i, liste[0]) == True) and (er_nær(i, liste[-1]) == True):
            nyliste.append(i)
    print(nyliste)
nærliste([3, 7, 5])
nærliste([4, 5, 6, 7, 8])
nærliste([7])

#4c

def faktor(a, b):
    for i in range(1,10):
        if a % i == 0 and b % i == 0:
            print(i)
            
faktor(12, 18)
faktor(49, 21)
faktor(4, 12)
faktor(8, 13)

# Oppgåve 5a
lag = ["Brann", "Molde", "Rosenborg", "Viking"]
mål = [[0, 3, 2, 2], [1, 0, 2, 4], [1, 0, 0, 1], [0, 3, 2, 0]]

def resultat(lag, mål):
    n = len(lag)
    for i in range(n):
        for j in range(i+1, n):
            print("%s - %s %d - %d" % (lag[i], lag[j], mål[i][j], mål[j][i]))
resultat(lag, mål)

def målskilnad(lag, mål):
    n = len(lag)
    system = {}
    for i in range(n):
        summen = 0
        for j in range(n):
            summen += (mål[i][j] - mål[j][i])
        system[lag[i]] = summen
    return system
print(målskilnad(lag, mål))

