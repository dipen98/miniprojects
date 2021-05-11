# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:14:16 2021

@author: Dipen
"""

import time

def countdown(t):
    while t :
        mins,secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end=" \r")
        time.sleep(1)
        t -=1
    return "timer completed"

t = input('Enter the time in seconds: ')

countdown(int(t))