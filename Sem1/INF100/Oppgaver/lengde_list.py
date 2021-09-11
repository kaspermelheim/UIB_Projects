# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:34:44 2019

@author: Kasper
"""
words_list = ["PHP", "Exercises", "Backend"]

def longestWord(words_list): 
    count = 0    #You set the count to 0
    for i in words_list: # Go through the whole list
        if len(i) > count: #Checking for the longest word(string)
            count = len(i)
            word = i
    return ("the longest string is " + word)
print(longestWord(words_list))