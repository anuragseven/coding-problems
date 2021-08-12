#Jarvis is weak in computing palindromes for Alphanumeric characters.
#While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
#You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
#If you are unable to solve it then it may result in the death of Iron Man.

import string
def saveIronman (s) : 
    validChars=[str(i) for i in range(10)]+list(string.ascii_lowercase)
    s=s.lower()
    
    j=len(s)-1
    i=0
    while i<=j:
        continueFlag=False
        if s[i] not in validChars :
            i+=1
            continueFlag=True
        if s[j] not in validChars:
            j-=1
            continueFlag=True
        if continueFlag:
            continue
            
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True