#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 08:03:28 2020

@author: sidtrip
"""

quest = int(input('Enter a num: '))
epsilon = 0.01
num_guesses = 0
low = 0
high = quest
ans = (high+low)/2.0

while abs(ans**2 - quest) >= epsilon:
    print(f'low = {low} high = {high} ans = {ans}')
    num_guesses += 1
    if ans**2 < quest:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print(f'number of guesses = {str(num_guesses)}')
print(f'{ans} is close to square root of {quest}')