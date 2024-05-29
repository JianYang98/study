import heapq

def dijkstra(graph,distince):
    q=[]
    # 처음에는 처음의 값은 0 #간선은 1임
    heapq.heappush(q,(0,1))
    
    while q:
        dist , now = heapq.heappop(q)
        #print(distince)
        if distince[now] < dist :
            continue
        for b in graph[now]:
            hap = dist+ b[1]
            if hap < distince[b[0]]:
                distince[b[0]] = hap
                heapq.heappush(q,(hap,b[0]))
    return distince


def solution(N, road, K):
    answer = 0
    
    #그래프
    graph ={i:[] for i  in range(N+1)}
    
    #최단거리 테이블
    distince = [int(1e9) for _ in range (N+1) ]
    # 내 자신은 1이다 
    distince[1] = 1

    # 그래프 세팅 
    beforeA =int(1e9)
    beforeB =int(1e9)
    beforeC =int(1e9)

    for a,b,c in road :
        if beforeA == a and beforeB == b and beforeC<c:
            c = beforeC
        
        graph[a].append((b,c))
        graph[b].append((a,c))
        beforeA = a
        beforeB = b
        beforeC = c        
        
    
    result =dijkstra(graph , distince)
    #print(result)
    for res in  result :
        if res<=K:
            answer+=1
    print(answer)
    return answer