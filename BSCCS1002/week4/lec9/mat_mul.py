#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:21:56 2021

@author: sidtrip
"""

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
B = []

A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim = 3

#C[i][j] is the dot product of the ith row or A and jth column of B

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k]* B[k][j]
            
print(C)

#another way, using numpy

import numpy

M = numpy.mat(A)

N = numpy.mat(B)

print(M*N)