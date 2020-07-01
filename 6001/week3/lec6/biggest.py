#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:41:33 2020

@author: sidtrip
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    lon = 0
    for elements in aDict.values():
        if len(elements) > lon:
            lon = len(elements)
    for e in aDict:
        if len(aDict[e]) == lon:
            return(e)
    

biggest(animals)
