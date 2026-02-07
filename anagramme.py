#!/usr/bin/env python

#lighter version
def anagramme2(expression1, expression2):
    expression1 = "".join(sorted(list(expression1.replace(' ', '').lower())))
    expression2 = "".join(sorted(list(expression2.replace(' ', '').lower())))

    if expression1 == expression2:
        return "It is an anagram"
    else:
        return "It is not an anagram" 

#long version
def anagramme(expression1:str, expression2:str) -> bool:
    #if one expression is an empty string exit directly
    if expression1 == '':
        return False
    #remove spaces
    expression1 = expression1.replace(' ', '')
    expression2 = expression2.replace(' ', '')

    #check if both expressions have the same length after removing spaces if not it can't be an anagramme
    if len(expression1) != len(expression2):
        return False
    
    #check if every word in the expression1 is present in the expression2 with the same number of time if so, and al the length is already equal, it means same letters are in both expressions
    for letter in expression1:
        if not expression2.lower().count(letter) == expression1.lower().count(letter):
            return False
    else:
        return True
#test
print(anagramme2('rail safety', 'faiRy tales'))

