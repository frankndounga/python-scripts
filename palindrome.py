#!/usr/bin/env python

#Recommandation of this version of palindrome checking
#assume that an empty string isn't a palindrome;
#treat upper- and lower-case letters as equal; 
#spaces are not taken into account during the check – treat them as non-existent;
#there are more than a few correct solutions – try to find more than one.

def check_if_palindrome(word):
    # do not consider an empty string
    if word == '':
        return "It's not a palindrome"
    # i first remove all spaces in the given word and choose a case to evaluate the string either lower or upper
    remove_space_word = "".join([x for x in word if x.isalnum()]).lower()
    # just to check the result
    print(remove_space_word)
    
    reversed_word = remove_space_word[::-1] #reversed_word = ''.join(reversed(remove_space_word))

    return "It's a palindrome" if reversed_word == remove_space_word else "It's not a palindrome"


if __name__ == '__main__':
    word_to_check = input("Enter the word you want to check: ")
    print(check_if_palindrome(word_to_check))
