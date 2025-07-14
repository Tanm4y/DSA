def easy_longest_word(string):
    count = 0 
    maximum = 0 
    for char in string :
        if char.isalnum():
            count +=1
        else:
            maximum = max(maximum , count)
            count = 0 
        maximum = max(maximum , count)
        return maximum 
    
    string = "kjsregkiawbk"
    print(easy_longest_word(string))


def naive_longest_word(string):
    count = 0 
    maximum = 0 
    words = 0 
    word = 0 
    for char in string :
        count += 1 
        word.append(char)
    else:
        if word not in words and word :
            words.append(''.join[word])
            print(words)
            print(word)
            word = []
        maximum = max(maximum,count)
        count = 0 
    maximum = max(maximum , count)
    if word not in words and word:
        word.append(''.join(word))
        print(words)
        print(word)
    for item in words :
        if len(item) == maximum :
            return item 
        
    print(naive_longest_word(string))


    #As can be seen, this has become a pretty complicated solution.
#We loop over every character and check if it is an alphanumeric character.
#If yes, we increase count by 1 and append the character to the word list.
#If not, we first check if the word which we have accumulated so far is their in the words list or not.
#If not, we convert the list word into a string using the join method and add the string to the words list
#If yes, then we ignore it. This is done so that same words are not added more than once in the words list
#Then we reset word to an empty list in anticipation of the next word and count to 0.
#This way by the end of the loop, words contains al the words in the string except for the last one, which we add manually after the for loop
#Finally, we check the length of which word is equal to the maximum value, which has been keeping track of the length of the longest word
#And we return the longest word, albeit only the first occurence , if there are more than one words with maximum length.

#The complexity is bad on all fronts. There is a join function used inside a for loop.
#Complexity of .join(string) is O(len(string)). So overall time complexity is O(mn)
#Also, two new arrays are created. So space complexity = O(m + n)


#A different method to solve this problem can be using Regex,or Regular Expressions
#First we split the string into groups of alphanumeric characters
#Then we find the maximum length among all the words
#Finally we find the word corresponding to the maximum length

import re
def regex(string):
    string = re.findall('\w+', string)
    maximum = max([len(item) for item in string])
    for item in string : 
        if len(item) == maximum :
            return item 
sss = "hello there how are you"
print(regex(sss))



