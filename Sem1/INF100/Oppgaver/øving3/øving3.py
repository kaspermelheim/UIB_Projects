# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:20:25 2019

@author: Kasper
"""

#1.a 
#Finn ut om bruker er myding eller ikkje myndig

alder = int(input("Hvor gammel er du: "))
if alder >= 18:
    print("Du er myndig.")
else:
    print("Du er ikkje myndig.")
    
#1.b

x = float(input("Skriv inn eit flyttal: "))
if x > 0:
    print("%.1f er eit positivt flyttal. " % x )
elif x < 0:
    print("%.1f er eit negativt flyttal. " % x )
else:
    print("%.1f er 0." % x )
    
#1.c

flyttall = float(input("Skriv inn eit flyttall: "))
print(flyttall >= 0)
    
#2.a
    
flyttall1 = float(input("Skriv inn flyttall nr. 1: "))
flyttall2 = float(input("Skriv inn flyttall nr. 2: "))
print(flyttall1 > 10 and flyttall2 > 10)

#2.b

lys_lux = float(input("Skriv inn lystyrke i lux: "))
temp_celsius = float(input("Skriv inn temp. i celsius: "))

if lys_lux < 0.01 and temp_celsius > 0:
    print("Kamera av.")
elif lys_lux < 0.01:
    print("Kamera på.")
elif temp_celsius > 0:
    print("Kamera på.")
    
#2.c
    
alder1 = int(input("Hva er alderen din? "))
alder2 = int(input("Hva er alderen til vennen din? "))
if alder1 >= 18 and alder2 >= 18:
    print("Både du og vennen din er myndige.")
elif alder1 >= 18 and alder2 < 18:
    print("Du er myndig men din venn er ikkje myndig.")
elif alder1 < 18 and alder2 >= 18:
    print("Du er ikkje myndig men din venn er myndig.")
else:
    print("Ingen av dere er myndige.")     
    
#3.a

for i1 in range (0,10):
    print(i1)
    
#3.b

for i2 in range (5,13):
    print(i2)

#3.c

for i3 in range (2,11,2):
    print(i3)

#3.d

for i4 in range(3,-1,-1):
    print(i4)
    if i4 == 1:
        print("Klare!")
    elif i4 == 0:
        print("Start!")
#4. a,b,c,d
    
max_customers = 3
daglig_inntekt = 0
antall_sales = 0
antall_nosales = 0

for i in range(max_customers):
    wallet = float(input("Hvor mye penger har kunden? "))
    item = input("Hvilken vare vil kunden ha? ")
    cost = float(input("Hvor mye koster varen? "))
    if wallet >= cost:
        print("Kunde nr:",(i+1),"kjøpte",item,"for",cost,"NOK.")
        daglig_inntekt += cost
        antall_sales += 1
    elif wallet < cost:
        print("Kunde nr:",(i+1),"hadde ikke råd til å kjøpe noe.")
        antall_nosales += 1
print("Butikken hadde daglig inntekt på",daglig_inntekt,"NOK.")
print("Butikken hadde totalt",(antall_sales + antall_nosales),
      "kunder i dag der",antall_sales,"kjøpte en vare, og",antall_nosales,"gikk tomhendt hjem.")

if daglig_inntekt >= 100:
    print("Vi har tjent nok i dag til å ikke gå konk.")
else:
    print("Vi har tjent for lite i dag og vil nå gå konk.")