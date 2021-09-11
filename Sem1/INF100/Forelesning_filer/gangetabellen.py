#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skriv ut gangetabellen.
@author: nmidd
"""

for i in range(1, 11):
    linje = ''
    for j in range(1, 11):
        produkt = i*j
        streng = '%4d' % produkt
        linje += streng
    print(linje)
