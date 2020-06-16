# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'oobobobvbobbpbobobob'
s = 'bobobobobobobobobob'
count = 0
for i in range(len(s)):
    if s[i : i+3] == 'bob':
        count += 1

print('Number of times bob occurs is: ' + str(count))
