# Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. You are given a number N, you have to output the number of integers less than N in the sample space S.

from math import ceil
class Solution:
    def countSquares(self, N):
        return ceil(N**0.5)-1