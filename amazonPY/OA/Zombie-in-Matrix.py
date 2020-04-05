'''
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
 '''


def turnIntoZombies(i, j, arr, orig, count):

    # up
    if i != 0:
        if not arr[i - 1][j]:
            arr[i - 1][j] = 1
            count += 1
    # down
    if i < len(arr) - 1:
        if not arr[i + 1][j]:
            arr[i + 1][j] = 1
            count += 1
    # right
    if j < len(arr[i]) - 1:
        if not arr[i][j + 1]:
            arr[i][j + 1] = 1
            count += 1
    # left
    if j != 0:
        if not arr[i][j - 1]:
            arr[i][j - 1] = 1
            count += 1

    return arr, count


def firstSol(arr):
    target = len(arr) * len(arr[0])
    visited = {}
    curr = 0
    hours = 0
    orig = []
    for x in arr:
        orig.append(x.copy())

    while curr < target:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if orig[i][j] and not visited.get((i, j)):
                    visited[(i, j)] = 1
                    curr += 1
                    arr, curr = turnIntoZombies(i, j, arr, orig, curr)
        orig = []
        for i in (arr):
            orig.append(i.copy())
        hours += 1
    return hours


print(firstSol([[0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]]))

'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''
def sol994(grid):
	counts = {'fresh':0,'rotten':0,'empty':0}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                counts['rotten'] += 1
            if grid[i][j] == 1:
                counts['fresh'] += 1
            else:
                counts['empty'] += 1

    if not counts['fresh'] and counts['rotten']:
        return 0
    if not counts['rotten'] and not counts['fresh']:
        return 0
    if counts['fresh'] and not counts['rotten']:
        return -1

    def infectNeighbours(i,j,arr):
        #up
        if i != 0:
            if arr[i - 1][j] == 1:
                arr[i - 1][j] = 2

        # down
        if i < len(arr) - 1:
            if arr[i + 1][j] == 1:
                arr[i + 1][j] = 2

        # right
        if j < len(arr[i]) - 1:
            if arr[i][j + 1] == 1:
                arr[i][j + 1] = 2

        # left
        if j != 0:
            if arr[i][j - 1] == 1:
                arr[i][j - 1] = 2

    tmp = []
    for x in grid:
        tmp.append(x.copy())

    visited = {}
    target = counts['fresh'] + counts['rotten']
    prev = len(visited.keys())
    minutes = 0
    while prev < target:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if tmp[i][j] == 2 and not visited.get((i,j)):
                    visited[(i,j)] = 1
                    infectNeighbours(i,j,grid)

        totaInfected = len(visited)
        if prev == totaInfected:
            return -1
        else:
            prev = totaInfected
        minutes += 1
        tmp = []
        for x in grid:
            tmp.append(x.copy())

    return minutes-1
