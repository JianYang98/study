import sys

n , m = map(int,sys.stdin.readline().split())

result = []

def DFS():
    if len(result) == m :
        print(*result)
        return 
    else :
        for x in range(1,n+1) :
                result.append(x)
                DFS()
                result.pop()

DFS()


