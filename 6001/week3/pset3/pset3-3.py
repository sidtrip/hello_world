#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:07:23 2020

@author: sidtrip
"""

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    x = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            x += i
    return x

'''
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
'''
