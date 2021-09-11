# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:14:06 2019
Skriv ut om eit innlest namn er langt,
passeleg langt eller kort.
@author: Kasper
"""

styrke = float(input("Gi vindstyrke (km/h): "))

if styrke > 117.0:
    print("Orkan.")
elif styrke > 76.0:
    print("Storm.")
elif styrke > 40.0:
    print("Kuling.")
elif styrke > 12.0:
    print("Bris.")
elif styrke >= 0.0:
    print("Lite vind.")
else:
    print("Feil. Negativ verdi.")
        