import sys


def DFS(k , dList ,visited ) : 
    print(k , end=' ')
    if visited[k] == False : # 방문 여부 체크 후 방문
        visited[k] = True
        
    for x in range(1,n+1) :
        if visited[x] == False and dList[k][x] == 1: # 처음 방문이고 있으면 ,DFS 재귀타기
            DFS(x ,dList ,visited )

def BFS(k , dList, visited2) :
    bfsQ = [k]
    visited2[k] = True #방문처리

    while  bfsQ : 
        v = bfsQ.pop(0) # 방문 노드 제거거
        print(v, end =' ')
        for i in range(1, n+1):
            if(visited2[i] == False and dList[v][i]):
                bfsQ.append(i)
                visited2[i] = True # 방문처리리

n , m , k = map(int,sys.stdin.readline().split())
nList = [[0] * (n+1) for i in range(n+1)]
for a in range(m):
    b,c = map(int,sys.stdin.readline().split())
    nList[b][c] = 1
    nList[c][b] = 1

visited = [False]*(n+1) 
visited2 = [False]*(n+1) 


DFS(k,nList , visited)
print()
BFS(k,nList , visited2)