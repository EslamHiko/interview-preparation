'''
1192. Critical Connections in a Network
Hard

703

62

Add to List

Share
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''
import collections

def sol(N,connections):
    def checkIsConnected(start,graph):
        visited = {}
        visited[start] = 1

        def dfs(node):

            for n in graph[node]:
                if not visited.get(n):
                    visited[n] = 1
                    dfs(n)

        dfs(start)

        return N == len(visited.keys())

    graph = collections.defaultdict(list)
    for n1,n2 in connections:
        graph[n1].append(n2)
        graph[n2].append(n1)

    critical = {}

    for n in range(N):
        count = 0
        for n2 in graph[n]:
            temp1,temp2 = n2,n
            if n < n2:
                temp1,temp2 = n,n2
            if critical.get((temp1,temp2)):
                continue
            tmp = n2
            graph[n].remove(n2)
            pos2 = graph[n2].index(n)


            if not checkIsConnected(n,graph):
                # connecting it back again
                if n > tmp:
                    critical[(tmp,n)] = 1
                else:
                    critical[(n,tmp)] = 1


            graph[n].insert(count,tmp)
            graph[n2].insert(pos2,n)

            count += 1

    return critical.keys()

print(sol(4, [[0,1],[1,2],[2,0],[1,3]]))

print(sol(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]))
print(sol(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))
print(sol(6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]))
print(sol(9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]))

def sollowlink(n,connections):
    bridges = []
    self.index = 0
    adj_list = [[] for _ in range(n)]
    ids = [0] * n
    low_link = [0] * n
    visited = [False] * n

    # build undirected graph
    for node_1, node_2 in connections:
        adj_list[node_1].append(node_2)
        adj_list[node_2].append(node_1)
    def dfs(current_node, parent_node, bridges):
        visited[current_node] = True

        low_link[current_node] = self.index
        ids[current_node] = self.index
        self.index += 1

        for dest in adj_list[current_node]:
            if dest == parent_node:
                continue
            if not visited[dest]:
                dfs(dest, current_node, bridges)
                low_link[current_node] = min(low_link[current_node], low_link[dest])
                if ids[current_node] < low_link[dest]:
                    bridges.append([current_node, dest])
            else:
                low_link[current_node] = min(low_link[current_node], ids[dest])


    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges)
    return bridges
