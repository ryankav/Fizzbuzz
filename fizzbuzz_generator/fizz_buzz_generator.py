# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:36:55 2020

@author: Ryan Kavanagh
"""
import os
import sys
from itertools import combinations as combinations 
#import re

# add rules in here. It is assumed that the user will not enter
# malicious values as this is just for fun. May edit later to prevent
#malicious use.

#REPLACEMENTS must not contain a key which is divisible by a differnet key.
#Keys must be positive and non-zero (preferably not 1 either)

REPLACEMENTS = {3:'Fizz', 5:'Buzz', 7:'Fun'}
NUM=50

if __name__=="__main__":
    
    
    #check to see if REPLACEMENTS has been populated
    if len(REPLACEMENTS)==0:
        sys.exit("No replacements defined")
# =============================================================================
#     #replace all non-aplhanumeric characters in values    
#       
#     for key in REPLACEMENTS:
#         REPLACEMENTS[key] = re.sub('[^0-9a-zA-Z]+','',REPLACEMENTS[key])
#         
#         
# =============================================================================
    keys=list(REPLACEMENTS.keys())
    keys.sort()

    val=1
    string=''
    
    #need rules to be in descending order to ensure correct output
    
    for key in keys:
        val *= key
        
        if(not string):
            string = REPLACEMENTS[key]
        else:
            string+=" " + REPLACEMENTS[key]
            
    name = string.replace(" ", "_")
    name+='.py'
    
    solution=f"def foo(num):\n\tfor i in range(1,num+1):\n\t\tif(i%{val}==0):\n\t\t\tprint('{string}')"
    
    ran=range(len(REPLACEMENTS))
    
    #make tuples containing all possible combinations of rules
    
    for i in range(len(REPLACEMENTS)-1,0,-1):
        combos = combinations(ran,i)
        
        string="\n\t\telif(i%{}==0):\n\t\t\tprint('{}')"
        
        for combo in combos:
            val=1
            sub_string=""  
            for index in combo:
                current = keys[index]
                val*=current
                if(not sub_string):
                    sub_string=REPLACEMENTS[current]
                else:
                    sub_string+=" " + REPLACEMENTS[current]
            
            solution+=string.format(val,sub_string)
    
    solution+=f"\n\t\telse:\n\t\t\tprint(i)\nif __name__=='__main__':\n\tnum={NUM}\n\tfoo(num)"
    
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"output")
    os.makedirs(path, exist_ok = True)
    
    with open(os.path.join(path,name),"w") as file:
        
        file.write(solution)
            
        
 
    
    

