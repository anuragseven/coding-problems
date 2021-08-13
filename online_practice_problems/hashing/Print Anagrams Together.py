# Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    anagrams={}
    for word in words:
        anagramKey=getAnagramKey(word)
        if anagramKey in anagrams:
            anagrams[anagramKey].append(word)
        else:
            anagrams[anagramKey]=[word]
            
    result=[]    
    for group in anagrams.values():
        result.append(group)
    
    return result
        
    
def getAnagramKey(s):
    chars=[0]*128
    for c in s:
        chars[ord(c)]+=1
    
    result=''
    for i in range(len(chars)):
        if chars[i]>0:
            result+=chr(i)+str(chars[i])
    return result