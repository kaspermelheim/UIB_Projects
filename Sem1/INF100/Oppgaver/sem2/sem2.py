#!/usr/bin/env python
# Kasper Melheim
# -*- coding: utf-8 -*-

"""
Importerer alle innebygde filer vi trenger for å løse oppgavene.
"""
import matplotlib.pyplot as plt
import random
from copy import deepcopy


def oppgave1():
    """ 
    Henter alle verdiene i lista 'store_tall' med for løkke og printer de ut
    oversiktlig og i like posisjoner under tittelene 'navn', 'lang' og 'kort'.
    """
    store_tall = [
        ["Million",    "10^6 ", "10^6 "],
        ["Milliard",   "     ", "10^9 "],
        ["Billion",    "10^9 ", "10^12"],
        ["Billiard",   "     ", "10^15"],
        ["Trillion",   "10^12", "10^18"],
        ["Quadrillion","10^15", "10^24"],
        ["Quintillion","10^18", "10^30"],
        ["Sextillion", "10^21", "10^36"]  
    ]  # Hentet fra https://en.wikipedia.org/wiki/Names_of_large_numbers
    print("%9s %8s %7s" % ("Navn", "Lang", "Kort"))
    for i in range(len(store_tall)):
        print("%11s %7s %7s" % (store_tall[i][0], store_tall[i][2], store_tall[i][1]))
        
# I billion USD (kort form)
microsoft_inntekt_dollar = [
    [2002, 28.37],
    [2003, 32.19],
    [2004, 36.84],
    [2005, 39.79],
    [2006, 44.28],
    [2007, 51.12],
    [2008, 60.42],
    [2009, 58.44],
    [2010, 62.48],
    [2011, 69.94],
    [2012, 73.12],
    [2013, 77.85],
    [2014, 86.83],
    [2015, 93.58],
    [2016, 85.32],
    [2017, 89.95],
    [2018, 110.36],
    [2019, 125.84]
]  # Hentet fra https://www.statista.com/statistics/267805/microsofts-global-revenue-since-2002/

def oppgave2():
    """
    Så lenge bruker ikke har skrive inn 'ferdig' i inputfeltet, skal while
    løkka fortsette å gå og bruker skal få skrive inn heiltala sine.
    Bruker if løkke for å sjekke om input er en lovlig verdi. Dersom ja, legger
    til input verdien i 'liste_heltall'. Bruker if løkke til å sjekke hva
    medianen i lista vår er. Printer ut resultat.
    """
    liste_heltall = []
    slutt = False
    
    print("Skriv inn en rekke heltall, avslutt med 'ferdig': ")
    while not slutt:   
        input_verdi = input(str("Heltall: "))
        if input_verdi.isnumeric() and "." not in input_verdi:
            liste_heltall.append(input_verdi)
        elif input_verdi[0] == "-" and "." not in input_verdi:
            liste_heltall.append(input_verdi)
        elif input_verdi == "ferdig":
            slutt = True
        else:
            print("Verdien du skreiv inn er ikkje eit heiltall og har ikkje blitt lagt til i lista")
    
    # key=int forteller sort funksjonen at verdiene skal bli sorter etter
    # integer verdien sin, altså i vanlig stigende rekkefølgje som vi kjenner
    liste_heltall.sort(key=int)
    print(liste_heltall)
    
    if (len(liste_heltall) % 2) == 0:
        pos = int(len(liste_heltall) / 2)
        median_pos = (int(liste_heltall[pos - 1]) + int(liste_heltall[pos])) / 2
        print("Medianen av verdiene er:",median_pos)
    else:
        median_pos = int(len(liste_heltall) / 2 - 0.5)
        print("Medianen av verdiene er:",liste_heltall[median_pos])

def oppgave3a():
    """ 
    Lager en ny liste for inntekta i kroner, som er eksakt kopi fra
    'microsoft_inntekt_dollar'. Bruker så for løkke til å gå gjennom elementa
    vi er ute etter, altså inntekta, i lista og konverterer disse til norske 
    kroner. Har då gjort om alle elementa i posisjon [x][1] i microsoft_inntekt_kroner
    til norske kroner, mens den originale lista er uendra. Printer så ut begge
    listene på ein oversiktelig måte.
    """
    microsoft_inntekt_kroner = deepcopy(microsoft_inntekt_dollar)
    
    print("Microsoft inntekt i dollar:")
    for verdi in range(len(microsoft_inntekt_kroner)):
        #Her skjer konverteringa fra USD til NOK
        microsoft_inntekt_kroner[verdi][1] = round(microsoft_inntekt_kroner[verdi][1] * 8.68)
        print(microsoft_inntekt_dollar[verdi])
    print()
    print("Microsoft inntekt i kroner:")
    for verdi in range(len(microsoft_inntekt_dollar)):
        print(microsoft_inntekt_kroner[verdi])

