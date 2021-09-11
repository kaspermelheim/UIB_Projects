# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:22:31 2019

@author: Kasper
"""

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
print("Butikken hadde totalt",(antall_sales + antall_nosales),"kunder i dag der",antall_sales,"kjøpte en vare, og",antall_nosales,"gikk tomhendt hjem.")

if daglig_inntekt >= 100:
    print("Vi har tjent nok i dag til å ikke gå konk.")
else:
    print("Vi har tjent for lite i dag og vil nå gå konk.")