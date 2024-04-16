import sys
n , m = map(int, sys.stdin.readline().split())
treeList =  list(map(int, sys.stdin.readline().split()))
tmp = 0
low = 1 
high = max(treeList)

while high>=low : 
    tmpCnt = 0
    mid = (low+high)//2

    for tree in treeList:
        if tree > mid:
            tmpCnt += tree-mid
    if tmpCnt >= m :
        low = mid+1
    elif tmpCnt<m :
        high= mid-1
        
print(high)