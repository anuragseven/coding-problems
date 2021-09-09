# You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).
def addFraction(num1, den1, num2, den2):


    numx=num1*den2+num2*den1
    denx=den1*den2
    hcf=gcd(numx,denx)
    
    numx=numx//hcf
    denx=denx//hcf
    
    print('{0}/{1}'.format(numx,denx))
    
def gcd(A,B):
    if A==0:
        return B
    
    return gcd(B%A,A)