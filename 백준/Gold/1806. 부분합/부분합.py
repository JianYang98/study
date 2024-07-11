from collections import deque
import sys

n , m = map(int,sys.stdin.readline().split())
tList= list(map(int,sys.stdin.readline().split()))

sumList = deque([])
curLen = float('INF')


rigth= 0
left = 0
sum  = 0 

while True : 
    if sum >= m :
        curLen = min(curLen , rigth-left)
        sum -= tList[left]
        left+=1
    elif rigth == n :
        break
    else: 
        sum += tList[rigth]
        rigth +=1

if curLen !=float('INF') :
    print(curLen)
else :
    print(0)



