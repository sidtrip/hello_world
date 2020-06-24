#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 07:25:47 2020

@author: sidtrip
"""

def hanoi(n, kahan, to, via):
    if n == 1:
        printer(kahan, to)
    else:
        hanoi(n-1, kahan, via, to)
        hanoi(1, kahan, to, via)
        hanoi(n-1, via, to, kahan)
        
def printer(kahan, to):
    print('Move coins from {} to {}.'.format(kahan, to))

hanoi(25, 'pillar1', 'pillar3', 'pillar2')
