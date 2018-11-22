#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 08:59:25 2018

5 Kyu - Hamster Me Kata

@author: gireesh
"""

# hamsterMe('hamster', 'hamster')   => h1a1m1s1t1e1r1
# hamsterMe('hamster', 'helpme')    => h1e1h5m4m1e1

from collections import OrderedDict as od
from copy import deepcopy as dp
# from string import ascii_lowercase
import string
def hamster_me(code, message):
    l1=[ch for ch in "".join(od.fromkeys(code))]
    # print(code)
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
    # print(l2)
    # print("l5 at end of 1st iteration: ", l5)        
    # print("List check keys", listCheck)
    while len(l5) >= 1:
        l3=[]; l4=[]
        for ch in l5:
            if ch[0] in string.ascii_lowercase:
                if ch[0] not in d1.keys():
                    d1[ch[0]]=l1[ch[1]]+str(j)
                    l3.append(chr(ord(ch[0])+1))
                    l4.append(ch[1])
                    listCheck.append(ch[0])
        l5=[k for k in zip(l3,l4) if k[0] not in l1]
        # print(d1)
        j+=1
    for ch in message:
        st1+=d1[ch]
    # print(st1)
    return st1
    # return message
        # print("l5 at end of iteration", l5)
#         if l5[0][0] in d1.keys():
            # break
print(hamster_me('hamster', 'helpme'))
        