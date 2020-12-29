# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:47:06 2020

@author: raysh
"""

"""
create a function to return the kth Fibonacci number
"""


def fib_num(k):
    if k==1:
        return 0
    if k==2:
        return 1
    #recursive function
    return fib_num(k-2)+fib_num(k-1)


fib_num(10)


        