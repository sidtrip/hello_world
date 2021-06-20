#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:18:55 2021

@author: sidtrip
"""
malgudi = ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his',
 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After',
 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to',
 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at',
 'the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the',
 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his',
 'thin', 'long', 'cane...']
def freqWords(words):
    #CLEANING DATA
    #Punctuatuions to be removed
    removeList = [',', ';', ':', '.', '!']
    d = {}
    malguda = []
    for index in range(len(malgudi)):
        #Removing Punct
        new = ''
        for letter in malgudi[index]:
            if letter not in removeList:
                new += letter
        malguda.append(new)
        #Making list items lower case        
        malguda[index] = malguda[index].lower()
        if malguda[index] not in d:
            d[malguda[index]] = 1
        else:
            d[malguda[index]] += 1
    
    #reversing the dictionary
    finalD = {}
    for i in d:
        if d[i] not in finalD:
            finalD[d[i]] = [i]
        else:
            finalD[d[i]].append(i)
        
    print(finalD)