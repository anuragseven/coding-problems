# Given a positive integer N, find the sum of all prime numbers between 1 and N(inclusive).


class Solution:
    def prime_Sum(self, n):
        primes=[True for i in range(n+1)]
		
	    for i in range(2,int(n**0.5)+1):
	        if primes[i]==True:
		    for j in range(i*i,n+1,i):
		        primes[j]=False
		
	S=0
		
	for i in range(2,n+1):
            if primes[i]:
	        S+=i
	return S