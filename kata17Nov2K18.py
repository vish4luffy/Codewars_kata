#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:28:49 2018

@author: gireesh
"""

# >: Move data selector right

# <: Move data selector left(infinite in both directions)

# +: Increment memory cell by 1. 255+1=0

# *: Add ascii value of memory cell to the output tape.

# test.assert_equals(interpreter('>>>>>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>+++++++++++++++++++++++++++++++++*'), 'Hello world!')
# 'Hello world!'
# H - ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>
# e - +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>
# l - ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*
# l - *>
# o - +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>
# space - ++++++++++++++++++++++++++++++++*>
# w - +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*
# o - <<*
# r - >>>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*
# l - <<<<*
# d - 
# ! - 

def interpreter(tape):
    word=""; ct=0; ct2=0; ct3=0;
    for ch in range(0, len(tape)):
    # for ch in tape:
        if tape[ch]=="+":
            ct+=1
        elif tape[ch]=="*":
            if ct2>0:
                # print("len(word)", len(word))
                # print("ct2 value", ct2)
                ct3+=1
                word+=word[len(word)-(ct2+ct3)]
                ct2=0
            else:
                word+=chr(ct%255)
        elif tape[ch]==">":
            ct=0
        elif tape[ch]=="<":
            # print("tapeCH", tape[ch])
            ct2+=1
                # ch+=1
                # print(ct2, ct)
    return word
    # print(word)
    
# =============================================================================
# def interpreter2(tape):
#     # Your code here
#     word=''
#     tapeList=tape.split("*")
#     print(tapeList)
#     # for each in tapeList:
#         # each.replace('>','')
#     tapeList = [w.replace('>', '') for w in tapeList]
#     for st in tapeList:
#         if '+' in st:
#             ct=st.count('+')
#             word+=chr(ct)
#         else:
#             word+=st
#     print('After removing >')
#     print(tapeList)
#     print(word)
#     
# =============================================================================
    
        
print(interpreter('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++**>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>++++++++++++++++++++++++++++++++*>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*<<*>>>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*<<<<*>>>>>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*>+++++++++++++++++++++++++++++++++*'))
