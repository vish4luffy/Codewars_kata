# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 23:47:32 2018

@author: Gireesh
"""

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

def nb_year(p0, percent, aug, p):
    """
    p0 - population at the beginning of a year
    percent - popn increase percentage
    aug - inhabitants coming or leaving each year
    p - target population
    """
    n=0
    while(p0 < p):
        p0+=(percent*(p0/100) + aug)
        n+=1
#        print('popn increased to: ', p0)
#        print('No: of years: ', n)
    return n

test1 = nb_year(1500, 5, 100, 5000)
print(test1)