#Given a N x N matrix M. Write a program to find count of all the distinct elements common to all rows of the matrix. Print count of such elements.

def distinct(self, M, N):
        
        
        s=set(M[0])
        
        for i in range(1,len(M)):
            temp=set(M[i])
            s=s.intersection(temp)
        return len(s)