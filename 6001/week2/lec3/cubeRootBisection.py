#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:07:50 2020

@author: sidtrip
"""

num = int(input('Enter a number to find the cube root of? \n'))
ans = low = num_guesses = 0
high = num
epsilon = 0.008

if num > 1:
    while(abs(ans**3 - num) >= epsilon):
        ans = (high + low) / 2
        num_guesses += 1
        if ans**3 > num:
            high = ans
        else:
            low = ans
    print('number of guesses = ', num_guesses)
    print(ans , ' is close to the cube root of ', num)

    