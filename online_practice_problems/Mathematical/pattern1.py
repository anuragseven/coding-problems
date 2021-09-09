'''
You a given a number N. You need to print the pattern for the given value of N.
for N = 2 the pattern will be 
2 2 1 1
2 1
for N = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
'''

def printPat(n):
    for j in range(n,1,-1):
        k=n
        while k:
            l=j
            while l:
                print(k,end='')
                l-=1
            k-=1
        print() 