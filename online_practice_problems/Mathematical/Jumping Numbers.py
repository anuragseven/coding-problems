# Given a positive number X. Find the largest Jumping Number smaller than or equal to X. 
# Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

class Solution:
    def jumpingNums(self, X):
        result=[]
        for i in range(1,10):
            self.bfs(X,i,result)
        return max(result)
    
    def bfs(self,X,num,result):
        q=[]
        q.append(num)
        while q!=[]:
            num=q.pop(0)
            
            if num<=X:
                result.append(num)
                lastDigit=num%10
                
                if lastDigit==0:
                    q.append(num*10+lastDigit+1)
                
                elif lastDigit==9:
                    q.append(num*10+lastDigit-1)
                
                else:
                    q.append(num*10+lastDigit-1)
                    q.append(num*10+lastDigit+1)