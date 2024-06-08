import sys

n , m = map(int, sys.stdin.readline().split())
distance = [(float('INF'))] * (n+1) 
edges = []

for _ in range(m):
    a , b, c =  map(int, sys.stdin.readline().split()) 
    edges.append((a,b,c))

def df(start) :
    distance[start] = 0
    # n-1 번 순회하쥬
    # 정점만큼 순회 
    for x in range(n) :
        # 간선만큼 순회
        for y in range(m) : 
            now = edges[y][0]
            next_node = edges[y][1]
            cost = edges[y][2]
            if now != (float('INF')) and distance[next_node] > distance[now] + cost :
                distance[next_node] = distance[now] + cost
                # n번째 라운드드 값에서도 갱신된다? 그러면 음수 사이클 존재 하는 거유 
                if x == n -1:
                    return True 
    return False 



dfResult = df(1)
if dfResult : 
    print(-1)
else : 
    for i in range(2,n+1) :
        if distance[i] == (float('INF')) :
            print(-1)
        else :
            print(distance[i])

