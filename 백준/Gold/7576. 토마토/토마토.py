import sys
from collections import deque
#sys.stdin = open("input.txt", "r")


def BFS (toCnt):
    global  n , m
    #print("toCnt ",toCnt) # 토마토 갯수
    day = -1
    tomatoCont = len(tomamoTmp)
    tomamo= deque(tomamoTmp)
    while tomamo :
        x ,y ,nowday= tomamo.popleft()
        #print(x,y)
        day = max(day ,nowday )

        visited[y][x] = True
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for a in range(4):
            tx = x +dx[a]
            ty = y +dy[a]
            if 0<=tx<m and 0<=ty<n : # 범위값안일때
                #print("tx : ",tx ," ty :",ty)
                if visited[ty][tx] == False and  tList[ty][tx] ==0:
                    visited[ty][tx] = True
                    tomatoCont += 1
                    tomamo.append((tx,ty,nowday+1))
    #print(tomatoCont)
    if tomatoCont == toCnt :
        print( day )
    elif tomatoCont <toCnt :
        print(-1)


if __name__ == "__main__" :
    m, n = map(int, sys.stdin.readline().split()) # m 은 x ,n는 y임
    tomamoTmp = []
    visited = [[False  for __ in range(m)] for __ in range(n)]
    #print(visited)
    tList = []
    ne = 0 # -1 갯수
    cnt = 0
    toCnt = 0
    for y in range(n):
        t = list(map(int, sys.stdin.readline().split()))
        # print(t)
        tList.append(t)
        for a in range(m):
            if t[a] == 1:
                tomamoTmp.append((a, y,0))
            elif t[a] == -1:
                ne+=1
    toCnt = (n * m )- ne # 총 카운트 해야하는 토마토 갯수

    BFS(toCnt)
