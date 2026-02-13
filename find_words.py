

eg = "Nabucodonosor"
word = 'donor'

def find_word(word_to_search, pattern):
    #initialise an index variable to keep the position for the beginning of the search for each loop on the word_to_search
    index = 0
    for i in range(len(word_to_search)):
        
        index = pattern.find(word_to_search[i], index) #each time i start to search in the beginning of the last end
        if index == -1:
            return 'No'
        print(index, word_to_search[i]) #just to test the order
    return 'Yes'

#exemple   
print(find_word(word, eg))