def oppgave3b():
    """
    Bruker pyplot til å printe ut eit historgram over inntektene til Microsoft
    fra 2002 til 2019. Gjør dette ved å sette år og inntekt i egne, nye lister.
    Her blir antall år (years) i lista microsoft_inntekt_dollar
    x-verdiene på x-aksen, og inntekta det året (profit) y-verdiene på
    y-aksen. Formaterer plt for å få farger, tittel osv.
    """
    years = []
    profit = []
    for i in range(len(microsoft_inntekt_dollar)):
        years.append(microsoft_inntekt_dollar[i][0])
        profit.append(microsoft_inntekt_dollar[i][1])
     
    plt.bar(years, profit, width=0.9, color=["blue","cyan","darkblue"])
    plt.title("Inntekt Microsoft fra 2002 til 2019")
    plt.show(years, profit)


def oppgave3c():
    """ 
    Bruker for løkke til å summere sammen inntekta i kvart år mellom 2002 og 2019
    i lista microsoft_inntekt_dollar, for så å dele på 1000 for å få summen
    i billioner. Printer ut svaret med 2 desimaler.
    """
    summen = 0
    for i in range(len(microsoft_inntekt_dollar)):
        summen += microsoft_inntekt_dollar[i][1]
        summen_billioner = summen/1000
    print("Microsoft tjente %.2f billioner dollar i perioden 2002-2019." % (summen_billioner))
    

def oppdater_brett(spillerX, spillerY, monsterX, monsterY, itemX, itemY):
    """
    Her blir selve brettet i spillet vårt laget. Setter brettet lik en tom
    liste 'brett'. Bruker så for løkker i range(0,10) til å lage 10 nye lister inni lista 'brett'.
    Spiller, monster og item sine x og y koordinater blir valgt utenfor funksjonen,
    disse er derfor parametera våre som blir brukt inne i funksjonen. Sjekker
    med if løkke om den posisjonen for løkka vår står på er lik posisjonen
    til spiller, monster eller item. Dersom ja, sett inn passende symbol til
    elementet. Dersom nei skal "▪" bli lagt til i lista på gjeldene pos,
    tegnet brettet vårt er bygd opp av.
    Bruker så print(" ".join(brett[rad])) for å printe ut brettet vårt på 
    brukervennlig form. Denne funksjonen vil også oppdatere og printe ut
    endringer gjort på brettet.
    """
    brett = []
    for rad in range(0,10):
        brett.append([])
        for kolonne in range(0,10):
            if rad == spillerY and kolonne == spillerX:
                brett[rad].append("😃")
            elif rad == monsterY and kolonne == monsterX:
                brett[rad].append("👺")
            elif rad == itemY and kolonne == itemX:
                brett[rad].append(" ★")
            else:
                brett[rad].append(" ▪ ")
        print(" ".join(brett[rad]))
    
def flytt_spiller(bruker_input, spillerX, spillerY, monsterX, monsterY, itemX, itemY):
    """ 
    Funksjon som sjekker om monsteret står i samme posisjon som spiller, altså
    om spiller er død og har tapt spillet. Dersom ja, flytt spiller ut av
    brettet for å fjerne han. Bruker oppdater_brett for å få oppdatert versjon
    av brettet.
    """        
    if spillerX == monsterX and spillerY == monsterY:
        spillerX = -1
        spillerY = -1
        print("Du traff monsteret og er nå død!")
    oppdater_brett(spillerX, spillerY, monsterX, monsterY, itemX, itemY) 
 
