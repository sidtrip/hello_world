#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:15:36 2020

@author: sidtrip
"""
num = low = uip= 0
high = 100

print('Please think of a number between 0 and 100!')

while uip != 'c':
    
    num = (int((low + high)/2))
    print('Is your secret number ' + str(num) + '?')
    uip = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if uip == 'h':
        high = num
    elif uip == 'l':
        low = num
    elif uip == 'c':
        break
    else:
        print('Sorry, I did not understand your imput.')
print('Game over. Your secret number was: ' + str(num))
