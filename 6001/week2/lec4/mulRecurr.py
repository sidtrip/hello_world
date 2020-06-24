#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:13:15 2020

@author: sidtrip
"""

def mulRecurr(a, b):
    if b == 1:
        return a
    else:
        return a + mulRecurr(a, b-1)


print(mulRecurr(5, 6))