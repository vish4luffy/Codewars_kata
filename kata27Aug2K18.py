#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:50:59 2018

@author: gireesh
"""

def diamond(n):
    x=1; y=n//2; z=n-2; # variables for '*' counter
    sp1=''; y2=n//2; y3=1; # variables for printing whitespaces
    lstIn=[]
    if (n%2==0) or (n<0):
        return None
    for i in range(n): # outermost loop
        # lstIn=[]
        if(i<=n//2):   # till printing n '*'
            d1=''; d2=''; # for printing '*'
            if(y2>0):
                sp1=y2*' '
                # print(sp1, end='')
            for j in range(x):
                d1+='*'
            if(y2>0):
                lstIn.append(sp1+d1+'\n')
            elif(y2==0):
                lstIn.append(d1+'\n')
            # print(d1, end='\n')    
            x+=2
            y2-=1
        else:          # for printing remaining rows when n decreases 
            sp1=y3*' '
            # print(sp1, end='')
            y3+=1
            d2=z*'*'
            y-=1
            z-=2
            lstIn.append(sp1+d2+'\n')
            # print(d2)
        # lstOut.append(lstIn)
    return ''.join(lstIn)

print(diamond(5))