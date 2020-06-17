#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 07:49:01 2020

@author: sidtrip
"""
s = 'azcbobobegghakl'
str_in_iter = '' 
str_in_prev_iter = ''
prev_letter = s[0]
for i in range(len(s)):
    if s[i] >= prev_letter:
        str_in_iter += s[i]
        prev_letter = s[i]
        if len(str_in_iter) > len(str_in_prev_iter):
            str_in_prev_iter = str_in_iter
    else:
        str_in_iter = '' + s[i]
        prev_letter = s[i]
print('Longest substring in alphabetical order is: ' + str_in_prev_iter)
        


