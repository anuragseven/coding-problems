# Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.

#Two strings are called K-anagrams if both of the below conditions are true.
#1. Both have same number of characters.
#2. Two strings can become anagram by changing at most K characters in a string.
def areKAnagrams(str1, str2, k):
    if len(str1)!=len(str2):
        return False
    
    chars=[0]*128
    commons=0
    for c in str1:
        chars[ord(c)]+=1
    
    for c in str2:
        if chars[ord(c)]>0:
            chars[ord(c)]-=1
            commons+=1
    
    
    return k>=(len(str1)-commons)