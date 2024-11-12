import sys
#sys.stdin = open("input.txt" , "r")
# 8:34

INF = float('inf')

def bef(start):
    distance[start] = 0
    global n,m
    # 노드
    for i in range(1, n+1) :
        for j in range(m) :
            currNode = tList[j][0]
            nextNode = tList[j][1]
            cost = tList[j][2]
            if distance[currNode] != INF and distance[nextNode] >distance[currNode]+ cost :
                distance[nextNode] = distance[currNode]+ cost
                if i == n :
                    return True
    return False




if __name__ == "__main__":
    n , m = map(int , sys.stdin.readline().split())
    distance = [INF] *(n+1)
    tList = []

    for _ in range(m):
        a , b, c = map(int , sys.stdin.readline().split())
        tList.append((a,b,c))

    result = bef(1)
    if result :
        print(-1)
    else :
        for i in range(2,n+1) :
            if distance[i] == INF :
                print(-1)
            else :
                print(distance[i])



