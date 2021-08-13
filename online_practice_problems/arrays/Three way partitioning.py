#Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.
#The individual elements of three sets can appear in any order. You are required to return the modified array.


def threeWayPartition(self, array, a, b):
	    array.append(a)
	    i=self.sortAroundNum(array,0,len(array)-1)
	    array.append(b)
	    self.sortAroundNum(array,i,len(array)-1)
	    
	     
	     
	     
	
	   
    def sortAroundNum(self,a, p, r):
        
        x=a[r]
        i = p - 1
        for j in range(p, r):
            if a[j] <= x:
                i = i + 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[r] = a[r], a[i + 1]
        a.remove(a[i+1])
        return i 


def threeWayPartition(arr, n, lowVal, highVal):
 
    # Initialize ext available positions for
    # smaller (than range) and greater lements
    start = 0
    end = n - 1
    i = 0
 
    # Traverse elements from left
    while i <= end:
 
        # If current element is smaller than
        # range, put it on next available smaller
        # position.
        if arr[i] < lowVal:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1
 
        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1
 
        else:
            i += 1