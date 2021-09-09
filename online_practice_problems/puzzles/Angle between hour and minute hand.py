# Calculate the angle between hour hand and minute hand.

# Note: There can be two angles between hands, we need to print minimum of two. Also, we need to print floor of final result angle. For example, if the final angle is 10.61, we need to print 10.

from math import floor

class Solution:
    def getAngle(self, H , M):
        
        # angle between 12 and hour hand

        a1=H*5*6+M*0.5

        # angle between 12 and minute hand 

        a2=M*6
        
        diff=abs(a1-a2)
        
        return floor(min(diff,360-diff))