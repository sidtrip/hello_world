#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 06:29:18 2020

@author: sidtrip
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oTup = ()
    for element in range(0,len(aTup),2):
        oTup += (aTup[element],)
    return oTup

r = oddTuples((19, 20, 8, 3, 18, 7, 6, 19))
print(r)