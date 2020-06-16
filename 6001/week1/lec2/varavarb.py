#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:13:55 2020

@author: sidtrip
"""

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print('smaller')