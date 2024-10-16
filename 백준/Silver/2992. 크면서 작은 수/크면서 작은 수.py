import sys

n = int(sys.stdin.readline().strip())
m = list(map(int,str(n)))
tmpMin = float('inf')
resultTmp=[]
result = []
visited = [False] * len(m)
def DFS(N):
    global tmpMin 
    before = float('inf')
    
    if len(result) == len(m) :
        currentValue =  int(''.join(map(str,result))) 
        if n < currentValue :
            resultTmp.append(currentValue)
            return ;
    for x in range (len(m)):
        if visited[x] == False and m[x]!=before :
            result.append(m[x])
            visited[x] = True
            DFS(N+1)
            before = result.pop()
            visited[x] = False

DFS(0)

if len(resultTmp) == 0 :
    print(0)
else :
    print(min(resultTmp))

