# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise). 

# Input:
# The first line of the input contains T denoting the number of testcases. First line of each test case contains two space separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent line will be the N space separated array elements.

def rotateArray(arr,k):
    k=k%len(arr)
    reverse(arr,0,k-1)
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,len(arr)-k-1)
    return arr
    
    
def reverse(arr,i,j):
    
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
        


t=int(input())

for i in range(t):
    k=int(input().split(' ')[1])
    
    arr=[int(c) for c in input().split(' ') if c!='']
    result=rotateArray(arr,k)
    print(*result)