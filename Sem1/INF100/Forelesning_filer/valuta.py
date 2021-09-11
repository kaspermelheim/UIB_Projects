#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for valutaomrekning
@author: nmidd
"""

valuta = {'EUR': 9.68551, 'USD': 8.50373, 'GBP': 11.0134,
          'SEK': 0.92950, 'AUD': 6.06501}

def tilNOK(beløp, frå):
    """
    Returnerer oppgitt beløp i NOK omforma frå oppgitt valuta
    """
    """
    if frå in valuta:
        return beløp * valuta[frå]
    else:
        return beløp """
    # Alternativ
    return beløp * valuta.get(frå, 1.0)

    
def fråNOK(beløp, til):
    """
    Returnerer oppgitt beløp i oppgitt valuta omforma frå NOK
    """
    return beløp / valuta.get(til, 1.0)


def main():
    print('50 EUR = %.2f NOK' % tilNOK(50, 'EUR'))
    print('50 NOK = %.2f EUR' % fråNOK(50, 'EUR'))
    
main()