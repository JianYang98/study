#8:31
import sys

n , m = map(int, sys.stdin.readline().split())
tList = list(map(int, sys.stdin.readline().split()))

# 정렬
tList.sort()
visitMoment = []
visit = [False] * n

def DFS (k) :

    if len(visitMoment) == m :
        print( *visitMoment)
    else :
        for i in range(1,n+1) :

            visitMoment.append(i)
   
            DFS(k+1)
            visitMoment.pop()

       
        
    



DFS(0)