# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:09:35 2019

@author: Kasper
"""

#Oppgåve 1
# a)
x = 2
x += 2
print(x)
#Output: 4

#b)
x = 15
def f(x):
    print(x)
f(37)
#Output: 37

#c)
x = 15
def f(x):
    x = x * 2
f(x)
print(x)
#Output: 15

#d)
def g(b):
    return b + 1

def f(a):
    b = 10
    return g(a) + 1
print(f(1))
#Output: 3

#e
def f(a = 1, b = 2):
    return a * b
print(f(a=3))
#Output: 6

#Oppgåve 2
#a

x = 10
if x <= 0:
    svar = "ingen"
if x <= 5:
    svar = "noen"
if x <= 10:
    svar = "fler"
if x <= 100:
    svar = "mange"
print(svar)
#Output: mange

#b
l = [x*2 for x in [1,2,3,4]]
print(l[1])
#Output: 4

#c
l = [x*2 for x in ["a","b","c","d",]]
print(l[1])
#Output: bb

#Oppgåve 3
#a
s = "*"
for i in range(5):
    t = "-" * (5 - i)
    print(t + s*i + t)
#Output: 
#----------
#----*----
#---**---
#--***--
#-****-

#Oppgåve 4
#a
x = [1,2]
def double(l):
    return [a*2 for a in l]
double(x)
print(x)
#Output: [1.2]

#b
def f(x):
    x = x + 1
    return x
x = 3
f(x)
print(x)
#Output:3

#c
def f(x):
    x[0] = x[0] + 1
    return x
x = [3]
f(x)
print(x)
#Output: [4]

#Oppgåve 5
#a)

x = [1,2]
y = [x, x, x]
y[0] = [3,3]
x[0] = 3
print(y)
#Output: [[3, 3], [3, 2], [3, 2]]

#Oppgåve 6
def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
    
print(is_divisible(-3, 2))
print(is_divisible(4, 2))
#Output: False, True
    
#b
def is_prime(n):
    if n >= 2:
        for i in range(2, n//2):
            if n % i == 0:
                return False
        else:
            return True
print(is_prime(7))
print(is_prime(9))
#Output: True, False
#c
def evenize(l):
    for i in range(len(l)):
        if l[i] % 2 != 0:
            l[i] += 1
    return l

#d
def pos_num(l): 
    summen = 0
    for i in range(len(l)):
        if l[i] >= 0:
            summen += l[i]
    return summen

#Oppgåve 7
#a

def plural(word):
    n = len(word)
    for i in range(len(word)):
        if word[-1] == "y":
            return word[:-1] + "ies"
        elif word[n-2:n+1] == "sh" or word[n-2:n+1] == "ch" or word[-1] == "s":
            return word + "es"
        else:
            return word + "s"

#b
def count(l):
    telling = {}
    for i in l:
        telling[i] = telling.get(i, 0)
        telling[i] += 1
    return telling

#Oppgåve 9
#a
def center(s, width):
    s1 = s.strip()
    streng = ""
    ny = width - len(s1)
    for i in range(ny):
        streng += " "
    halv = ny//2
    nystreng = streng[:halv] + s1 + streng[halv:-1]
    return nystreng

#b
def print_tree(width, height):
    start = "*"
    print(center("x", 20))
    for i in range(height):
        start += "**"
        if i == 2 or i == 5:
            print(center(start[1:-3], 20))
        print(center(start, 20))
    print(center("*", 20))

#Oppgåve 8
#a
hendelser = []
status = {}

def reg_incident(navn, beskrivelse, poeng):
    status[navn] = status.get(navn, 0) + poeng
    hendelser.append([navn, beskrivelse, poeng, status.get(navn, 0)])
    return status, hendelser

#b
def is_nice(navn):
    if status[navn] >= 0:
        return True
    else:
        return False
    
def status_all():
    status_all = {}
    navn = status.keys()
    for i in navn:
        if is_nice(i):
            status_all[i] = True
        elif not is_nice(i):
            status_all[i] = False
    return status_all

#c
presents = [(23791, 'Dinosaurfigur', 0.3, 'AD-339'), (23792, 'Stripete slips', 0.2, 'ZR-201'),
                (23793, 'Lekekjøkken', 5.3, 'UB-799'), 
                (23794, 'PuffinBoard v0.1', 0.01, 'ZZ-237')]

def assign_presents(liste, available_coal=1.0):
    gaver = {}
    slemme = []
    navn = status.keys()
    for i in navn:
        if is_nice(i):
            gaver[i] = presents.pop()
        elif not is_nice(i):
            slemme.append(i)
            
    for i in slemme:
        per = round(available_coal / len(slemme), 2)
        gaver[i] = (0, "Kull", per, "")
        
    return gaver

#d

def person_log(navn):
    log = []
    for i in range(len(hendelser)):
        if hendelser[i][0] == navn:
            log.append(hendelser[i])
    return log
                    
def delete_person(navn):
    for i in range(0,len(hendelser)):
        if navn == hendelser[i][0]:
            hendelser[i] = None
            
    if navn in status.keys():
        del status[navn]
        
    return hendelser, status

def check_assignment(gaver):
    s = len(status)
    g = len(gaver)
    print("Dobbelsjekker lister: ")
    if s == g:
        print("Antall personer på gaveliste er lik antall personer registrert.")
    elif s > g:
        print("Antall personer registrert er større enn antall personer i gaveliste.")
    elif s < g:
        print("Antall personer i gaveliste er større enn antall personer registrert.")
        
    if gaver.keys() == status.keys():
        print("Alle registrerte personer er på gavelisten.")
        for i in gaver.keys():
            if (status[i] >= 0 and gaver[i][0] != 0) or (status[i] < 0 and gaver[i][0] == 0):
                print(i + " har fått rett gave.")
            else:
                print(i + " har fått feil gave.")
    else:
        print("Alle registrerte personer er ikke på gavelisten.")

def main():
    
    print(evenize([-3,4,5,9,0]))
    
    print(pos_num([-4,2,0,-5,9]))
    
    print(plural("daisy"))
    print(plural("present"))
    print(plural("dish"))
    print(plural("day"))
    print(plural("foot"))
    print(plural("witch")) 
    
    print(count(['apple', 'apple', 'grape', 'banana', 'pear', 'kiwi', 'kiwi', 'kiwi']))
    
    print(center('***', 30))
    print(center('    A Christmas Carol', 30)) 
    
    print_tree(10, 7)
    
    reg_incident("Kasper", "Stjelte kaker av mor.", -5)
    reg_incident("Kasper", "Slo til Alvar.", -10)
    reg_incident("Alvar", "Tilgav Kasper for slaget.", 10)
    reg_incident("Kjetil", "Sa hei til Postmannen", 5)
    reg_incident("Eskil", "Droppa ut av studiet.", -5)
    
    print(status)
    print(hendelser)
    
    print(is_nice("Alvar"))
    print(status_all()) 
    
    print(person_log("Kasper"))
    
    #delete_person("Kasper")
    
    print()
    print(status)
    print(assign_presents(presents))
    print()
    check_assignment(assign_presents(presents))
    
main()






























             
