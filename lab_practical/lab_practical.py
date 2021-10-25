import os 
import itertools
import re

def get_list_of_divisors(n):
    #Used for Solution
    list_of_divisors = []
    for i in range(1,n):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

def get_string_concordence(s):
    #Use for Solution
    '''precondition: lowered string'''
    s = s.strip()
    concordence_dict = {}
    for char in s:
        if char not in concordence_dict.keys():
            concordence_dict[char] = 1 
        elif char in concordence_dict.keys():
            concordence_dict[char] += 1  
    return concordence_dict

###################Problem 1##############################
def countWords(s):
    #Solved
    """
        countWords("I eat cake") -> 3
        countWords("0") -> 1
        countWords("To be or not to be, that is the question.") -> 10"""
    s = s.strip().split(" ")
    return len(s)

###################Problem 2##############################
def checkFileForWord(fileName, word):
    #Solved
    """
    fileName is a string
    if the file does not exist, return False
    if the file does exist, check for word being a
    substring of the file; if you find it return True and 
    return False otherwise"""
    if not os.path.exists(fileName):
        return False
    else:
        file_input = open(fileName,'r')
        for line in file_input.readlines():
            if word in line:
                return True
        file_input.close()
    return False
        
    
    
###################Problem 3##############################
def weaveStrings(s,t):
    #Solved
    """ weaveStrings("cat", "dog") -> "cdaotg"
        weaveStrings("nasty", "cow") -> "ncaowty"
        weaveStrings("cosmic", "eat") -> "ceoamtic"  """
    s = list(s) 
    t = list(t)
    n = 1
    for obj in t:
        s.insert(n, obj)
        n += 2
    word = ""
    for obj in s:
        word += obj
    return word
        
    
###################Problem 4##############################
def areAnagrams(s,t):
    #Solved
    """ s and t are strings
        return True if s and t are anagrams, case INSENSITIVE
        areAnagrams('space', 'Capes') -> True
        areAnagrams('spatter', 'parsers') -> False
        areAngrams('dog', 'log') -> False"""
    s, t = s.lower(), t.lower()
    s_concordence_dict, t_concordence_dict = get_string_concordence(s), get_string_concordence(t)
    return (s_concordence_dict == t_concordence_dict)

###################Problem 5##############################
def isPerfectNumber(n):
    #Solved
    """
        n is a positive integer and n >= 2
        n is perfect if it is the sum of its proper divisors.
        6 has proper divisors 1,2,3 so isPerfectNumber(6) -> True
        12 has proper divisors 1,2,3,4,6, which sum to 22,
        so isPerfectNumber(12) -> False
        Hint: You might want to write a helper function 
        sumOfProperDivisors(n)
    """
    return sum(get_list_of_divisors(n)) == n
###################Problem 6##############################
def containsEmbeddedWord(word, searchField):
    """
    word is a string of letters 
    searchField is a string
    returns True if the letters in word can be found in 
    order in the string searchField.  This is case-insensitive
    containsEmbeddedWord("abcd, "abcessed") -> True
    containsEmbeddedWord("foot, "flounder of trust") -> True
    containsEmbeddedWord("dequeue", "defend the queen") -> False"""
    word, searchField = word.lower(), searchField.lower()
    word_counter = 0
    truthiness = [] ; x = True
    for check in searchField:
        if word_counter == len(word):
            break
        if check == word[word_counter]:
            truthiness.append(x)
            word_counter += 1
    if len(truthiness) != len(word):
        return False 
    else:
        return True



    
    

