#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:11:35 2020

@author: darksho
"""


import time
i = 1
n = 1

while i < 1000000:
    print(str(n) + "  //  " + str(i))
    time.sleep(1) #sleep for 1 second
    i = i * 2
    n = n + 1
    
    