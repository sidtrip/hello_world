#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 06:53:11 2020

@author: sidtrip
"""
quest = int(input('Enter the number to find cube root of: '))
guess = 0
step = 0.001
epsilon = 0.01
num_guesses = 0

while (abs(guess**3 - quest) >= epsilon) and guess <= quest:
    guess += step
    num_guesses += 1
print(f'number of guesses {num_guesses}')
if (abs(guess**3 - quest) >= epsilon):
    print(f'failed on cube root of {quest}')
else:
    print(guess, 'is close to the cube root of', quest)

    