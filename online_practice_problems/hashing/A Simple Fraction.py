# Given a fraction. Convert it into a decimal. 
# If the fractional part is repeating, enclose the repeating part in parentheses.

class Solution:
	def fractionToDecimal(self, num, den):
	    integerPart=num//den
	    
	    d={}
	    rem=num%den
	    
	    result=''
	    while rem!=0 and rem not in d:
	        d[rem]=len(result)
	        rem*=10
	        result+=str((rem//den))
	        rem=rem%den
	        
	    
	    if rem==0:
	        if result=='':
	            return integerPart
	        return str(integerPart)+'.'+result
	    
	    elif d[rem]==0:
	        return str(integerPart)+'.('+result+')'
            else:
                return str(integerPart)+'.'+result[0:d[rem]]+'('+result[d[rem]:]+')'