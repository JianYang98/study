import sys
sys.setrecursionlimit(10**6)


n, m = map(int, sys.stdin.readline().split())
graph = {}
cnt = 0

def DFS(i):
    visited[i] = True 
    if i in graph:
        for x in graph[i]:
            if visited[x] == False :
                DFS(x)
            
for __ in range (m):
    u, v = map(int, sys.stdin.readline().split())
    if u in graph:
        graph[u].append(v)
    else :
        graph[u] = [v]

    if v in graph:
        graph[v].append(u)
    else :
        graph[v] = [u]

visited = [ False for __ in range(n+1)]

for i in range(1,n+1):
    if visited[i] == False :
        DFS(i)
        cnt += 1


print(cnt)

