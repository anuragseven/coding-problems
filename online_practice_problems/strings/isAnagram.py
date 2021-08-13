 def isAnagram(self,a,b):
        if len(a)!=len(b):
            return False
        chars=[0]*128
        
        for i in range(len(a)):
            
            chars[ord(a[i])]+=1
            chars[ord(b[i])]-=1
        
        
        for count in chars:
            if count!=0:
                return False
        return True