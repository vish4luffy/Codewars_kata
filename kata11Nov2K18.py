#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 08:59:25 2018

5 Kyu - Hamster Me Kata

@author: gireesh
"""

from collections import OrderedDict as od
from copy import deepcopy as dp
import string

def char_incr(i):
    incr=1
    #if letter is lowercase
    asci = ord(i)
    if (asci >= 97) & (asci <= 122):            
        asci += incr
      # for increment case
        if asci > 122 :
            asci = asci%122 + 96
        # for decrement case
            if asci < 97:
                asci += 26
        return chr(asci)

def hamster_me(code, message):
    l1=[ch for ch in "".join(od.fromkeys(code))]
    # print(l1)
    d1={}; i=1; l3=[]; l4=[]; j=2; listCheck=[]; st1=''
    l2=dp(l1)
    for i in range(1,2):
        for ch in l2:
            if i==1:
                d1[ch]=ch+str(i)
            l3.append(chr(ord(ch)+1))
            l4.append(l2.index(ch))
            listCheck.append(ch)
        l5=[k for k in zip(l3,l4) if k[0] not in l1]
    # print("l5 at end of 1st iteration: ", l5)        
    # print("List check keys", listCheck)
    while len(l5) >= 1:
        l3=[]; l4=[]
        for ch in l5:
            # print(ch[0], type(ch[0]))
            if ch[0] in string.ascii_lowercase:
                # print(d1.keys())
                if ch[0] not in d1.keys():
                    d1[ch[0]]=l1[ch[1]]+str(j)
                    # print("test1")
                    # print("ch[0]", ch[0])
                    # chNew=char_incr(ch[0])
                    # print("chNew", chNew)
                    # print("test2")
                    l3.append(char_incr(ch[0]))
                    l4.append(ch[1])
                    listCheck.append(ch[0])
                    # print("l3 in while", l3)
                    # print("l4 in while", l4)
        l5=[k for k in zip(l3,l4) if k[0] not in l1]
        # print("l5 inside while", l5)
        # print(d1)
        j+=1
    print("dict", d1)
    for ch in message:
        st1+=d1[ch]
    return st1
