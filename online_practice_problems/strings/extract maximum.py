#Given a alphanumeric string S, extract maximum numeric value from S.
def extractMaximum(self,S): 
        maximum=-1
        nums=[str(i) for i in range(10)]
        cnum=''
      
        for c in S:
            if c in nums:
                cnum+=c
                
            else:
                if cnum!='':
                    maximum=max(maximum,int(cnum))
                cnum=''
        if cnum!='':
            maximum=max(maximum,int(cnum))
            
        return maximum