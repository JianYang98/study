import sys
import heapq
INF = int(1e9)
n , d = map(int,sys.stdin.readline().split())

graph = [ [] for _ in range(d+1)]
distance = [INF]*(d+1)
result = 0

# 일단 거리 초기화
for i in range(d+1):
    graph[i].append((i+1 , 1))

# 지름길이 있는 경로 세팅 

for i in range(n) :
    s , e , g = map(int, sys.stdin.readline().split()) 
    # 끝 값이 d 보다 크면 역주행 불가래서 X 
    if e > d :
        continue
    graph[s].append((e,g))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    # 처음 위치 초기화
    distance[start] = 0
    while q : 
        dist ,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            
            cost = dist + i[1]
            if i[0] > d :
                continue
            elif cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost , i[0] ))
    
    


dijkstra(0)
print(distance[d])