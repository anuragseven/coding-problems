# Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        
        
        stack=[]
        closeBr=[')','}',']']
        for i in range(len(x)-1,-1,-1):
            br=x[i]
            if br in closeBr:
                stack.append(br)
            
            else:
                if stack==[]:
                    return False
                if br=='(' and stack.pop()!=')':
                    return False
                if br=='{' and stack.pop()!='}':
                    return False
                if br=='[' and stack.pop()!=']':
                    return False
        if stack==[]:
            return True
        else:
            return False