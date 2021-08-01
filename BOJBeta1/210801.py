# 1260 DFS와 BFS, 실버 2
n, m, v = map(int, input().split())
nodes = [[0 for i in range(n + 1)] for j in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m) :
    a, b = map(int, input().split())
    nodes[a][b] = 1
    nodes[b][a] = 1

def dfs(v) :
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1) :
        if not visited[i] and nodes[v][i] :
            dfs(i)

def bfs(v) :
    queue = [v]
    visited[v] = 0
    while queue :
        v = queue[0]
        print(v, end=' ')
        queue.pop(0)
        for i in range(1, n + 1) :
            if visited[i] and nodes[v][i] :
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)




