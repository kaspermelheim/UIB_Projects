# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

streng = input("Streng: ")
første = -1
for i in range(len(streng)-2):
    delstreng = streng[i:i+3]
    if delstreng.isdigit() and første == -1:
        første = i
if første == -1:
    print("Strengen", streng,"har ikkje tre etterfølgjande siffer.")
else:
    print("Første forekomst av tre etterfølgjande siffer i strengen ",streng, "er", streng[første:første+3])