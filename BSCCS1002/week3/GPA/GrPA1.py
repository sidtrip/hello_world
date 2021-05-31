#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:06:49 2021

@author: sidtrip
"""

n = int(input())
su = 0
for i in range(1, n+1):
    tsu = 0    
    
    for j in range(1, i+1):
        tsu += 1
        su += tsu

print(su)