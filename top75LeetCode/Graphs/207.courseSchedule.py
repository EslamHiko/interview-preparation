'''
Topoligcal Sort problem
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
'''
   [[1, 0]]

   0 --> 1

   2, [[1,0],[0,1]]

   0 --> 1
     <--
     cycle

     finding if a topological ordering is possible <-> there's no cycle


     0 -> 1 ->....y... x
          <-------
                       visiting =  1
                       visited = [x, ....]

         x ----> y ---> z

         u ---> v

         w --> m

     DFS
     - traverse all nodes with dfs + keep two ds visited list (contains nodes that we are done exploring - including neighbors), visiting list (we started explored this node but haven't finished going through all its neighbors)
     - when we start exploring a node add it to the visiting list
     - once all neighbors of a node have been visited -> remove it from visiting list and add it to visited
     - if we call dfs on a node that is already in the visiting list -> we have cycle -> topological ordering is not possible -> return false

     - outer loop to make sure we touch all nodes in the graph

    Time complexity: O(E + V)
    Space complexity: O(V)

    visit :  0: not touched yet (<->  not in the list)
            -1: visiting
            1: visited

   '''
def canFinish(numCourses,prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for j, i in prerequisites:
        graph[i].append(j)
    print(graph)
    def dfs(i): # checks for that graph is acyclic (if there's a cycle return false else return true)
        if visit[i] == 1:
            return True
        if visit[i] == -1:
            return False
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True

    for i in range(numCourses):
        if  not dfs(i):
            return False

    return True

print(canFinish(2, [[1,0],[0,1]]))
print(canFinish(2, [[0,1]]))

'''
   BFS

   indegree: how many edge are coming into a node

Y --->
       X
  -->

 indegree(X) = 2
 indegree(Y) = 0 -> we can take that course right away <=> adding it to our bfs queue

 if we take a course -> all those that depend on it have one less dependency  -> substracting one from the count of its indegrees

 BFS
 1 - Calculate the indegrees and adj list of all nodes in the graph
 2 - Go through indegree and add those with 0 indegree to bfs queue
 3 - start bfs and all pop from the queue = x
 4 - go through all neighbors of x and substract their indegree by 1
     If any of these neighbors became with indegree 0 then add it to the queue
 5 - keep counting the nodes we added to the queue (= the courses we've taken) = count
 6 - if count = number of courses -> we were able to process all courses


 Time complexity: O(V + E)
 Space complexity: O(V + E)
 
   '''
def canFinish(n, pre):
    graph = [[] for i in range(n)]
    indegree = [0 for _ in range(n)]
    for j, i in pre:# 1
        graph[i].append(j) # i ----> j
        indegree[j] += 1
    queue = collections.deque([i for i in range(n) if indegree[i] == 0]) # 2
    count = len(queue)
    while queue: # 3
        i = queue.popleft()
        for j in graph[i]: # 4
            indegree[j] -= 1
            if indegree[j] == 0:
                count += 1
                queue.append(j)
    return count == n
