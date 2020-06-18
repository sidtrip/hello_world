#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 06:24:49 2020

@author: sidtrip
"""
guess = 0
neg_flag = False
quest = int(input('Enter a integer: '))
if quest < 0:
    neg_flag = True
while guess*guess < quest:
    guess +=1
if guess**2 == quest:
    print(f'square root of {quest} is {guess}' )
else:
    print(str(quest) + ' is not a perfect square')
    if neg_flag:
        print('Just checling.... did you mean', -quest, '?')
        