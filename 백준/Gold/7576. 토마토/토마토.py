from collections import deque
import sys

# m 가로 , n 세로 
m , n = map(int,sys.stdin.readline().split())
tList = []
#vistied = [[ -1 for x in range (m) ] for _ in range(n)]
tomato = []
for x in range(n) :
    tmpList = list( map(int,sys.stdin.readline().split()))
    tList.append(tmpList)


# 익은 토마토 위치 찾기
q = deque()
for i in range(n):
    for j in range(m):
        if tList[i][j] == 1:
            q.append((i, j))



dx = [1,-1,0,0]
dy = [0,0,1,-1]
day = -1 
while q :
    day +=1
    for _ in range(len(q)):
        qx , qy = q.popleft()
        #print("qx , qy", qx , qy)
        for i in range(4):
            tx = qx+dx[i]
            ty = qy+dy[i]
            #print("tx , ty", tx , ty)
            #print ( n,m)
            if 0<=tx< n and 0<=ty< m :
                if tList[tx][ty] == 0  :
                    #print(1)
                    tList[tx][ty]  = tList[tx][ty] + 1
                    q.append((tx,ty))

verify = True
for i in range(n):
    if 0 in tList[i]:
        verify = False
        break


if verify :
    print(day)    
else :
    print(-1)






    

