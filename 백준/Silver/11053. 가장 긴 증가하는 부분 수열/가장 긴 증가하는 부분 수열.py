import sys
from bisect import bisect_left 

n = int(sys.stdin.readline().strip())
tList = list(map(int,sys.stdin.readline().split() ) )

# 수열 담는 List 
xList = [tList[0]]

# DP테이블
dp = [1] 

for i in range(1,n):
    if tList[i] > xList[-1]:
        #print("tList[i-1] < tList[i] " ,tList[i-1], tList[i]  )
        xList.append(tList[i])
        dp.append(dp[-1]+1)
        #print("dp" , dp)
        #print(xList)
    else :
        idx = bisect_left(xList ,tList[i] )
        xList[idx] = tList[i]

print(max(dp))
#print("xList " , xList)
#print("xList len " , len(xList))
#print("dp " , dp)
#print("dp len " , len(dp))
