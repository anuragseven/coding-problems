# Find all pairs (sets) of prime numbers (p,q) such that p*q <= n, where n is given number.


class Solution1:
	def prime_pairs(self, n):
	    primes=self.sieveOfEratosthenes(n)
	    
	    result=[]
	    
	    for num in primes:
	        l=0
	        
	        
	        while primes[l]*num<=n:
	            result.append(num)
	            result.append(primes[l])
	            
	            l+=1
	    return result
	    
	def sieveOfEratosthenes(self, N):
            primes=[True for i in range(N+1)]
        
            for i in range(2,int(N**0.5)+1):
                if primes[i]==True:
                    for j in range(i*i,N+1,i):
                        primes[j]=False
        
            result=[]
            for i in range(2,N+1):
                if primes[i]:
                    result.append(i)
                
            return result