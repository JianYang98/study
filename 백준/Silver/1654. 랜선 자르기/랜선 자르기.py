import sys

n, k = map(int,sys.stdin.readline().split())
lineList =[]
for a in range(n):
    lineList.append(int(sys.stdin.readline().strip()))


high = max(lineList)
low = 1
tmp = 0
 
while high>=low:
    lineCnt = 0 
    mid = (high+low)//2
    
    for line in lineList :
        lineCnt+=(line//mid) 
    if lineCnt>=k:
        low = mid+1
    if lineCnt<k:
        high = mid-1
      
print(high)
