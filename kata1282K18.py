# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:21:42 2018

@author: Gireesh
"""
import re

def move_zeros(array):
    d2={}; l2=[]; ct=0
    for i, v in enumerate(array):
        d2[i]=v
    for k,v in d2.items():
        if v!=0 or v is False:# and v is not False:
            l2.append(v)
        else:
            ct+=1                        
    for num in range(ct):
        l2.append(0)
    return l2

# print(move_zeros([0,1,None,2,False,1,0])) 
    # ,[1,None,2,False,1,0,0]
    # returns[false,1,1,2,1,3,"a",0,0]

# a1=[False,1,0,1,2,0,1,3,"a"]
# print(a1.pop(0))
    
def count_smileys(arr):
    arr1=''.join(arr)
    l4=re.findall("[:;]{1}[-~]{0,1}[)D]{1}",arr1)
    return len(l4)

# print(count_smileys([';D', ':-(', ':-)', ';~)']))
#;       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

def tower_builder(n_floors):
    n=1; x=n_floors-1; y=n_floors-1; lst1=[];
    for i in range(n_floors):
        k=x; l=y; k1=''; k2=''; k3=''; lst2=[]; 
        while(k>0):
            k1+=' ' # print(' ', end='')
            k-=1
        lst2.append(k1)
        for j in range(n):
            k2+='*' # print('*', end='')
        lst2.append(k2)
        while(l>0):
            k3+=' ' # print(' ', end='')
            l-=1
        lst2.append(k3) # print('\n')
        n+=2
        x-=1
        y-=1
        lst1.append(''.join(lst2))
    return lst1

# =========================check the below solution out!=======================
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
# =============================================================================
# def tower_builder(n_floors):
#     if n_floors == 0:
#         return []
#         
#     count = 1
#     result = []
# 
#     for i in range(1, n_floors + 1):
#       stars = '*' * (2 * i - 1)
#       space = ' ' * (n_floors - i)
#       result.append(space + stars + space)
#     
#     return result
# =============================================================================
# =============================================================================
def tower_builder2(n_floors):
    n=1; x=n_floors-1; y=n_floors-1;
    for i in range(n_floors):
        k=x; l=y; 
        while(k>0):
            print(' ', end='')
            k-=1
        for j in range(n):
            print('*', end='')
        while(l>0):
            print(' ', end='')
            l-=1
        print('\n')
        n+=2
        x-=1
        y-=1

print(tower_builder(6))

# =============================================================================
# for example, a tower of 3 floors looks like below
# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
# 
# and a tower of 6 floors looks like below
# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]
# 
# =============================================================================
