#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer operasjonar på mengder
@author: nmidd
"""

menn5000m = {'Etiopia', 'Belgia', 'Canada',
             'Australia', 'Etiopia', 'USA'}
kvinner5000m = {'Kenya', 'USA', 'USA',
                'Etiopia', 'Tyskland'}
minst_ein = menn5000m.union(kvinner5000m)
begge = menn5000m.intersection(kvinner5000m)
første_ikkje_andre = menn5000m.difference(kvinner5000m)
nøyaktig_ein = menn5000m.symmetric_difference(kvinner5000m)
print(nøyaktig_ein)