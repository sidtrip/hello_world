#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:23:56 2020

@author: sidtrip
"""

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
updated = balance
minimum = 0
while updated > 0:
    updated = balance
    minimum += 10

    for month in range(1, 13):
        unpaid = updated - minimum
        updated = unpaid + (monthlyInterestRate * unpaid)
    
print(f'Lowest Payment: {minimum}')