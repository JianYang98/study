import sys
#sys.stdin = open("input.txt" , "r")
# 9 : 36
import heapq
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q,(0 ,  start )) # 거리 , now
    distnace[start] = 0
    while q :
        dist , now = heapq.heappop(q)
        if distnace[now] < dist :
            continue
        for a in mList[now] :
            cost = dist +1
            if cost < distnace[a] :
                distnace[a] = cost
                heapq.heappush(q,(cost , a ))

if __name__ == "__main__":
    n , m , k ,x = map(int, sys.stdin.readline().split())
    mList = [[] for __ in range(n+1)]
    distnace = [INF] * (n+1)

    for __ in range(m) :
        a ,b = map(int, sys.stdin.readline().split())
        mList[a].append(b)


    dijkstra(x)
    result = []
    for b in range(1,n+1):
        if distnace[b] ==  k :
            result.append(b)
    if len(result) == 0:
        print(-1)
    else:
        for x in result:
            print(x)
