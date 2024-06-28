import sys
import heapq

n , m = map(int,sys.stdin.readline().split())

tList = list(map(int,sys.stdin.readline().split()))
heapq.heapify(tList)

for _ in range (m) :
    x = heapq.heappop(tList)
    y = heapq.heappop(tList)
    heapq.heappush(tList,x+y)
    heapq.heappush(tList,x+y)

print(sum(tList))
    