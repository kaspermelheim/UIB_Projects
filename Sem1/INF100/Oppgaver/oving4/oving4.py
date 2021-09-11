#!/usr/bin/env python
# Kasper Melheim
# -*- coding: utf-8 -*-


def oppgave1():
    """ Setter x og y verdi til monster og spiller i egne variabler. Bruker
    for løkker og if løkker til å skrive ut eit 10x10 spel bygd opp av dots,
    og når løkka går over samme x og y pos til monster og spiller, skal ein av
    bli putta inn på den xy pos i spillet. Resetter linja etter kvar y verdi
    for å få kvar linje med dots på ein egen linje i konsollen.
    """
    spiller_x = 3
    spiller_y = 4
    monster_x = 7
    monster_y = 5

    linje = ""
    for y in range(0,11):
        for x in range(0,11):
            if y == spiller_y and x == spiller_x:
                linje += "😃"
            elif y == monster_y and x == monster_x:
                linje += "👺"
            else:
                linje += " • "
        print(linje)
        linje=""
            

def oppgave2():
    """
    Liste av 10 første primtall, skal printe ut nr. 9
    """
    primtall = [2,3,5,7,11,13,17,19,23,29,31]
    print(primtall[9])

""" Lista vi skal bruke. """
størsteLand = [
    'Russland',
    'Canada',
    'USA',
    'Kina',
    'Brasil',
    'Australia',
    'EU',
    'India',
    'Argentina',
    'Kasakhstan',
]


def oppgave3a():
    """
    Skriver ut ulike verdier fra lista størsteLand.
    """
    print(størsteLand[0])
    print(størsteLand[2])
    print(størsteLand[9])
    print(størsteLand[:3])
    print(størsteLand[1:5])
    print(størsteLand[3:])
    list.reverse(størsteLand)
    print(størsteLand)

def oppgave3b(): 
    størst_tal = 0    # Setter det lengste talet til 0 (verdien før vi sjekker)
    for i in størsteLand: # Går gjennom alle verdiane i lista
        if len(i) > størst_tal: # Sjekker om landet pos i er lengre enn
                                # verdien til størst_tal.
            størst_tal = len(i) # Setter lengda til landet lik størst_tal.
            land = i
    print("Landet",land,"har flest karakterar med",størst_tal,"stk.")

def flyttLitenBokstav(c, steg):
    """ 
    char_index finner indexen til den nye posisjonen til "c" i alfabetet.
    Koneverterer indexen tilbake til bokstaven den hører til. 

    >>> flyttLitenBokstav('a', 5)
    'f'
    >>> flyttLitenBokstav('z', 1)
    'a'
    >>> flyttLitenBokstav('a', -1)
    'z'
    >>> flyttLitenBokstav('x', 100)
    't'
    """
    char_index = (((ord(c) - ord("a")) + steg) % 26) + ord("a")
    char = chr(char_index)
    return char
    


def oppgave4a():
    """
    Tester funksjonen flyttLitenBokstav(c, steg)
    """
    print(flyttLitenBokstav('a', 5))
    print(flyttLitenBokstav('z', 1))
    print(flyttLitenBokstav('a', -1))
    print(flyttLitenBokstav('x', 100))


def flyttStorBokstav(c, steg):
    """
    char_index finner indexen til den nye posisjonen til "c" i alfabetet.
    Koneverterer indexen tilbake til bokstaven den hører til. 
    """
    char_index = (((ord(c) - ord("A")) + steg) % 26) + ord("A")
    char = chr(char_index)
    return char


def oppgave4b():
    """
    Tester funksjonen flyttStorBokstav(c, steg)
    """
    print(flyttStorBokstav('A', 5))
    print(flyttStorBokstav('Z', 5))
    print(flyttStorBokstav('A', -1))
    print(flyttStorBokstav('X', 100))


def flyttKarakter(c, steg):
    """ 
    Bruker if løkke til å sjekke om input er ein stor eller liten bokstav,
    eller om det er eit spesialtegn. Bruker så funksjonane laga i tidlegare
    oppgave til å flytte bokstaven. 
    """
    if c.isupper():
        return flyttStorBokstav(c, steg)
    elif c.islower():
        return flyttLitenBokstav(c, steg)
    else:
        return c

def oppgave4c():
    """
    Tester funksjonen flyttKarakter(c, steg)
    """
    print(flyttKarakter('a', 5))
    print(flyttKarakter('z', 5))
    print(flyttKarakter('A', 5))
    print(flyttKarakter('Z', 5))
    print(flyttKarakter('.', 5))


def cæsarChiffer(tekst, steg):
    """
    Krypterer strengen tekst med cæsarChiffer. Bokstavene flyttes steg antall 
    steg i alfabetet. Sjekker her alle pos i teksten med for løkke,
    sjekker så om i er uppercase, lowercase eller spesialtegn. Legger til
    resultatet til tekst_new og returnerer resultat.

    >>> cæsarChiffer('abc', 5)
    'fgh'
    >>> cæsarChiffer('Dette er en test', 7)
    'Klaal ly lu alza'
    >>> cæsarChiffer('Dette er en test', -7)
    'Wxmmx xk xg mxlm'
    """
    tekst_new = ""
    for i in tekst:
        if i.islower():
            char_index = (((ord(i) - ord("a")) + steg) % 26) + ord("a")
            char = chr(char_index)
            tekst_new += char
        elif i.isupper():
            char_index = (((ord(i) - ord("A")) + steg) % 26) + ord("A")
            char = chr(char_index)
            tekst_new += char
        else: 
            tekst_new += " "
    return tekst_new
        


def oppgave4d():
    """
    Tester funksjonen cæsarChiffer(tekst, steg)
    """
    print(cæsarChiffer('abc', 5))
    print(cæsarChiffer('Dette er en test', 7))
    print(cæsarChiffer('Dette er en test', -7))


def main():
    """ Alle oppgaver, kommenter ut her hvis du 
        bare vil kjøre en oppgave

"""
    oppgave1()
    print()
    
    oppgave2()
    print()

    
    oppgave3a()
    print()
    
    oppgave3b()
    print()
    
    oppgave4a()
    print()
    
    oppgave4b()
    print()
    
    oppgave4c()
    print()
    
    oppgave4d()

main() 
