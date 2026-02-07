#!/usr/bin/env python

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
