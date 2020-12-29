# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:30:52 2020

@author: raysh
"""

"""
calculate the smaller angel between the 2 handles of a clock. Input the hour and minute, output the angle.
"""

def clock_angel(hour,minute):
    minute_angle=minute*(360/60)
    hour_angle=hour*(360/12)+(minute/60)*(360/12)
    diff=abs(hour_angle-minute_angle)
    return(min(diff,360-diff))

clock_angel(3,20)


