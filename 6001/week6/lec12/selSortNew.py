# -*- coding: utf-8 -*-

def selection_sort(L):
    suffixStart = 0
    while suffixStart != len(L):
        print(L)
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
        
test = [1, 5, 3, 8, 4, 9, 6, 2]