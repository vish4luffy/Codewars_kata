#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:05:45 2018

@author: gireesh
"""

# Prize Draw Kata

# Test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")

# Test.assert_equals(rank("Lagon,Lily", [1, 5], 2), "Lagon")

# Test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), 
# "Not enough participants")

# Test.assert_equals(rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participants")

#Task:
# =============================================================================
# 
# parameters: st a string of firstnames, we an array of weights, n a rank
# 
# return: the firstname of the participant whose rank is n (ranks are numbered from 1)
# 
# #Example: names: COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH weights: [1, 4, 4, 5, 2, 1] n: 4
# 
# The function should return: PauL
# 
# #Note: If st is empty return "No participants".
# 
# If n is greater than the number of participants then return "Not enough participants".

# Example: 
# PAUL -> n = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54 
# The weight associated with PAUL is 2 so Paul's winning number is 54 * 2 = 108.
#
# Now one can sort the firstnames in decreasing order of the winning numbers. 
# When two people have the same winning number sort them alphabetically by their firstnames.
# =============================================================================

# Convert input string to lowercase
# have a dict for score of each alphabet from a - z
# Then, calc rank by adding length of word + score of each letter and then multiplying by weight
# Then store them in a list of tuples and sort them by names with descending ranks and 
# in case of same rank, sort them 
# alphabetically
# Then display only the first name for a specific rank that is being asked in the problem


def rank(st, we, n):
    if st=="":
        return "No participants"
    else:
        nameScore1=[]; nameDict1={}
        st1=st.lower().split(',')
        # print(st1)
        scoreLetter={chr(i+96):i for i in range(1, 27)}
        for name in st1:
            score=0
            for letter in name:
                score+=scoreLetter.get(letter,0)
            nameScore1.append([name, score])
        if n>len(st1):
            return "Not enough participants"
        elif len(st1)==len(we):
            nameDict1=dict(nameScore1)
            for i in st1:
                nameDict1[i]+=len(i)
            nameWeights=dict(zip(st1, we))
            nameDict2={k: v*nameWeights[k] for k, v in nameDict1.items() if k in nameWeights}
            # nameDict3={key: rank for rank, key in enumerate(sorted(nameDict2, key=nameDict2.get, reverse=True), 1)}
            # nameDict3=nameDict2.sort(key=lambda x: (int(x[0]), x[1]), reverse=True)
            # nameDict3 = {k:v for k,v in sorted(nameDict2.items(), key=lambda(k,v): (-v,k))}
            nameFinal=[(k,v) for k,v in sorted(nameDict2.items(), key=lambda kv: (-kv[1], kv[0]))]
            return nameFinal[n-1][0].title()

# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
print(rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    