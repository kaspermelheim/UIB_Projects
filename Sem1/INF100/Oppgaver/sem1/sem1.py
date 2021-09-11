# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:18:35 2019

@author: Kasper
Seminaroppgave 1
"""

print("---------- 1: Stigende eller synkende ----------")

#1.a
# Har 3 ulike variabler med input, sjekker om fleire tilfelle er sant
# med if løkka. Dersom ikkje går den rett til else.
# Printer ut resultatet.
tall_1= int(input("Skriv inn heltall nr. 1: "))
tall_2 = int(input("Skriv inn heltall nr. 2: "))
tall_3 = int(input("Skriv inn heltall nr. 3: "))

print("Tall nr 1: %.f " % tall_1)
print("Tall nr 2: %.f " % tall_2)
print("Tall nr 3: %.f " % tall_3)

if tall_2 < tall_1 and tall_3 < tall_2:
    print("Tallene er i synkende rekkefølge.")
elif tall_2 > tall_1 and tall_3 > tall_2:
    print("Tallene er i stigende rekkefølge.")
else: 
    print("Tallene er ikke i stigende eller synkende rekkefølge.")

print("--------- 2: Hurtignotasjon for kort ----------")

#2.a
# Lager en if løkke som spør om input verdien er den samme som 
# verdien vi er ute etter.
bokstav = str(input("Skriv inn en bokstav (D, H, C, S): "))
if bokstav == "D":
    print("Ruter.")
elif bokstav == "H":
    print("Hjerte.")
elif bokstav == "C":
    print("Spar.")
elif bokstav == "S":
    print("Kløver.")
else:
    print("Du har skrive inn en ugyldig bokstav.")

print("-------------------------------------------------")

#2.b
# Tar input verdien, sjekker den i if løkka og printer ut resultatet.
# Printer ut feilmelding om verdien er feil.
input_verdi = input("Skriv inn et tall eller bokstav (A, 2,...,10, J, Q, K): ")

if input_verdi == "A":
    print("Ess.")
elif input_verdi == "2":
    print("To.")
elif input_verdi == "3":
    print("Tre.")
elif input_verdi == "4":
    print("Fire.")
elif input_verdi == "5":
    print("Fem.")
elif input_verdi == "6":
    print("Seks.")
elif input_verdi == "7":
    print("Sju.")
elif input_verdi == "8":
    print("Åtte.")
elif input_verdi == "9":
    print("Ni.")
elif input_verdi == "10":
    print("Ti.")
elif input_verdi == "J":
    print("Knekt.")
elif input_verdi == "Q":
    print("Dame.")
elif input_verdi == "K":
    print("Konge.")
else:
    print("Du har skrive inn en ugyldig bokstav.")

print("---------- 3: Valutakalkulator ----------")

#3.a
# Tar tallverdien i variabelen "verdi" og stringen i "valutakurs"
# og  sjekker om de som blir skrive inn i input er lik de verdiene vi ser etter
# Printer så ut den konverterte verdien, i NOK.
verdi = float(input("Skriv inn ein verdi som flyttall: "))
valutakurs = str(input("Skriv inn valutakursen i tekst: "))

if valutakurs == "EUR":
    NOK = (9.68551*verdi)
    print(verdi,"i",valutakurs,"= %2.2f NOK" % (NOK))
elif valutakurs == "USD":
    NOK = (8.50373*verdi)
    print(verdi,"i",valutakurs,"= %2.2f NOK" % (NOK))
elif valutakurs == "GBP":
    NOK = (11.0134*verdi)
    print(verdi,"i",valutakurs,"= %2.2f NOK" % (NOK))
elif valutakurs == "SEK":
    NOK = (0.92950*verdi)
    print(verdi,"i",valutakurs,"= %2.2f NOK" % (NOK))
elif valutakurs == "AUD":
    NOK = (6.06501*verdi)
    print(verdi,"i",valutakurs,"= %2.2f NOK" % (NOK))
else:
    print("Du har skrive inn en ugyldig verdi.")
    
#3.b
# Gjør det samme i 3b som i 3a, har berre endra koden litt sånn at vi nå
# skriver inn verdien i NOK og får ut verdien i ønska valutakurs (den kursen
# brukeren skrev inn i "valutakurs")
verdi = float(input("Skriv inn ein verdi som flyttall: "))
valutakurs = str(input("Skriv inn valutakursen i tekst: "))

if valutakurs == "EUR":
    EUR = (verdi / 9.68551)
    print(verdi,"i NOK = %.2f EUR" % (EUR))
elif valutakurs == "USD":
    USD = (verdi / 8.50373)
    print(verdi,"i NOK = %.2f USD" % (USD))
elif valutakurs == "GBP":
    GBP = (verdi / 11.0134)
    print(verdi,"i NOK = %.2f GBP" % (GBP))
elif valutakurs == "SEK":
    SEK = (verdi / 0.92950)
    print(verdi,"i NOK = %.2f SEK" % (SEK))
elif valutakurs == "AUD":
    AUD = (verdi / 6.06501)
    print(verdi,"i NOK = %.2f AUD" % (AUD))
else:
    print("Du har skrive inn en ugyldig verdi.")
    
print("---------- 4: Opphøyd i potens 3 ----------")

#4.a
# Lar heltall gå fra 0 til men ikke med 11.  
# Printer så ut svaret for alle verdiene opphøyd i 3.
for heltall in range (0,11):
    print(heltall,"** 3 = ",(heltall ** 3))

print("---------- 5: Delelig på N ----------")

#5.a
# Har 3 variabler som bruker skriver inn verdier for. Bruker så if og for 
# løkker for å først sjekke om "start" er større en "stop", og omvendt.
# Går så gjennom alle tall mellom "start" og stop og sjekker om de er delelige
# med "n". Printer så ut resultat.
start = int(input("Skriv inn heltall start: "))
stop = int(input("Skriv inn heltall stop: "))
n = int(input("Skriv inn heltall du vil dele på (ikke 0): "))

print("Verdier mellom",start,"og",stop,"som er delelige på",n,":")
if start < stop:
    for i in range (start, stop+1):
        if (i % n == 0):
            print(i)
elif start > stop:
    for i in range (start, stop-1, -1):
        if (i % n == 0):
            print(i)
else:
    print("Start og stop kan ikkje være samme verdi!")

print("-------- 6: Temperaturtabell --------")

#6.a
# Definerer her funksjonen "tilFahrenheit" først. Den skal print ut celsius
# sammen med konverteringa fra celsius til fahrenheit. Har og valt å sette
# in mellomrom mellom for å få ein fin og ryddig tabell.
# For løkka teller fra 0 til 100 med 10 i mellomrom, og for hver verdi blir
# funksjonen kalla på, og printer ut resultatet.
def tilFahrenheit(celsius):
    print("%7.d %13.d" % (celsius,((celsius*1.8)+32)))
print("Celsius    Fahrenheit")
for x in range(0,101,10):
     tilFahrenheit(x)

#6.b
# Bruker koden i 6.a. Legger til if løkke som størrelsen på "celsius", og
# endrer "status_mld" alt etter hva "celsius" er. Legger og til at print
# inne i funksjonen skal inkludere "status_mld. Printer ut resultatet.
def tilFahrenheit(celsius):
    if celsius <= 60:
        status_mld = "Jeg har det bra."
    else:
        status_mld = "Jeg svetter i hjel!"
    print("%7.d %13.d    %s" % (celsius,((celsius*1.8)+32),status_mld))
print("Celsius    Fahrenheit       Status")
for x in range(0,101,10):
    tilFahrenheit(x)
    
print("---------- 7: Inflasjonsmål ----------")

#7.a
# Definerer her funksjonen renteOkning som får 3 parameter "verdi", "fra" og
# "til". Inne i funksjonen blir antall terminer regnet ut, inflasjonsmålet 
# blir oversiktlig definert, og vi får den nye "fiksa" verdien i en egen
# variabel. Printer så ut en melding som inkluderer verdiene som blir skrevet
# inn på linje 205 når vi kaller på funksjonen, og utrekningene som blir utført
# inne i funksjonen. 
def renteOkning(verdi, fra, til):
    terminer = int(til-fra)
    inflasjon_maal = 1.02
    verdi_fixed = (verdi*(inflasjon_maal)**(terminer))
    print("%.2f kr i år %d, med et inflasjonsmål på %.2f årlig, er i %d verdt %.2f kr." 
          % (verdi, fra, inflasjon_maal, til, verdi_fixed))
    
renteOkning(100,1910,2020)
    
    
        
        
        
    
    
    
     
     