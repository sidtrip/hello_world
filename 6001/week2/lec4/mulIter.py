#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:00:42 2020

@author: sidtrip
"""

def mulIter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print(mulIter(5, 6))