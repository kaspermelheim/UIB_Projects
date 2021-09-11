# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

streng = input("Streng: ")
siffer = int(input("Lengda sifferstrengen skal ha: "))

funn = False
i = 0

while (funn == False) and i+siffer <= len(streng):
    delstreng = streng[i:i+siffer]
    if delstreng.isdigit():
        funn = True
    else:
        i += 1
if funn: 
    print("Første forekomst av %d etterfølgjande siffer i %s er %s." % (siffer, streng, delstreng))
else:
    print("Strengen %s har ikkje %d etterfølgjande siffer." (streng, siffer))
        