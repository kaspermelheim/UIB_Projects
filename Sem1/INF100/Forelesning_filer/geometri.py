#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funksjonar for geometriske utrekningar
@author: nmidd
"""

from math import pi

def sirkel(radius):
    """
    Returnerer arealet og omkrinsen av ein sirkel som eit tuppel
    """
    areal = pi * radius * radius
    omkrins = 2 * pi * radius
    return (areal, omkrins)


def main():

    r = 7.3

    (areal, omkrins) = sirkel(r)

    print('Ein sirkel med radius %.1f har areal %.1f og omkrins %.1f' %
          (r, areal, omkrins))
main()