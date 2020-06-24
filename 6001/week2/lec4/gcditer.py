#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 07:49:06 2020

@author: sidtrip
"""

def gcdIter(a, b):
    gcd = 1
    if a < b:
        smaller = a
    else:
        smaller = b
    while smaller > 1:
        if not(a % smaller) and not(b % smaller):
            gcd = smaller
            break
        smaller -= 1
    return gcd
'''
def gcdIter(a, b):
    
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
'''