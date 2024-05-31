import heapq
import sys
INF = int(1e9)

#총 갯수
n = int(sys.stdin.readline().strip())
# 기억할 관계 값 
a1 ,a2 = map(int,(sys.stdin.readline().split()))
# 관계 수
m = int(sys.stdin.readline().strip())

#distance
visted = [INF]*(n+1)
#디버기용

#그래프
graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    a ,b = map(int,(sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

# 다익스트라 최단거리 테이블 초기화
distance = [int(1e9) for _ in range(n+1)]

#다익스트라 ㄱㄱ
def dijistra(start) : 
    q=[]
    heapq.heappush(q,(0,start))
    distance[a1] = 0
    while q : 
        dist , now = heapq.heappop(q)
    
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
dijistra(a1)
if distance[a2] != int(1e9):
    print(distance[a2])
else:
    print(-1)