def oppgave4():
    """
    Funksjonen som setter spillet i gang og holder det gående med while loop.
    """
    print("-------------------------------------------------------------------")
    print("Velkommen til monsterspillet. Målet er å samle stjerner, samtidig som du ikke treffer på monsteret.")
    print("Skriv inn w, a, s og d og trykk enter for å styre spilleren din.")
    print("Monsteret vil bevege seg tilfeldig rundt. Dersom spiller eller monster faller av brettet, vil de få en ny tilfeldig posisjon på brettet.")
    print("Om du vil avslutte spillet skriv inn 'endgame'.")
    print("-------------------------------------------------------------------")
    """
    Før while loopen starter blir de ulike variablene vi skal bruke inni while
    løkka gitt en startverdi. Dette bestemmer hvor spiller, monster og item
    vil "spawne" i starten av spillet. Legg merke til at slutt er satt til false,
    dette fordi while løkka er satt til å fortsette å loope så lenge slutt IKKE
    er true, altså at den er false. If løkke inne i while løkka bestemmer
    når slutt skal få verdien true, og spillet stopper.
    """
    slutt = False
    spiller_fall = 0
    monster_fall = 0
    spiller_poeng = 0
    monster_poeng = 0
    spillerX = 0
    spillerY = 0
    monsterX = 9
    monsterY = 9
    itemX = random.randint(0,9)
    itemY = random.randint(0,9)
    oppdater_brett(spillerX, spillerY, monsterX, monsterY, itemX, itemY)
    
    """
    While løkka som holder hele spillet gående. 
    """
    while not slutt:
        """
        If løkke som sjekker om det bokstaven som heile tida blir tasta inn i
        inputfelt er w, a, s eller d. Koordinatene til spiller skal så bli 
        endra på avhengig av kva bokstav som blei skrive inn. Om bruker skreiv
        inn noko anna vil han få ein feilmelding som seier at han må bruke 
        'wasd' for å styre spilleren.
        """
        bruker_input = str(input(" "))
        if bruker_input == "w":
            spillerY += -1
        elif bruker_input == "s":
            spillerY += 1
        elif bruker_input == "a":
            spillerX += -1
        elif bruker_input == "d":
            spillerX += 1
        else:
            print("Bruk 'wasd' for å styre spiller.")
        
        """
        If løkke som sjekker om posisjonen til spiller eller monster er utenfor
        brettet vårt, dersom ja skal de få en ny tilfeldig posisjon på brettet.
        I tillegg skal spiller_fall og monster_fall øke alt etter hvem det
        var som falt av brettet.
        """
        if (spillerX < 0 or spillerX > 9) or (spillerY < 0 or spillerY > 9):
            spillerX = random.randint(0,9)
            spillerY = random.randint(0,9)
            spiller_fall += 1
        elif (monsterX < 0 or monsterX > 9) or (monsterY < 0 or monsterY > 9):
            monsterX = random.randint(1,9)
            monsterY = random.randint(1,9)
            monster_fall += 1
           
        """
        If løkke som sjekker om spiller eller monster står i posisjonen
        til stjerna (itemX og itemY). Dersom ja skal stjerna bli "plukka opp"
        og en ny stjerne skal bli printa ut på en tilfeldig plass på brettet. 
        I tillegg vil spiller_poeng og monster_poeng øke med 1 alt etter 
        hvem som "plukket opp" stjerna.
        """
        if itemX == spillerX and itemY == spillerY:
            itemX = random.randint(0,9)
            itemY = random.randint(0,9)
            spiller_poeng += 1
        elif itemX == monsterX and itemY == monsterY:
            itemX = random.randint(0,9)
            itemY = random.randint(0,9)
            monster_poeng += 1
        
        """
        I hver gjennomgang av while løkka skal monster sin X og Y posisjon
        anten øke eller synke med 1. På denne måten vil monsteret bevege seg
        tilfeldig rundt på brettet for hver bevegelse spiller tar.
        """
        flytt = [-1,1]
        monsterX += random.choice(flytt)
        monsterY += random.choice(flytt)
        
        print("-------------------------------------------------------------------")
        print("Skriv inn w, a, s og d og trykk enter for å styre spilleren din.")
        print("Om du vil avslutte spillet skriv inn 'endgame'.")
        print("-------------------------------------------------------------------")
        
        
        """
        If løkke som sjekker om det ulike hendelsene som skal avslutte spiller
        har intruffet. Alt etter korleis spillet blei stoppa skal det skrives
        ut passende meldinger til brukeren om kor mange poeng han fikk, kor
        mange fall han hadde av brettet osv. Det er her variablene som 
        skulle økes tidligere blir printet ut. Dersom grunnen til at spillet
        var ferdig var at enten monster eller spiller hadde samlet nok stjerner,
        vil den nye stjerna som bli generert fjerna fra brettet, siden det ikke
        skal samles mer stjerner.
        
        Merk her og at slutt blir satt til true. Dette var betingelsen for at
        while løkka skulle slutte. While løkka vil derfor ikkje fortsette å 
        gå dersom en av disse hendelsene inntreffer.
        """
        if bruker_input == "endgame" or (monsterX == spillerX and monsterY == spillerY):
            slutt = True
            print("GAME OVER.")
            print("Antall fall av brett spiller:",spiller_fall)
            print("Antall fall av brett monster:",monster_fall)
            print("Du samlet",spiller_poeng,"stjerne(r) mens monsteret samlet",monster_poeng,"stk.")
        elif monster_poeng == 5 or spiller_poeng == 5:
            itemX = -1
            itemY = -1
            slutt = True
            print("GAME OVER.")
            print("Antall fall av brett spiller:",spiller_fall)
            print("Antall fall av brett monster:",monster_fall)
            if monster_poeng == 5:
                print("Monsteret var førstemann til å samle 5 stjerner og vant spillet!")
            elif spiller_poeng == 5:
                print("Du var førstemann til å samle 5 stjerner og vant spillet!")
        
        """
        Kaller på funksjonen som sjekker om spiller er "spist" av monsteret,
        og flytter spiller bort fra brettet.
        """
        flytt_spiller(bruker_input, spillerX, spillerY, monsterX, monsterY, itemX, itemY)
        


def main():
    """ 
    Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt. 
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet 
    foran oppgave-funksjonen slik at den blir "skrudd på".
    """
    # oppgave1()
    #print()
    # oppgave2()
    #print()
    #print()
    oppgave3a()
    #print()
    #oppgave3b()
    #print()
    #oppgave3c()
    #print() """
    # oppgave4()
    # print()
    
main()