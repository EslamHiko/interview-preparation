'''
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.


Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Note:
grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

input:
3 3
1 1 3
2 1 2
1 1 1
'''
lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

curr_line = 0
m,n = [int(el) for el in lines[curr_line].split()]
grid = []
for i in range(m): # rows
    curr_line += 1
    grid.append([int(el) for el in lines[curr_line].split()])


def findMaxCollect(grid,m,n,x,y,distX,distY,visitMap,pathArr):

    if x >= m or y < 0 or y >= n:
        return 0

    if x == distX and y == distY:
        return grid[x][y]

    # can't reach distnation / reached the bottom
    if not visitMap.get((x,y)):
        sum = max(findMaxCollect(grid,m,n,x+1,y,distX,distY,visitMap,path),findMaxCollect(grid,m,n,x+1,y+1,distX,distY,visitMap,path),findMaxCollect(grid,m,n,x,y-1,distX,distY,visitMap,pathArr))
        if sum == findMaxCollect(grid,m,n,x+1,y,distX,distY,visitMap,pathArr):
            pathArr.append([x+1,y])
        elif sum == findMaxCollect(grid,m,n,x+1,y+1,distX,distY,visitMap,pathArr):
            pathArr.append([x+1,y+1])
        else:
            pathArr.append([x,y-1])

        visitMap[(x,y)] = grid[x][y] + sum

    return visitMap[(x,y)]




visited = {}
path = [[0,0]]
findMaxCollect(grid,m,n,0,0,m-1,0,visited,path)
visited2 = {}
path2 = [[0,n-1]]
findMaxCollect(grid,m,n,0,n-1,m-1,n-1,visited2,path2)

print(visited,path)
print(visited2,path2)
