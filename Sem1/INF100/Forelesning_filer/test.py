#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer ulike operasjonar på lister
@author: nmidd
"""
lower_bound = {
        0: "none",
        1: "one",
        2: "more than one",
        3: "some",
        10: "many"
}

def estimate(num):
    key_list = sorted(lower_bound.keys())
    lowest = 0
    value = "none"
    for i in key_list:
        if i <= num:
            lowest = i
            value = lower_bound[i]
    return value

print(estimate(99))
        

"""
#a)
def estimate(num):
    if num == 0:
        return "none"
    elif num == 1:
        return "one"
    elif num == 2:
        return "more than one"
    elif num >= 3 and num <= 9:
        return "some"
    elif num >= 10:
        return "many" 
"""

def ESTIMATE(num, suffix= "."):
    text = estimate(num)
    cap_text = exam.cap(text)
    final_text = cap_text + suffix
    return final_text


def unique(s):
    final_text = ""
    for char in s:
        if char == " ":
            final_text += char
            continue
        if char in final_text:
            continue
        else:
            final_text += char
    return final_text
            
print(unique("F****d up beyond all recognition!"))
    
