#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 08:47:03 2020

@author: sidtrip
"""

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def f(x):
    return abs(x)
applyToEach(testList, f)

def f(x):
    return x + 1
applyToEach(testList, f)

def f(x):
    return x**2
applyToEach(testList, f)