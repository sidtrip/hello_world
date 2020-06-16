#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:14:26 2020

@author: sidtrip
"""

x = 25
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans =ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))
