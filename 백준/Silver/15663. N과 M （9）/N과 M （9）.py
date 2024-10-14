import sys

n , m = map(int, sys.stdin.readline().split())
tList = list(map(int, sys.stdin.readline().split()))

# 정렬
tList.sort()
visitMoment = []
visit = [False] * n

def DFS (k) :
    # visitMoment에 전칸과 내가 같아? 그럼 ㄴ
    #print(k)
    check = 0 

    if len(visitMoment) == m :
        print(*visitMoment)
    else :
        for i in range(n) :
            if visit[i] == False and check != tList[i] :

                visit[i] = True
                visitMoment.append(tList[i])
   
                DFS(k+1)
                check = visitMoment.pop()
                visit[i] = False


DFS(0)