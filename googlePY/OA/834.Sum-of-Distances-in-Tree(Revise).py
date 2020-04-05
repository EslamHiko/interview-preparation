'''
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000
'''
def sol(N,graph):
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

    arr = []
    def dist(n1,n2):
        visitedWithLevels = {}


        def bfs(n1):

            q = collections.deque()
            q.appendleft(n1)
            visitedWithLevels[n1] = 0
            distance = float('inf')
            while len(q):

                curr = q.popleft()

                for n in graph[curr]:
                    if n == n2:
                        distance = min(distance,visitedWithLevels[curr]+1)
                    if visitedWithLevels.get(n) is None:
                        visitedWithLevels[n] = visitedWithLevels[curr]+1
                        q.appendleft(n)

            return distance
        length = bfs(n1)
        return length
    memo = {}
    for n1 in range(N):
        sum = 0

        for n2 in range(N):

            if n1 != n2:
                if memo.get((n1,n2)) or memo.get((n2,n1)):
                    if memo.get((n1,n2)):
                        sum += memo[(n1,n2)]
                    else:
                        sum += memo[(n2,n1)]
                else :
                    memo[(n1,n2)] = dist(n1,n2)
                    memo[(n2,n1)] = memo[(n1,n2)]
                    sum += memo[(n1,n2)]

        arr.append(sum)

    return arr

def sol2UnUnderstandable(N,edges):
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    count = [1] * N
    ans = [0] * N
    def dfs(node = 0, parent = None):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

    def dfs2(node = 0, parent = None):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + N - count[child]
                dfs2(child, node)

    dfs()
    dfs2()

    return ans
