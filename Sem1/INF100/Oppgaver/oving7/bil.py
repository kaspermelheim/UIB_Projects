# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:33:05 2019

@author: Kasper
"""

class Bil():
    
    def __init__(self, navn, x, y, bensin):
        self.navn = navn
        self.x = x
        self.y = y
        self.bensin = bensin
    
    def kjørNord(self, distanse):
        for i in range(0,distanse):
            if self.bensin > 0:
                self.y -= 1
                self.bensin -= 1
            else:
                self.y -= 0
                self.bensin += 0
                print("{} er tom for bensin!".format(self.navn))
                return self.y, self.bensin
    
    def kjørSør(self, distanse):
        for i in range(0,distanse):
            if self.bensin > 0:
                self.y += 1
                self.bensin -= 1
            else:
                self.y += 0
                self.bensin += 0
                print("{} er tom for bensin!".format(self.navn))
                return self.y, self.bensin
    
    def kjørVest(self, distanse):
        for i in range(0,distanse):
            if self.bensin > 0:
                self.x -= 1
                self.bensin -= 1
            else:
                self.x -= 0
                self.bensin -= 0
                print("{} er tom for bensin!".format(self.navn))
                return self.x, self.bensin
    
    def kjørØst(self, distanse):
        for i in range(0,distanse):
            if self.bensin > 0:
                self.x += 1
                self.bensin -= 1
            else:
                self.x += 0
                self.bensin -= 0
                print("{} er tom for bensin!".format(self.navn))
                return self.x, self.bensin
    
    def fyllBensin(self, enheter):
        self.bensin += enheter
        return self.bensin
    
    def printStatus(self):
        print("{} befinner seg på ({},{}) med {} enheter bensin igjen".format(self.navn,
                self.x, self.y, self.bensin))