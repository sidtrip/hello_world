#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 06:55:59 2020

@author: sidtrip
"""

s = 'azcbobobegghakl'
num_vow = 0
for ch in s:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        num_vow += 1
print('Number of vowels: ' + str(num_vow))
