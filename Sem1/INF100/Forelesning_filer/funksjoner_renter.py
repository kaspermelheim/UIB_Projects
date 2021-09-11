# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:57:11 2019

@author: Kasper
"""

from math import log, ceil

def verdi(rente, tid):
    """
    Returnerer verdi av ei krone ved sparing 
    med oppgitt rente i oppgitt antal år.
    """
    return (1+rente/100.0)**tid

def rente(verdi,tid):
    """
    Returnerer renta vi må ha for å få oppgit 
    verdi av ei krone ved sparing i oppgitt antal år.
    """
    return (verdi**(1/tid)-1)*100.0

def tid(verdi, rente):
    """
    Returnerer antal heile år vi må spara for å oppnå
    oppgitt verdi av ei krone ved sparing til oppgitt rente.
    """
    tid_flyt = log(verdi) / log(1 + rente/100.0)
    return ceil(tid_flyt)    
    