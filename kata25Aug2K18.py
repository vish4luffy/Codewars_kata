#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:44:28 2018

@author: gireesh
"""
from functools import cmp_to_key
# import collections as ct1

def order_weight(strng):
    if strng:
        l2=[]
        temp=0
        l1=[int(st.strip()) for st in strng.split(' ')]
        # print(l1, type(l1[0]))
        for i in l1:
            x=sum_digits(i)
            l2.append(x)
        d2=list(zip(l1, l2))
        print("d2", d2)
        d3 = sorted(d2, key=lambda x: (x[1]))
        print("d3", d3)
        for j in range(1, len(d3)):
            for i in range(1,len(d3)):
                if d3[i][1]==d3[i-1][1]:
                    if str(d3[i][0])<str(d3[i-1][0]):
                        temp=d3[i-1]
                        d3[i-1]=d3[i]
                        d3[i]=temp
        l3=[str(i[0]) for i in d3]
        return ' '.join(l3)
    elif strng=="" or strng==" ":
        return strng


def order_weight2(strng):
    if strng:
        l2=[]
        temp=0
        l1=[int(st.strip()) for st in strng.split(' ')]
        # print(l1, type(l1[0]))
        for i in l1:
            x=sum_digits(i)
            l2.append(x)
        d2=list(zip(l1, l2))
        print("d2", d2)
        d3 = sorted(d2, key=lambda x: (x[1]))
        print("d3", d3)
        x2=len(d3)
        notSorted=True
        while(notSorted):
            for j in range(1, x2):
                for i in range(1,x2):
                    if d3[i][1]==d3[i-1][1]:
                        if str(d3[i][0])<str(d3[i-1][0]):
                            temp=d3[i-1]
                            d3[i-1]=d3[i]
                            d3[i]=temp
                            x2-=1
            notSorted=False
        l3=[str(i[0]) for i in d3]
        return ' '.join(l3)
    elif strng=="" or strng==" ":
        return strng
        

def order_weight3(strng):
    if strng:
        l2=[]
        l1=[int(st.strip()) for st in strng.split(' ')]
        for i in l1:
            x=sum_digits(i)
            l2.append(x)
        d2=list(zip(l1, l2))
        # print("d2", d2)
        # d3 = sorted(d2, key=lambda x: (x[1]))
        d3=sorted(d2, key=lambda x: (x[1], str(x[0])))
        l3=[str(i[0]) for i in d3]
        return ' '.join(l3)
    elif strng=="" or strng==" ":
        return strng

def cmp_items(a, b): # a,b would be the tuples in d2
    if a[1] > b[1]:  # i'm checking the weights of a, b
        # a, b = b, a
        return 1
    elif a[1] == b[1]:  # checking if the weights are equal
        if str(a[0])>str(b[0]):
            return 1
        elif str(a[0])==str(b[0]):
            return 0
        else:                        
            return -1
    else:
        return -1

def order_weight4(strng):
    if strng:
        l2=[]
        l1=[int(st.strip()) for st in strng.split(' ')]
        for i in l1:
            x=sum_digits(i)
            l2.append(x)
        d2=list(zip(l1, l2))
        print("d2", d2)
        cmp_items_py3 = cmp_to_key(cmp_items)
        d2.sort(key=cmp_items_py3)
        print("d2 after sorting", d2)
        l3=[str(i[0]) for i in d2]
        return ' '.join(l3)
    elif strng=="" or strng==" ":
        return strng

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# =============================================================================
# 102 103 4 122 50 50 51 60 106 106 115 
# 62 8 153 54 82 137 183 190020 66 93 94 94 185 
# 266001 87 97 197 406207 208082 304229 132646 22576 
# 128804 188421 393603 427409 468053 324927 95445 24679 
# 62794 167285 37784 74828 197274 34959 36975 490387 285675 275995
# 
# =============================================================================

print(order_weight4('2000 10003 1234000 44444444 9999 11 11 22 123'))
# print(order_weight('102 103 4 50 122 50 51 60 106 106 115 62 8 153 54 82 137 183 190020 66 93 94 94 185 266001 87 97 197 406207 208082 304229 132646 22576 128804 188421 393603 427409 468053 324927 95445 24679 62794 37784 167285 74828 34959 197274 36975 490387 285675 275995'))