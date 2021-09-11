# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:14:57 2020

@author: Kasper
"""

n=int(input('please enter the no. in decimal format: '))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
print('The binary no. for %d is %s'%(x, string))