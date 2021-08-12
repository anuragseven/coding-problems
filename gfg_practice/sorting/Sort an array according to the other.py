# Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. Sort the first array A1[ ] such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ]

from collections import OrderedDict
class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    
    def relativeSort (self,A1, N, A2, M):
        counts={}
        
        nums=OrderedDict()
        for num in A2:
            nums[num]=None
        for num in A1:
            if num in counts:
                counts[num]+=1
            elif num in nums:
                counts[num]=1
        
        others=[]
        for num in A1:
            if num not in nums:
                others.append(num)
        others.sort()
        A1=[]
        for num in nums.keys():
            while counts[num]:
                A1.append(num)
                counts[num]-=1
        A1.extend(others)
        return A1