import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

def DFS(b,a):
    global Danji 

    if a<0 or a>=n or b<0 or b>=n :
        return False
    if dlist[b][a] == 1 :
        Danji+=1
        dlist[b][a] =0
        DFS(b-1,a)
        DFS(b+1,a)
        DFS(b,a-1)
        DFS(b,a+1)
        
        return True
    else:
        return False





dlist = []
for x in range(n):
    aaa=list(map(int,sys.stdin.readline().strip()))
    dlist.append(aaa)

result = []
for a in range(n):
    for b in range(n):
        Danji = 0
        if DFS(b,a) == True :
            result.append(Danji)

print(len(result))
result.sort()
print(*result , sep='\n')
            