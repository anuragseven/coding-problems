#User function Template for python3
class Solution:
    def getDayOfWeek(self, d: int, m: int, y: int):
        days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
        y -= m < 3
        
        return days[(( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)]
