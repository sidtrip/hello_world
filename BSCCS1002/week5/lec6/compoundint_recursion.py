#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:39:13 2021

@author: sidtrip
"""
#Computing compound interest assuming interest to be 10%

def comp(p,n):
    if (n==1):
        return p*(1.1)
    else:
        return(comp(p,n-1))*1.1
        
print (comp(2000, 3))