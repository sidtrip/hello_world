#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:40:55 2020

@author: sidtrip
"""

x = int(input("Enter Values. x: "))
y = int(input("Enter Values, y: "))
z = int(input("Enter Values, z: "))
if x < y and x < z:
    print("X is the smallest of the all")
elif y < z:
    print("y is least")
else:
    print("z is smallest of them all")