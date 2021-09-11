# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:54:44 2019

@author: Kasper
"""
""" def kart1(spiller_x, spiller_y, monster_x, monster_y):
    linje = ""
    for y in range(0,11):
        for x in range(0,11):
            if y == spiller_y and x == spiller_x:
                linje += "😃"
            elif y == monster_y and x == monster_x:
                linje += "👺"
            else:
                linje += " • "
        print(linje)
        linje=""
kart1(2,2,10,10) 

kart = []
def print_kart():
    for rad in range(0,10):
        kart.append([])
        for kolonne in range(0,10):
            kart[rad].append("•")
        print(" ".join(kart[rad]))
        
    for n in range(len(kart)):
        print(kart[rad]) """

def oppdater_kart(spillerX, spillerY, monsterX, monsterY):
    ''' Printer et 10 * 10 kart med spiller i posisjon (spillerX, spillerY)
    og monster i posisjon (monsterX, monsterY)
    input:
        spillerX og spillerY, heltall mellom 0 og 9
    return:
        None
    '''
    kart = []
    for rad in range(0,10):
        kart.append([])
        for kolonne in range(0,10):
            if rad == spillerY and kolonne == spillerX:
                kart[rad].append("😃")
            elif rad == monsterY and kolonne == monsterX:
                kart[rad].append("👺")
            else:
                kart[rad].append(" • ")
        print(" ".join(kart[rad]))
        
    for n in range(len(kart)):
        print(kart[n])
    
oppdater_kart(1,2,7,9)