#User function Template for python3
from math import factorial as fact
#Count pairs with given sum 
class Solution:
    def getPairsCount(self, arr, n, k):
        counts={}
        for num in arr:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
                
        count=0
        for num in arr:
            
            if k-num==num: 
                if counts[num]>1 :
                    count+=int(self.combinations(counts[num],2))
                    counts[num]=0
            
            elif k-num in arr and counts[num]>0:
                count+=counts[k-num]*counts[num]
                counts[num]=0
                counts[k-num]=0
        return count
                
                
                
    def combinations(self,n, r):
 
        return (fact(n) / (fact(r)
                    * fact(n - r)))



#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        counts={}
        for num in arr:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
                
        count=0
        for num in arr:
            
            if k-num==num: 
                
                    count-=1
                    
            
            if k-num in arr:
                count+=counts[k-num]
                
        return int(count/2)