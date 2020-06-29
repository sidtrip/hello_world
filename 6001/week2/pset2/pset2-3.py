#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 06:33:04 2020

@author: sidtrip
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
minimum = 0
updated = balance




lower = balance / 12
upper = balance * ((1 + monthlyInterestRate)**12) / 12.0







while updated != 0:
    
    updated = balance
    guess = (upper + lower) / 2
    
    for month in range(1, 13):
        unpaid = updated - guess
        updated = unpaid + (monthlyInterestRate * unpaid)
    
    updated = round(updated, 1)
    if updated == 0:
        break
    
    if(updated < 0):
        upper = guess
        
    elif(updated > 0):
        lower = guess
        
    
    
    
    
print('Lowest Payment: ' + str(round(guess, 2)))