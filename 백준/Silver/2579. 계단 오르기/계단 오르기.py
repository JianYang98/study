import sys

t = int(sys.stdin.readline().strip())

xList = [0] * 301
DP = [0] * 301
for x in range(t):
    xList[x] = (int(sys.stdin.readline().strip()))

DP[0] = xList[0] # 첫번째 계단ㄱ
DP[1] = xList[0] + xList[1] # 두번째 계단 ㄱ
DP[2] = max((xList[1]+xList[2]) , (xList[0]+xList[2]) ) # 세번째 계단

for x in range(3,t) :
    DP[x] = max( ( DP[x-3] + xList[x-1] + xList[x] ),  (DP[x-2] + xList[x]))

print(DP[t-1])