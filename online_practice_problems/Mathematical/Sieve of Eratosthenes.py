# Given a number N, calculate the prime numbers up to N using Sieve of Eratosthenes.  
# hint: Run a loop from 2 till sqrt of N considering every number as prime and mark the multiple of 2 as not prime. Then select next number which is prime then again marked its multiple as not prime.
class Solution:
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