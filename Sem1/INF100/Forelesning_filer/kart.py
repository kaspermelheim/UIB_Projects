#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skriv ut kart med fargekode for høgde over havet
@author: nmidd
"""

from random import randint
from colorama import Fore, Back, Style

def finn_høgder(n_sør, n_aust):
    """
    Genererer og returnerer matrise med n_sør*n_aust
    tilfeldige høgder i intervallet [0, 500]
    """
    høgder = [None] * n_sør
    for sør in range(n_sør):
        høgder[sør] = [None] * n_aust
        for aust in range(n_aust):
            høgder[sør][aust] = randint(0, 500)
    return høgder

def teikn(høgde, fargar, grenser):
    """
    Skriv ut ein pixel med farge som funksjon av høgd
    """
    farge = fargar[0]
    for i in range(len(grenser)):
        if høgde >= grenser[i]:
            farge = fargar[i+1]
    print(farge, end="")

def teikn_kart(høgder, fargar, grenser):
    """
    Teiknar kart med farge som funksjon av høgd
    """
    for sør in range(len(høgder)):
        for aust in range(len(høgder[sør])):
            teikn(høgder[sør][aust], fargar, grenser)
        print()

def main():
    """
    Genererer og skriv ut kartet.
    """
    pixel = chr(9608)
    print(Style.BRIGHT)
    blå = Fore.BLUE + pixel
    raud = Fore.RED + pixel
    grøn = Fore.GREEN + pixel
    gul = Fore.YELLOW + pixel
    
    fargar = [blå, grøn, gul, raud]
    grenser = [1, 200, 400]
    høgder = finn_høgder(20, 50)
    teikn_kart(høgder, fargar, grenser)
    print(Style.RESET_ALL)

main()