import sys
import heapq
#sys.stdin = open("input.txt" , "r")
# 8:34

INF = float('inf')

def dijkstra(start):
    global n
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    graphTmp[0][0] = graph[0][0]
    q = []
    heapq.heappush(q , (graph[0][0],0,0))

    while q :
        cost , x , y   = heapq.heappop(q)

        for i in range(4) :
            fx = dx[i] + x
            fy = dy[i] + y
            if -1<fx < n and -1< fy< n : # 범위값내고
                if graph[fy][fx] + cost < graphTmp[fy][fx] :
                    graphTmp[fy][fx] = graph[fy][fx] + cost
                    heapq.heappush(q, (graph[fy][fx] + cost, fx,fy))


if __name__ == "__main__":
    cnt = 1
    while True :
        n =  int(sys.stdin.readline().strip())
        if n == 0 :
            break
        graphTmp = [[INF for __ in range(n)] for __ in range(n)]
        graph= []
        for __ in range (n):
            addList = list(map(int , sys.stdin.readline().split()))
            graph.append(addList)
        dijkstra(0)
        print("Problem %d: %d" %(cnt,graphTmp[n-1][n-1]))
        cnt+=1



