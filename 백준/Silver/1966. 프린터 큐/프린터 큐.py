import sys
from collections import  deque

N = int(sys.stdin.readline())
for x in range(N):
    cnt = 0 
    qeueList =[]
    index , k = map(int , sys.stdin.readline().split())
    tmpList =  deque(list(map(int,sys.stdin.readline().split())))
    while tmpList:
        listMax = max(tmpList)
        if tmpList[0] == listMax :
            if tmpList.index(listMax) == k:
                break            
            tmpList.popleft()
            cnt= cnt+ 1

            k = k-1
        else : 
            tmpList.append(tmpList.popleft())
            k = len(tmpList) -1 if k-1 <0 else k-1
            

    print(cnt+1)
        
        
    