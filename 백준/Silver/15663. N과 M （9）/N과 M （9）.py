import sys

n , m = map(int,sys.stdin.readline().split())
nList = list(map(int,sys.stdin.readline().split()))
nList.sort()

result = []
res = [False]*n

def DFS():
    check = 0
    if len(result) == m :
        print(*result)
        return 
    else :
        for x in range(n) :
            if res[x] == False and check != nList[x] :
                result.append(nList[x])
                check = nList[x]
                res[x] = True
                DFS()
                result.pop()
                res[x] = False

DFS()


