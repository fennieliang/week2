#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:56:50 2021

@author: fennieliang
"""
#list [item1, item2,...]

a=['apple','melon','orange','pine apple']


a.append('tomato')# append single item
#print (a)

a.insert(3,'tomato')# insert into a certain position
#print (a) 

a.remove('apple')# indicate the item to be remove
#print (a) 

a.pop(1)#pop out a certain position
print (a) 


a1=['fish','pork']

#a.append(a1)# append a list
print(a)


a.extend(a1) 
print(a)

print (a.index('fish')) #find the index

print (a.count('tomato')) #count quantity

a.reverse()# do the action before printing

print (a)

a.sort()# in the alphabetic order
print (a)

a2=a.copy() #equals to a2=a

print (a2)



a1=['fish','pork']

a.extend(a1)
print (a)

a.extend('tomato') 
print (a)

for fruit in a:
    print(fruit) 
    

  
a.clear()

print (f"final list:{a}")

'''
practice 0205 print the list a using range
'''

