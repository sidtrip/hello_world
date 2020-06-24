#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:19:47 2020

@author: sidtrip
"""

def factRecurr(n):
    if n == 1:
        return 1
    else:
        return n * factRecurr(n-1)


print(factRecurr(6))