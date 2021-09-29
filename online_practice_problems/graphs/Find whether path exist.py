"""
Given a grid of size n*n filled with 0, 1, 2, 3. Check whether there is a path possible from the source to destination. You can traverse up, down, right and left.
The description of cells is as follows:
A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Wall.
Note: There are only a single source and a single destination.
"""


class Solution:

    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        sr, sc = self.findSource(grid)
        return self.bfs(grid, len(grid), sr, sc)

    def bfs(self, grid, n, sr, sc):

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        visited = []

        for i in range(n):
            visited.append([False] * n)
        visited[sr][sc] = True
        row_q = [sr]
        col_q = [sc]

        while row_q != []:

            r = row_q.pop(0)
            c = col_q.pop(0)

            for i in range(4):
                adjr = r + dr[i]
                adjc = c + dc[i]

                if 0 <= adjr < n and 0 <= adjc < n:
                    if grid[adjr][adjc] == 2:
                        return True

                    if grid[adjr][adjc] != 0 and visited[adjr][adjc] == False:
                        visited[adjr][adjc] = True
                        row_q.append(adjr)
                        col_q.append(adjc)

        return False

    def findSource(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    return (i, j)


'''
code for reading input from a file
input should be in this format :
5
3 0 3 0 0 
3 0 0 0 3 
3 3 3 3 3 
0 2 3 0 0 
3 0 0 1 3 
'''


def getParsedInput():
    inp = open('fileInput.txt', 'r')
    lines = inp.readlines()
    validInput = [str(i) for i in range(10)]
    parsedLines = []
    for line in lines:
        for i in range(len(line) - 1, -1, -1):
            if line[i] in validInput:
                parsedLines.append(line[:i + 1])
                break

    return parsedLines


def driver():
    grid = []
    inp = getParsedInput()
    for i in range(1, len(inp)):
        row = list(map(int, inp[i].split(' ')))
        grid.append(row)
    obj = Solution()
    ans = obj.is_Possible(grid)
    if (ans):
        print("Possible")
    else:
        print("Not Possible")


driver()
