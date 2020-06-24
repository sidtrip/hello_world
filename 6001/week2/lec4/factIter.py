#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:16:57 2020

@author: sidtrip
"""

def factIter(n):
    prod = 1
    for i in range(n):
        prod *= i+1
    return prod



print(factIter(6))