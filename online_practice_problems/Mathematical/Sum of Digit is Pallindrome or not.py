# Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
# Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.

class Solution:
    def isDigitSumPalindrome(self,N):
        S=0
        
        while N!=0:
            d=N%10
            S+=d
            N=N//10
        
        return 1 if str(S)==(str(S)[::-1]) else 0