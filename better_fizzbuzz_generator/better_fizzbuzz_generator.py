# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:23:29 2020

@author: Ryan Kavanagh
"""
import os
import sys
#import re

#REPLACEMENTS can contain a key which is divisible by a differnet key with this
#implementation. Keys must be positive and non-zero (preferably not 1 either)

REPLACEMENTS = {3:'Fizz', 5:'Buzz'}
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
    
    name = ''
    for key in keys:
        name += REPLACEMENTS[key]
    name += '.py'
    
    start = f"def foo(num):\n\tfor i in range(1,num+1):\n\t\tstring = ''"
    
    arr = [0 for i in range(len(keys))]
    
    for i in range(len(keys)):
        arr[i] = f"\n\t\tif 0 == i%{keys[i]}:\n\t\t\tstring += {REPLACEMENTS[keys[i]]}"
        
    last = f"\n\tif string:\n\t\tprint(string)\n\telse:\n\t\tprint(i)\n"   
    
    end = f"\nif __name__=='__main__':\n\tnum={NUM}\n\tfoo(num)"
    
    solution = f"{start}{''.join(arr)}{last}{end}"
    
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"output")
    os.makedirs(path, exist_ok = True)
    
    with open(os.path.join(path,name),"w") as file:
        
        file.write(solution)