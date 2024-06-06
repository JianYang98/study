import heapq
import sys
INF = int(1e9)

n , m = map(int,sys.stdin.readline().split())
#print(n)
graph = {i : [] for i in range(1,n+1)}
distance = [INF] * (n+1)
for _ in range(m):
    a, b , c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def dijistra(start) : 
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q :
        dist , now = heapq.heappop(q)
        if distance[now] <dist : 
            continue
        for next_node, weight in  graph[now]  :
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost , next_node ))

dijistra(1)

print(distance[n]) 
