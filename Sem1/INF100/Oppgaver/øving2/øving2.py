# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:05:29 2019

@author: Kasper
"""

print('\n --- 1: Aritmetikk ---')

#1.a
print("Oppgave 1.a")

print(9 - 3) #6 - heiltal
print(8 * 2.5) #20.0 - flyttal
print(9 / 2) #4.5 - flyttal
print(9 / -2) #-4.5 - flyttal
print(9 // -2) #-5 - heiltal
print(9 % 2) #1 - heiltal
print(9.0 % 2) #1.0 - flyttal
print(9 % 2.0) #1.0 - flyttal
print(9 % -2) #-1 - heiltal
print(-9 % 2) #1 - heiltal
print(9 / -2.0) #-4.5 - flyttal
print(4 + 3 * 5) #19 - heiltal
print((4 + 3) * 5) #35 - heiltal
print(abs(5 - 10)) #5 - heiltal

#1.b
print("Oppgave 1.b")

print(3 ** 6)
print(4 * 2 - 3)
print((4 + 2) * 3)
print(100 // 6)
print(100 % 6)
print(100.0 / 6.0)

#1.c
print("Oppgave 1.c")

print(500 % 8)
print(500 // 8)

print(500 % 365)
print(1000000 % 365)
print(1000000 // 365)

print(30 % 24)
print(300 % 24)
print(300 // 24)

print('\n --- 2: Strenger ---')

#2.a
print("Oppgave 2.a")

print("Denne\n strengen\n har\n mange\n linjeskift.")

#2.b
print("Oppgave 2.b")

print("\"He said, ’Absolutely not,’\", recalled Mel.")

#2.c
print("Oppgave 2.c")

setning1 = "Dette er den første teksten, "
setning2 = "dette er den andre."
print(len(setning1))
print(len(setning2))
setning = setning1 + setning2
print(setning)

print('\n --- 3: Innlesing ---')
#3.a
print("Oppgave 3.a")

fornavn = input("Hva er fornavnet ditt?")
etternavn = input("Hva er etternavnet ditt?")
navn = fornavn + " " + etternavn
print("Ditt navn er" , navn,".")
print("Lengde på navn:" ,len(navn))

#3.b
print("Oppgave 3.b")

x = float(input("Skriv inn det første flyttalet: "))
y = float(input("Skriv inn det andre flyttalet: "))

print("Summen er: ",x+y)