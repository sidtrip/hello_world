#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:28:32 2020

@author: sidtrip
"""

def calmonremain(month, prevbal):
    
    monthintrate = annualInterestRate/12.0
    minimumpayment = monthlyPaymentRate * prevbal
    monthlyunpaid = prevbal - minimumpayment
    
    
    updatedbalance = monthlyunpaid + (monthintrate * monthlyunpaid)
    print(f'month {month} balance {updatedbalance}')
    return updatedbalance


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04




for month in range(1, 13):
    balance = calmonremain(month, balance)
   


print('Remaining balance: {}'.format(round(balance, 2)))







  
    