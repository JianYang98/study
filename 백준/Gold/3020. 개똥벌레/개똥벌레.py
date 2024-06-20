import sys
sys.setrecursionlimit(10**6)

n , h = map(int,sys.stdin.readline().split())
top = [0] * (h+1)
bottom = [0] * (h+1)

# top , bottom 세팅
for i in range (n) :
     num = (int(sys.stdin.readline().strip()))
    # num는 장애물이다. num크기의 장애물 몇개인지 count
     if i%2 == 0 :
         bottom[num] +=1      
     else :
         top[num] +=1          
#print(bottom)

# 가중치 계산하기 
for x in range(h-1 , 0 , -1) :
        bottom[x] +=bottom[x+1]
        top[x] += top[x+1]

minCnt = n
minIndex = 0

# 장애물 계산
for x in range(1,h+1) :
    barrier = bottom[x] + top[h+1-x]
    #print(" minCnt " , minCnt ," barrier " , barrier)
    if barrier < minCnt:
        minCnt = barrier
        minIndex = 1
    elif barrier == minCnt:
        minIndex += 1

print(minCnt,minIndex)

