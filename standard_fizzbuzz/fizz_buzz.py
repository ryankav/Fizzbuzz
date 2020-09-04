# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:22:24 2020

@author: Ryan Kavanagh
"""

def fizzbuzz(rules, num, base=10):
    
    keys = [i for i in rules]
    keys.sort()
    
    for i in range(1,num+1):
        string = ''
        for key in keys:
            if 0 == i%key:
                string += rules[key]
        
        if string:
            print(string)
        else:
            print(i)

if __name__ == '__main__':
    
    rules = {3 : 'Fizz', 5 : 'Buzz'}
    num = 50
    fizzbuzz(rules, num)