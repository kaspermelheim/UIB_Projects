# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:36:15 2019

@author: Kasper
"""

from math import sqrt

s1 = 6
sTot = 10
h = 3
v1 = 5
v2 = 2

katet = sTot - s1
s2 = sqrt(h*h + katet*katet)
t1 = s1/v1
t2 = s2/v2
totalTid = t1 + t2

print("Roboten treng", totalTid,
      "sekund på å nå målet.")