#Given an input stream of A of n characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. If there is no such character then append '#' to the answer.

from collections import OrderedDict
class Solution:
	def FirstNonRepeating(self, A):
		S=set()
		d=OrderedDict()
		result=''
		for c in A:
		    if c not in S:
		        S.add(c)
		        d[c]=None
		        
		        result+=list(d.keys())[0]
		        
		    else:
		        if c in d:
		            del d[c]
		            
		        if len(d)==0:
		            result+='#'
		        else:
		            result+=list(d.keys())[0]
	    return result