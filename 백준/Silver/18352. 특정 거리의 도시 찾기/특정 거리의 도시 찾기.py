import sys
import heapq

INF = int(1e9)
n , m, k, start = map(int,sys.stdin.readline().split())
#graph =[ [0 for i in range(n+1)] for i in range(n+1) ]
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
result = []
# 방문 
visited = [False] * (n+1)

#그래프 정보 입력
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append((b, 1)) # 노드번호 , 가중치 

def dijkstra(start) : 
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0    
    while q :
        # 우선 안에 있는 큐를 탈탈탈
        dist , now = heapq.heappop(q)
        # 이미 전에 처리된 노드면 NEXT
        if distance[now] < dist:
            continue 
        # now 노드와 연결된 인접이들 확인요     
        for i in graph[now] :
            # 노드들 간 거리들 계산
            cost = dist + i[1] 
            
            # 현재 노드를 거쳐서 인접 노드로 이동하는 거리가 더 짧은 경우
            # 노들의 거리 보다 <  지금까지 최단 거리가 더클때
            if cost < distance[i[0]] :
                distance[i[0]] = cost # 이동거리 넣어줌
                heapq.heappush(q,(cost,i[0]))            
            




    
dijkstra(start)

for i in range(1, n+1):
    # 최단 거리 저장한 곳에서  k와 같으면 ? ㄱ
    if distance[i] == k: 
        result.append(i)
if len(result) == 0: 
    print(-1)        
else:
    for x in result :
        print(x)





