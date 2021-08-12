# Given an array of names (consisting of lowercase characters) of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidate that received Max votes. If there is tie, print lexicographically smaller name.

def winner(self,arr,n):
        namesCount={}
        for name in arr:
            if name in namesCount:
                namesCount[name]+=1
            else:
                namesCount[name]=1
        
      
        maxCount=0
        winner='zzzzzzzzzzzzzz'
        
        for name in namesCount.keys():
            if namesCount[name]>maxCount:
                maxCount=namesCount[name]
                winner=name
            elif namesCount[name]==maxCount:
                if name<winner:
                    winner=name
                    
            
         
        return [winner,maxCount]