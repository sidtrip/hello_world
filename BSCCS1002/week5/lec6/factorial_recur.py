#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:43:25 2021

@author: sidtrip
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))