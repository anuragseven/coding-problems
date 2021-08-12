# The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.


def stockBuySell(self, A, n):
	    
		
		minIndex=0
		maxIndex=0
		maxProfit=0
		
		for i in range(n):
		    
		   
		    if A[minIndex]>A[i]:
		        minIndex=i
		    
		    if maxProfit < A[i]-A[minIndex]:
		        maxProfit=A[maxIndex]-A[minIndex]
		        maxIndex=i
	    
	    return [minIndex,maxIndex] if maxProfit!=0 else []