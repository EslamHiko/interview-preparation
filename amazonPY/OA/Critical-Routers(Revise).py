'''
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
'''

def sol(numNodes,numEdges,edges):
    graph = {}
    for n in edges:
        if graph.get(n[0]):
            graph[n[0]].append(n[1])
        else:
            graph[n[0]] = [n[1]]

        if graph.get(n[1]):
            graph[n[1]].append(n[0])
        else:
            graph[n[1]] = [n[0]]


    def countConnectedNodes(clone):

        start = list(clone.keys())[0]
        visited = {}
        visited[start] = 1
        def dfs(node):

            for n in clone[node]:
                if not visited.get(n):
                    visited[n] = 1
                    dfs(n)

        dfs(start)

        return len(visited.keys())

    result = []
    for n in graph:
        clone = {}
        # copying the graph
        for g in graph:
            clone[g] = graph[g].copy()

        # deleting the bridges connected to the node
        for node in clone[n]:
            if n in clone[node]:
                clone[node].remove(n)

        del clone[n] # deleting the main node


        length = countConnectedNodes(clone)

        if length < numNodes-1:
            result.append(n)

    return result

print(sol(7,7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]))
print(sol(5,5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))
print(sol(6,6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]))
print(sol(9,9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]))
