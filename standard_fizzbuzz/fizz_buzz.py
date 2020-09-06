# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:22:24 2020

@author: Ryan Kavanagh
"""
import string

def num_in_base(num, base, chars):
    '''
    A function that prodeces a string representing a given number in the base 
    passed.
    
    Parameters:
        num: Positive integer to be converted
        
        base: Integer less than 62. That will be the base.
        
    Returns:
        String: containing symbols that represent the number in a different base
    '''
    out = ""
    while num:
        rem = num % base
        out = chars[rem] + out
        num//=base
    
    if out:
        return out
    else:
        return 0

def fizzbuzz(rules, ran, base):
    '''
    Prints out the correct numbers for the game fizzbuzz
    
    Parameters:
        
        rules: dictionary contianing integer keys and string values.
        
        ran: Integer which contains the number to loop up to
        
        base: Integer greater than equal to 2. That is the base you would like 
            to see the numbers printed out in
    
    returns: None
    '''
    if not 1<base<62:
        print("Invalid base")
        return
    if ran<1:
        print("Invalid range")
        return
        
    base_char = f"{string.digits}{string.ascii_uppercase}{string.ascii_lowercase}"
    keys = [i for i in rules]
    keys.sort()
    
    for i in range(1,ran+1):
        out = ''
        for key in keys:
            if 0 == i%key:
                out += rules[key]
        
        if out:
            print(out)
        else:
            print(num_in_base(i, base, base_char))

if __name__ == '__main__':
    
    rules = {3 : 'Fizz', 5 : 'Buzz'}
    ran= 50
    base = 9
    fizzbuzz(rules, ran, base)