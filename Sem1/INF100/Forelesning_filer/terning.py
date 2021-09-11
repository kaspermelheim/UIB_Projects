# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""
from random import randint

sum = 0
    
for i in range(0,3):
    terning = randint(1,6)
    print(terning)
    sum += terning
    if sum == 18:
        print("YATZY!")
    