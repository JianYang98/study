import sys
n = int(sys.stdin.readline().strip())
nList =[[0 for _ in range(n) ] for __ in range(n)]

startFlag = False 
starX = 0
starY = 0 
armSCountL =0
armSCountR =0
ss =[]
for i in range(n):
    startList = list(sys.stdin.readline().strip())
    ss.append(startList)
    for x in range(n):
        if startFlag  == False :
            if startList[x] == '*':
                startFlag = True
                starX = i+2 # 좌표설정
                starY= x +1 # 좌표설정
                print(starX,starY)
#왼
cnt = 0
for i in range(starY-1 ):
    if ss[starX-1][i] == "*":
        cnt+=1
print(cnt, end=" ")

#오
cnt = 0
for i in range(starY , n):
    if ss[starX-1][i] == "*":
        cnt+=1
print(cnt, end=" ")

#허리
cnt=0
k = starX
while True :
    if ss[k][starY-1] == "_":
        break
    k+=1
    cnt+=1
print(cnt, end=" ")

c=k
#왼쪽
cnt=0
while k <n :
    if ss[k][starY-2] == "_":
        break
    k+=1
    cnt+=1
print(cnt, end=" ")
        
        
#오
#왼쪽
cnt=0
while c <n :
    if ss[c][starY] == "_":
        break
    c+=1
    cnt+=1
print(cnt, end=" ")


