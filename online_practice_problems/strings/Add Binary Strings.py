#Given two binary strings A and B consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
#Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

def addBinary(self, A, B):
	    
	    a=self.convertToDecimal(A)
	    b=self.convertToDecimal(B)
	    
	    return self.convertToBinary(a+b)
	    
		
	
	
	def convertToDecimal(self,s):
	    result=0
	    
	    l=len(s)-1
	    
	    for c in s:
	        if c=='1':
	            result=result+2**l
	        l-=1
	    return result
	
	def convertToBinary(self,s):
	    s=int(s)
	    if s==0:
	        return 0
	    result=''
	    while s!=0:
	        result+=str(s%2)
	        s=s//2
	    return result[::-1]

class Solution:
	def addBinary(self, A, B):
	    B=self.removeTrailingZeroes(B)
	    A=self.removeTrailingZeroes(A)
	    result=''
	    i=len(A)-1
	    j=len(B)-1
	    carry='0'
	    tz=abs(j-i)
	    if j>i:
	        
	        while tz!=0:
	            A='0'+A
	            tz-=1
	    else:
	        while tz!=0:
	            B='0'+B
	            tz-=1
	    i=len(A)-1
	    while i>=0: 
	        if A[i]=='0' and B[i]=='0':
	            if carry=='1':
	                result+='1'
	                carry='0'
	            else:
	                result+='0'
	        elif A[i]=='1' and B[i]=='1':
	            if carry=='1':
	                 result+='1'
	            else:
	                result+='0'
	                carry='1'
	        else:
	            if carry=='1':
	                result+='0'
	            else:
	                result+='1'
	        
	        i-=1
        result=result[::-1]
        
	    if carry=='1':
	        result='1'+result
	    return result
    
    def removeTrailingZeroes(self,s):
        j=0
        for i in range(len(s)):
            if s[i]=='1':
                break
            j+=1
        return s[j:]
