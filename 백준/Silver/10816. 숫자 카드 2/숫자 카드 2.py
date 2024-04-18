import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
nList = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
mList = list(map(int,sys.stdin.readline().split()))
nCounter = Counter(nList)

for a in range(len(mList)) :
    print( nCounter[mList[a]] , end=' ' )