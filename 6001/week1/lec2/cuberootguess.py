#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:32:32 2020

@author: sidtrip
"""

#Program 1

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x)+ ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of '+ str(x) + ' is ' +  str(ans))
    


#Program 2    
    
    
cube = -27
for guess in range (abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
        
    print("Cube root of" + str(cube) + "is" + str(guess))