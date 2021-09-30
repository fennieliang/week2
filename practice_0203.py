#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:33:07 2021

@author: fennieliang
"""
import math

for i in range (10):#from 0-19

    if math.remainder(i, 2)!=0:#exclude even number
        for j in range (20-int(i/2)):#position the print in centre 
            print (" ", end='')#print spaces before * 
        for k in range (i):#control the number of * to be printed
            print ("*", end='')
        print ('')
            
    