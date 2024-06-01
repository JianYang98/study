from collections import deque
import sys
INF = int(1e9)

n , m = map(int, sys.stdin.readline().split())
distances  = [   [ -1 for _ in range(m) ] for _ in range(n) ]
visited = [ [False for _ in range(m) ]  for _ in range(n)]
graph = []

x2 = -1
y2 = -1
for x in range(n) :
    xList = list(map(int , sys.stdin.readline().split()))
    if 2 in xList :
        x2 =x 
        y2 = xList.index(2)
        
        
    graph.append(xList)
distances[x2][y2] = 0

def BFS(x , y) :
    #상하좌우우
    dx = [ 1, -1, 0, 0]
    dy = [ 0, 0, -1, 1]
    q = []
    q = deque([(x,y)])
    # 시작점 방문 처리 리
    visited[x][y] = True

    while q :
        a= q.popleft()
        #print(a)
        nowx = a[0]
        nowy = a[1]

        # 상하 좌우 
        for i in range(4):
            nowx_new = nowx + dx[i]
            nowy_new = nowy + dy[i]
            if (0<= nowx_new <=n-1) and (0<= nowy_new<=m-1):
#                if graph[nowx_new][nowy_new] == 0: 
#                    distances[nowx_new][nowy_new] = 0 
                if graph[nowx_new][nowy_new] == 1 and not visited[nowx_new][nowy_new] :
                    q.append((nowx_new,nowy_new))
                    visited[nowx_new][nowy_new] = True
                    distances[nowx_new][nowy_new] = distances[nowx][nowy] + 1





BFS(x2 , y2)
for a in range(n):
    for b in range(m) :
        if graph[a][b] == 0 : 
            distances[a][b] = 0
    print(*distances[a])

