# Minimum Window Substring

class Solution:
    def minWindow(self, s: str, p: str) -> str:
        if len(p)>len(s):
            return ''
        pchars={}
        for c in p:
            if c in pchars:
                pchars[c]+=1
            else:
                pchars[c]=1
        
        
        count=0
        results=[]
        schars={}
        j=0
        for i in range(len(s)):
            if s[i] in schars:
                schars[s[i]]+=1
                
            else:
                schars[s[i]]=1
            if s[i] in pchars:
                    if schars[s[i]]<=pchars[s[i]]:
                        count+=1
            
            if count==len(p):
                results.append(s[j:i+1])
                
                
                while j<=i:
                    if s[j] not in pchars:
                        schars[s[j]]-=1
                        j+=1
                    elif schars[s[j]]>pchars[s[j]]:
                        schars[s[j]]-=1
                        j+=1
                    else:
                    
                        results.append(s[j:i+1])
                        count-=1
                        schars[s[j]]-=1
                        j+=1
                        break
        if len(results)==0:
            return ''
        minLength=len(s)
        finalResult=[]
       
        for result in results:
            minLength=min(minLength,len(result))
        
        for result in results:
            if len(result)==minLength:
                return result
        
