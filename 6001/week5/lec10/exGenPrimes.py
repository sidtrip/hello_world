#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:38:56 2020

@author: sidtrip
"""

def genPrimes():
    primeList = []
    x = 2
    
    while True:
        bulu = True
        for i in primeList:
            if x % i == 0:
                bulu = False
                break
        if bulu == True:
            primeList.append(x)
            y = x
            x += 1
            yield y
        else:
            x += 1
