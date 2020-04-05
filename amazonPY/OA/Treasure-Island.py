'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
Solution
Java BFS: https://leetcode.com/playground/uQoVfEmr
Time complexity: O(r * c).
Space complexity: O(r * c).
'''
import collections

def sol(arr):
    startPoints = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                startPoints.append((i,j))

    def findSolForPoint(i,j,arr):
        q = collections.deque()
        q.appendleft((i,j))
        visited = {}
        currLevel = 0
        levelLen = 0
        visited[(i,j)] = 0

        while len(q):
            curr = q.popleft()
            currLevel = visited[(curr[0],curr[1])]
            res = traverse(curr[0],curr[1],arr,visited,currLevel)
            if res == 'Found':
                return currLevel+1
            else:
                q.extend(res)



        return None


    def traverse(i,j,arr,visited,currLevel):
        level = []
        newLevel = currLevel+1
        # up
        if i != 0 and visited.get((i-1,j)) is None:
            if arr[i-1][j] == 'O':
                level.append((i-1,j))
                visited[(i-1,j)] = newLevel
            elif arr[i-1][j] == 'X':
                return 'Found'

        # down
        if i < len(arr)-1 and visited.get((i+1,j)) is None:
            if arr[i+1][j] == 'O':
                level.append((i+1,j))
                visited[(i+1,j)] = newLevel
            elif arr[i+1][j] == 'X':
                return 'Found'

        # left
        if j != 0 and visited.get((i,j-1)) is None:
            if arr[i][j-1] == 'O':
                level.append((i,j-1))
                visited[(i,j-1)] = newLevel
            elif arr[i][j-1] == 'X':
                return 'Found'

        # right
        if j < len(arr)-1 and visited.get((i,j+1)) is None:
            if arr[i][j+1] == 'O':
                level.append((i,j+1))
                visited[(i,j+1)] = newLevel
            elif arr[i][j+1] == 'X':
                return 'Found'

        return level

    sols = []
    for point in startPoints:
        result = findSolForPoint(point[0],point[1],arr)
        if result:
            sols.append(result)

    print(sols)

    return min(sols) if len(sols) else None

print(sol([
 ['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]))

'''
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

def sol542(matrix):
    startingPoints = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                startingPoints.append((i,j))

    def findShortestPaths(i,j,matrix):
        visited = {}
        visited[(i,j)] = 0
        q = collections.deque()
        q.appendleft((i,j))
        while len(q):
            curr = q.popleft()
            currLevel = visited[(curr[0],curr[1])]
            res = traverse(curr[0],curr[1],matrix,visited,currLevel)
            if res == 'Found':
                return currLevel+1
            else:
                q.extend(res)

        return None

    def traverse(i,j,arr,visited,currLevel):
        level = []
        newLevel = currLevel+1
        # up
        if i != 0 and visited.get((i-1,j)) is None:
            if arr[i-1][j] != 0:
                level.append((i-1,j))
                visited[(i-1,j)] = newLevel
            elif arr[i-1][j] == 0:
                return 'Found'

        # down
        print(i,len(arr))
        if i < len(arr)-1 and visited.get((i+1,j)) is None:
            if arr[i+1][j] != 0:
                level.append((i+1,j))
                visited[(i+1,j)] = newLevel
            elif arr[i+1][j] == 0:
                return 'Found'

        # left
        if j != 0 and visited.get((i,j-1)) is None:
            if arr[i][j-1] != 0:
                level.append((i,j-1))
                visited[(i,j-1)] = newLevel
            elif arr[i][j-1] == 0:
                return 'Found'

        # right
        if j < len(arr[i])-1 and visited.get((i,j+1)) is None:
            if arr[i][j+1] != 0:
                level.append((i,j+1))
                visited[(i,j+1)] = newLevel
            elif arr[i][j+1] == 0:
                return 'Found'

        return level

    print(startingPoints)
    for point in startingPoints:
        result = findShortestPaths(point[0],point[1],matrix)

        if result:
            matrix[point[0]][point[1]] = result

    return matrix
