# Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1 to N.

def frequencyCount(self, arr, N, P):
        
        temp=[0]*N
        
        for num in arr:
            if num<=len(arr):
                temp[num-1]+=1
        
        for i in range(len(arr)):
            arr[i]=temp[i]