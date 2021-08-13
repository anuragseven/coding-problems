# Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.
def remAnagram(str1,str2):
    
    chars=[0]*128
    for c in str1:
        chars[ord(c)]+=1
    
    for c in str2:
        chars[ord(c)]-=1
        
    
    
    count=0
    
    for cou in chars:
        count+=abs(cou)
    return count