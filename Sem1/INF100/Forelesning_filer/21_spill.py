# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

from random import randint
from matplotlib import pyplot

spelar = input("Namn på spelar: ")
farge = input("%s sin farge (engelsk): " % spelar)
beste_spelar = " "
størst = -1

while len(spelar)>0:
    poeng = 0
    slutt_spill = False
    
    while not slutt_spill:
        svar = input("%s har %d poeng. Fleire kort (j/n)? " % (spelar, poeng))
        if svar[0].lower() == "j":
            kort = randint(1,13)
            print("%s trakk kort %d. " % (spelar,kort))
            poeng += kort
            if poeng > 21:
                poeng = 0
                slutt_spill = True
        else:
            slutt_spill = True
    print("%s fekk %d poeng." % (spelar, poeng))
    pyplot.bar(spelar, poeng)
    if poeng > størst:
        beste_spelar = spelar
        størst = poeng
    spelar = input("Namn på neste spelar: ")
    if len(spelar)>0:
        farge = input("%s sin farge (engelsk): " % spelar)
print("Beste spelar var %s med %d poeng." % (beste_spelar, størst))
pyplot.show()
    
    