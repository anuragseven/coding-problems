# Armstrong Number
class Solution:
    def armstrongNumber (self, N):
        arr=[]
        n=N
        while n!=0:
            digit=n%10
            arr.append(digit)
            n=n//10
        
        if (arr[0]**3)+(arr[1]**3)+(arr[2]**3) ==N:
            return 'Yes'
        return 'No'