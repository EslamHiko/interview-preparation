n = int(input())
finalResult = ''

def traverse(p,graph,visited):
    visited[p] = 1
    if graph.get(p):
        for project in graph[p]:
            if not visited.get(project):
                traverse(project,graph,visited)

for n in range(n):
    graph = {}
    visited = {}
    k,j = [int(el) for el in input().split()]
    for el in range(k):
        X,Y = input().split()
        if not graph.get(Y):
            graph[Y] = [X]
        else:
            graph[Y].append(X)

    for j in input().split():
        visited[j] = 1

    currDelayed = list(visited.keys())
    for p in currDelayed:
        traverse(p,graph,visited)

    print('Case #'+str(n+1)+': '+' '.join(sorted([el for el in visited.keys()]))+'\n')
