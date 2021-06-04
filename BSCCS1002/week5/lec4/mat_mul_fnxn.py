#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:19:42 2021

@author: sidtrip
"""

# inititallizse C to zero
# need to consider twom matrices A and B
# need to find the dot product of two lsits
# need to pick ith tow and jth column in matrix

def initialize_mat(dim):
    #code verified, works on test case
    C = []
    for i in range(dim):
        C.append([])
        for j in range(dim):
            C[i].append(0)
    return C

def dot_product(u, v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans += (u[i]*v[i])
    return ans

def row(M, i):
    l = M[i]
    return l

def column(M,j):
    dim = len(M)
    l = []
    for i in range(dim):
        l.append(M[i][j])
    return l

def mat_mul(A,B):
    dim = (len(A))
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C
    
def main():
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[1,2,1],[3,1,7],[6,2,3]]
    C = mat_mul(A,B)
    for i in range(len(A)):
        print(C[i])

    
    
    
    
    
    