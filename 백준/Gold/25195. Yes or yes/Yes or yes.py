import sys
sys.setrecursionlimit(10**6)
#sys.stdin = open("input.txt" , "r")
#  DFS로 백트래킹으로 풀자
def DFS(v):
    global n , m
    global  result
    if v > m :
        return
    if len(graph[v]) == 0:
        result = True # 팬안만나는 길이 존재한다.
        return
    for ele in graph[v] :
        if ele not in fanList:
            if visit[ele] == False :
                visit[ele] = True
                DFS(ele)
                visit[ele] = False
    return

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for __ in range(n+1)]
    for __ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    fan = int(sys.stdin.readline().strip())
    fanList = list(map(int, sys.stdin.readline().split()))
    visit = [False] * (n+1)
    FanVisit = [False] * (n+1)

    result = False
    if 1 not in fanList :
        val = DFS(1)
    if result :
        print("yes")
    else :
        print("Yes")
