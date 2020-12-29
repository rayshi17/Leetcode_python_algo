# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 00:02:22 2020

@author: raysh
"""

"""
how to reverse a string
"Today is a good day"
to 
"day good a is Today"
preserve the space
"""

def reverse(s):
   return s.split()[::-1]


print(reverse('Today is a good day'))
    