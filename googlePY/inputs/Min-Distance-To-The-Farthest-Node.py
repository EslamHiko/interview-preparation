'''
ref : https://leetcode.com/discuss/interview-question/356378/
You are given a tree-shaped undirected graph consisting of n nodes labeled 1...n and n-1 edges. The i-th edge connects nodes edges[i][0] and edges[i][1] together.
For a node x in the tree, let d(x) be the distance (the number of edges) from x to its farthest node. Find the min value of d(x) for the given tree.
The tree has the following properties:

It is connected.
It has no cycles.
For any pair of distinct nodes x and y in the tree, there's exactly 1 path connecting x and y.
Example 1:
Input: n = 6, edges = [[1, 4], [2, 3], [3, 4], [4, 5], [5, 6]]



Output: 2

Example 2:
Input: n = 6, edges = [[1, 3], [4, 5], [5, 6], [3, 2], [3, 4]]



Output: 2

Example 3:
Input: n = 2, edges = [[1, 2]]



Output: 1

Example 4:
Input: n = 10, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]



Output: 5

Example 5:
Input: n = 10, edges = [[7, 8], [7, 9], [4, 5], [1, 3], [3, 4], [6, 7], [4, 6], [2, 3], [9, 10]]



Output: 3

You can assume that input is always valid and satisfies all constraints.

input:
6
1 3
4 5
5 6
3 2
3 4

10
7 8
7 9
4 5
1 3
3 4
6 7
4 6
2 3
9 10
'''
import collections
lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

lines = [el for el in lines if el != '\n' and el != '']
currLine = 0
n = int(lines[currLine])
nodes = [el+1 for el in range(n)]
g = collections.defaultdict(lambda: [])
for i in range(1,len(lines)):
    node,dist = [int(el) for el in lines[i].split()]
    g[node].append(dist)
    g[dist].append(node)


def isLeaf(n,g):
    return len(g[n]) == 1



maxDist = 0

def dfs(prev,n,g,visited):
    global maxDist
    visited[n] = visited[prev] + 1

    if isLeaf(n,g):
        maxDist = max(maxDist,visited[n])

    for node in g[n]:
        if not visited[node]:
            dfs(n,node,g,visited)

def getMaxDistance(node,g):
    global maxDist
    visited = collections.defaultdict(lambda: 0)
    maxDist = 0
    dfs(node,node,g,visited)
    return maxDist - 1


minDistance = float('inf')

for node in nodes:
    minDistance = min(minDistance,getMaxDistance(node,g))

print(minDistance)
