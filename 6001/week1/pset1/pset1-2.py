#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 07:12:19 2020

@author: sidtrip
"""
s = 'bobobobobobobobobob'
times = 0
for c in range(len(s)):
    if s[c] == 'b':
        if len(s) >= c+2 and s[c+1] == 'o':
            if len(s) >= c+3 and s[c+2] == 'b':
                times += 1
print('Number of times bob occurs is: ' + str(times))