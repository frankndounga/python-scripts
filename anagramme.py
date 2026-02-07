#!/usr/bin/env python

#An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.


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

print(anagramme('rail safety', 'faiRy tales'))

