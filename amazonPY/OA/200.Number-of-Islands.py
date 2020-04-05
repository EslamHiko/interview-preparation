    '''
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

def sol(grid):
    visited = {}

    def traverse(i,j,grid,visited):
        # up
        if i > 0:

            if not visited.get((i-1,j)) and grid[i-1][j] != "0":

                visited[(i-1,j)] = 1
                traverse(i-1,j,grid,visited)
        # down
        if i <  len(grid)-1:
            if not visited.get((i+1,j)) and grid[i+1][j] != "0":
                visited[(i+1,j)] = 1
                traverse(i+1,j,grid,visited)

        # right
        if j < len(grid[i])-1:
            if not visited.get((i,j+1)) and grid[i][j+1] != "0":
                visited[(i,j+1)] = 1
                traverse(i,j+1,grid,visited)

        # left
        if j > 0:
            if not visited.get((i,j-1)) and grid[i][j-1] != "0":
                visited[(i,j-1)] = 1
                traverse(i,j-1,grid,visited)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not visited.get((i,j)) and grid[i][j] != "0":

                visited[(i,j)] = 1
                count += 1
                traverse(i,j,grid,visited)

    return count
