# Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

# Note: It may be assumed that the rectangles are parallel to the coordinate axis.
# image: https://www.geeksforgeeks.org/wp-content/uploads/rectanglesOverlap.png
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Returns true if two rectangles(l1, r1)
class Solution:
    def doOverlap(self,l1, r1, l2, r2):
     
   
        l1 =Point(l1[0],l1[1])
        l2=Point(l2[0],l2[1])
        r1=Point(r1[0],r1[1])
        r2=Point(r2[0],r2[1])
       
       
     
    
        if(l1.x > r2.x or l2.x > r1.x):
            return 0
 
    
        if(r1.y > l2.y or r2.y > l1.y):
            return 0
 
        return 1