import heapq
import sys
INF = int(1e9)
# n 학생 , m 도로 , x 마을
n , m ,x = map(int,sys.stdin.readline().split())


graph = {i : [] for i  in range(1,n+1)}

for _ in range(m):
    a, b ,c = map(int,sys.stdin.readline().split())    
    graph[a].append((b,c))
# X 에서 모든 간선 
def dijkstra(start) :
    distance = [ INF ] * (n+1)
    # 방문 안하는 0 과 시작점 strat 0으로 세팅 
    distance[0] = 0
    distance[start] = 0
    q =[]
    heapq.heappush(q,(0,start))
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for next_node , weight in graph[now] :
            cost = dist + weight
            if distance[next_node] > cost :
                distance[next_node] = cost
                heapq.heappush(q,( cost,next_node ))
            
            
    return distance



# x에서 모든 정점까지
fulltime = dijkstra(x)
#print(distTime)
for num in range(1,n+1):
    if num ==0 :
        continue
    returnTime = dijkstra(num)  # num에서 다익스트라 ㄱㄱ ㅇ
    fulltime[num] +=returnTime[x]  # num에서 시작한 다익스트라에서 x까지의 값으로 업뎃

print(max(fulltime))
    
