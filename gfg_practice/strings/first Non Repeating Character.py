# Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.
from collections import OrderedDict
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        chars=OrderedDict()
        
        for c in s:
            if c in chars:
                chars[c]+=1
            else:
                chars[c]=1
        
        for c in chars.keys():
            if chars[c]==1:
                return c
        
        return '$'