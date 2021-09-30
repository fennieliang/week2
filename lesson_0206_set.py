#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:04:38 2021

@author: fennieliang
"""

#set{item1, item2,...} unique item only

a=['apple','melon','orange','pine apple','apple']

b = set(a) #make a set from a list
print (b)
  
b.add('melon') #set can only have uniq items
print (b)

b.remove('apple') #if the item doesn't exist in the set then error occurs 
print (b) 
  
b.discard('melon') #no error occurs if the item doesn't exist in the set
print (b) 

a1=["meat","fish","egg"]

b.update(a1) #use update to append a list 

print (b) 

print (b.pop()) #return the poped item

b.pop()#pop will drop the first item

print (b) 

set1={'orange', 'melon', 'pine apple', 'apple'}
set2={'orange', 'meat', 'pine apple', 'fish', 'egg'}

print (set1|set2)#set1 or set2 
print (set1.union(set2))#same as above

print (set1-set2)#remove items appear in set2
print (set1&set2)#pick items in both sets

print (set1.difference(set2))
print (set2.difference(set1))
