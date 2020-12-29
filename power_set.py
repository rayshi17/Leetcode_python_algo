# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 00:58:44 2020

@author: raysh
"""

"""
create a power set of the given set, including [] and the set itself
"""
#iterative method
def power_set(s):
    output=[[]]
    for i in s:
        output+=[o+[i] for o in output]
        
    return output


power_set([1,2,3,4,5])

