import sys
sys.setrecursionlimit(10**6)

def DFS(a,b):
    

    # 상하좌우
    fx = [0, 0, -1, 1] 
    fy = [1, -1, 0, 0]
    
    for i in range(4) : 
        dx = a+fx[i]
        dy = b+fy[i]
        if (0<=dx<m) and (0<=dy<n) and feild[dy][dx] == 1 :
            feild[dy][dx] = -1 # 탐색 쌉완료
            DFS(dx,dy)




t = int(sys.stdin.readline().strip())

while t>0 :
    m,n,k = map(int,sys.stdin.readline().rstrip().split())
    feild= [ [0 for __ in range(m)] for __ in range(n)]

    # 배추 배추 심자!! 배추 
    for __ in range(k):

        xx ,yy = map(int,sys.stdin.readline().rstrip().split())
        feild[yy][xx] =1 
        
    result = 0
    for a in range(m): # x,y 바꿔서 입력조심 하시길 # 배추는 x,y순으로 입력되지만 실제는 [y][x]로 입력해야한다.
        for b in range(n):
            if feild[b][a] == 1 :
                DFS(a,b)
                result+=1

    print(result)    
    t-=1
