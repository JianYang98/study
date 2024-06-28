import sys

n , m = map(int,sys.stdin.readline().split())

tList = list(map(int,sys.stdin.readline().split()))

for _ in range (m) :
    tList.sort()
    a = tList[0]
    b = tList[1]
    tList[0] = a+b
    tList[1] = a+b

print(sum(tList))
    