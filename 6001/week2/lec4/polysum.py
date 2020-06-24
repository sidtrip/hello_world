#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:52:13 2020

@author: sidtrip
"""
import math

def polysum(n, s):
    area = ((0.25*n*s**2)/math.tan(math.pi/n))
    perimeter = s*n
    
    polysumi = area + perimeter**2
    return round(polysumi, 4)

polysum(5, 9)