#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:29:06 2021

@author: sidtrip
"""
import random 
#write a code to find dot product of vectors

x = random.sample(list(range(500)), 5)
y = random.sample(list(range(500)), 5)

dot_product = 0
for i in range(len(x)):
    dot_product += x[i] + y[i]

    
print(dot_product)