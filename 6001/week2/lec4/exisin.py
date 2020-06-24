#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:59:10 2020

@author: sidtrip
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = len(aStr)//2
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return aStr[0] == char
    
    elif(aStr[mid] == char):
        return True 
    
    elif(aStr[mid] > char):
        return isIn(char, aStr[ : mid])
        
    elif(aStr[mid] < char):
        return isIn(char, aStr[mid + 1 : ])
        