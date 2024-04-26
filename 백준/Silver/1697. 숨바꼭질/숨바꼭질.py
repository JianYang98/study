import sys
from collections import deque
sys.setrecursionlimit(10**6)

n , k = map(int , sys.stdin.readline().split())
filedList = [0]*100001



def bfs(start) :
    bqueue = deque([start]) # 노드 , 시간 
    while bqueue :
        v  = bqueue.popleft()        
        if k == v : # 동생 V 랑 bfs랑 같으면 걍 멈춰
            return filedList[v]
        for next_v  in (v-1 , v+1 ,v*2 ) :
            if 0<=next_v<=100000 and  filedList[next_v ] ==0 :
                filedList[next_v ]= filedList[v] + 1
                bqueue.append(next_v)

        



print(bfs(n))




