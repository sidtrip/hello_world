# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

unsorted_list = [12, 10, 7, 18, 6, 42, 8, 35]

sorted_list = []


while len(unsorted_list) > 0:
    smallest = unsorted_list[0]
    for number in unsorted_list:
        if number < smallest:
            smallest = number
      
    sorted_list.append(smallest)
    unsorted_list.remove(smallest)
    
print(sorted_list)