# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:18:45 2020

@author: raysh
"""

"""
calculate the max profit of buy and sell a stock. the list contains the price of the stock at the ith day
you can only buy and then sell to gain profits.
retunn the max profit of the list of price.
"""


def maxprofit(price):
    currmax=0
    globalmax=0
    
    for i in range(1,len(price)):
        currmax=max(currmax+price[i]-price[i-1], 0)
        globalmax=max(currmax,globalmax)
        
    return globalmax


maxprofit([6,4,8,19,22,30,5])



        