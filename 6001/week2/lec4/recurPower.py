#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:51:12 2020

@author: sidtrip
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
    