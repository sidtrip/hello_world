#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:48:19 2020

@author: sidtrip
"""

x = float(input("enter x: "))
y = float(input("enter y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is ", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks!")
