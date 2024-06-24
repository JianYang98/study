from collections import deque 

def bfs(maps,n,m) :
    tmpresult = -1
    q  = deque([(0,0)])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q :
        qx , qy =  q.popleft()
        if n-1 == qx and m-1 == qy :
            tmpresult = maps[qx][qy]
            break
        for i in range(4):
            fx = qx + dx[i]
            fy = qy + dy[i]
            if 0<= fx < n and  0<= fy < m :
                if maps[fx][fy] == 1 :
                    maps[fx][fy] = maps[qx][qy] + 1
                    q.append((fx,fy))
    return tmpresult
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    answer = bfs(maps,n,m)
    return answer