#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:02:40 2021

@author: sidtrip
"""
def sum(m):
    ans = 0

    for i in range(1, m+1):
        ans += (i)
    return ans

def resum(n):
    if (n==1):
        return 1
    else:
        return n+resum(n-1)

print(sum(10))
print(resum(10))