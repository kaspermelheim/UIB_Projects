# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:14:06 2019
@author: Kasper
"""
passord = input("Passord: ")
lengd = len(passord)
if lengd < 10:
    print("Passordet må ha minst 10 karakterar.")
else: 
    små = 0
    store = 0
    siffer = 0
    andre = 0
    for karakter in passord:
        if karakter.islower():
            små += 1
        elif karakter.isupper():
            store += 1
        elif karakter.isdigit():
            siffer += 1
        else:
            andre += 1
    if små >= 3 and store >= 2 and siffer >= 1 and andre >=2:
        print("Passord OK.")
    else:
        print("Ugyldig passord.")