# The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.


class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        result=[]
	    
	currBuyingDay=0
	currSellingDay=0
	    
	for i in range(1,n):
	    if A[i]>A[currSellingDay]:
	        currSellingDay=i
	        
	    else:
	        if currBuyingDay<currSellingDay:
	            result.append([currBuyingDay,currSellingDay])
	        currBuyingDay=i
	        currSellingDay=i
	            
	    
	if currSellingDay>currBuyingDay:
	    result.append([currBuyingDay,currSellingDay])
	    
	return result