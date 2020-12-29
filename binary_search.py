# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:31:14 2020

@author: raysh
"""

"""
binary search for a sorted list, given a list, and a target, return the index of the target if it is in the list
otherwise return -1
the list is already sorted as ascending.
"""


def binary_search(nums,target):
    #get number of elements in list and initialize 2 pointer
    N= len(nums)
    l,r=0,N-1
    
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
                r=mid-1
                
    return -1
                

binary_search([-2,3,5,7,9,10,12],10)
        

        
    
    