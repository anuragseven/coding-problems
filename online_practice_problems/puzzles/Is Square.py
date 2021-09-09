# Given four different points in space. Find whether these points can form a square or not.

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Solution:
    
    def isSquare(self, x1, y1, x2, y2, x3, y3, x4, y4):
    
        r1=self.isSquareHelper( x1, y1, x2, y2, x3, y3, x4, y4) 
        r2=self.isSquareHelper(x1, y1, x3, y3, x2, y2, x4, y4)
        
        return 'Yes' if r1 or r2 else 'No'
        
    def isSquareHelper(self, x1, y1, x2, y2, x3, y3, x4, y4):
        A=Point(x1,y1)
        B=Point(x2,y2)
        C=Point(x3,y3)
        D=Point(x4,y4)
        
         
        
        AB=self.distanceSq(A,B)
        BC=self.distanceSq(B,C)
        CD=self.distanceSq(C,D)
        AC=self.distanceSq(A,C)
        BD=self.distanceSq(B,D)
        c1=False
        c2=False
        
        if AB==0 or BC==0 or CD==0 :
            return False
        
        if AB==BC and BC==CD:
            c1=True
        
        if AC==(2*AB) and BD==(2*BC):
            c2=True
        
        
        return c1 and c2 
        
    
    def distanceSq(self,a,b):

        X=(a.x-b.x)**2
        Y=(a.y-b.y)**2
        return (X+Y)