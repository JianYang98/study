import sys

n = int(sys.stdin.readline().strip())
nList = sorted(list(map(int,sys.stdin.readline().split()))) # O(N log N)
m = int(sys.stdin.readline().strip())
mList = list(map(int,sys.stdin.readline().split()))

dic = {}

for x in nList:
    if x not in dic:
        dic[x] = 1

for y in mList :
    if y in dic :
        print(dic[y] )
    else:
        print(0)
