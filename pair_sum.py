# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:15:43 2020

@author: raysh
"""

# python example for coding
# 1. pair sum
"""
Define a function that takes input as a array and integer K, returns the pair of 2 numbers in the arrary
which sum up to K.
"""
def pair_sum(array, k):
    #initial check 
    if len(array)<2:
        return print("The array is too short")
    #initialize the variables
    seen=set()
    output=set()
    
    # start the for loop to check
    for i in array:
        target = k - i
        if target not in seen:
            seen.add(i)
            
        else:
            output.add((min(i, target),max(i, target)))
        
    print('\n'.join(map(str, list(output))))
    
    
    
pair_sum([1],2)

pair_sum([1,3,4,5,22],5)
            
            
    